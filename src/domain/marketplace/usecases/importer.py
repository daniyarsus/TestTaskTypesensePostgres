from bindme import inject
import uuid
import lxml.etree as ET
from fastapi import UploadFile

from src.infrastructure.db.postgres.interfaces import PublicSkuPostgresRepositoryInterface
from src.infrastructure.searchers.typesense.interfaces import ProductsTypesenseRepositoryInterface


class ProcessDataUseCase:
    @inject
    def __init__(
            self,
            public_sku_postgres_repo: PublicSkuPostgresRepositoryInterface,
            products_typesense_repo: ProductsTypesenseRepositoryInterface
    ) -> None:
        self._public_sku_postgres_repo = public_sku_postgres_repo
        self._products_typesense_repo = products_typesense_repo

    async def __call__(self, file: UploadFile) -> None:
        context = ET.iterparse(file.file, events=('end',), tag='offer')
        for event, elem in context:
            product_data = {
                'uuid': str(uuid.uuid4()),
                'marketplace_id': int(elem.get('id')),
                'product_id': int(elem.find('product_id').text) if elem.find('product_id') is not None else None,
                'title': elem.find('name').text if elem.find('name') is not None else None,
                'description': elem.find('description').text if elem.find('description') is not None else None,
                'brand': elem.find('vendor').text if elem.find('vendor') is not None else None,
                'seller_id': int(elem.find('vendorCode').text) if elem.find('vendorCode') is not None else None,
                'seller_name': elem.find('vendor').text if elem.find('vendor') is not None else None,
                'first_image_url': elem.find('picture').text if elem.find('picture') is not None else None,
                'category_id': int(elem.find('categoryId').text) if elem.find('categoryId') is not None else None,
                'category_lvl_1': None,
                'category_lvl_2': None,
                'category_lvl_3': None,
                'category_remaining': None,
                'features': {},
                'rating_count': None,
                'rating_value': None,
                'price_before_discounts': float(elem.find('price').text) if elem.find('price') is not None else None,
                'discount': None,
                'price_after_discounts': float(elem.find('price').text) if elem.find('price') is not None else None,
                'bonuses': None,
                'sales': None,
                'currency': elem.find('currencyId').text if elem.find('currencyId') is not None else None,
                'barcode': int(elem.find('barcode').text) if elem.find('barcode') is not None else None,
                'similar_sku': []
            }

            await self._public_sku_postgres_repo.add_one(product_data=product_data)
            self._products_typesense_repo.add_product(product_data=product_data)
            elem.clear()

        rows = await self._products_typesense_repo.fetch_all()
        for row in rows:
            product_uuid, title, description = row['uuid'], row['title'], row['description']
            search_query = f"{title} {description}"
            search_results = await self._products_typesense_repo.search_similar(search_query=search_query)
            similar_uuids = [hit['document']['id'] for hit in search_results['hits'] if
                             hit['document']['id'] != product_uuid]
            await self._public_sku_postgres_repo.update_one(product_uuid, similar_uuids)
