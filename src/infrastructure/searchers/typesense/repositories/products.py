from typing import override
import time

import typesense

from src.infrastructure.searchers.typesense.interfaces import ProductsTypesenseRepositoryInterface
from src.infrastructure.searchers.typesense.settings import get_typesense_settings


class ProductsTypeSenseRepositoryImplement(ProductsTypesenseRepositoryInterface):
    def __init__(self) -> None:
        self.client = get_typesense_settings().get_typesense_client()
        time.sleep(5)
        self.create_schema()

    @override
    def create_schema(self) -> None:
        schema = {
            'name': 'products',
            'fields': [
                {'name': 'id', 'type': 'string'},
                {'name': 'title', 'type': 'string'},
                {'name': 'description', 'type': 'string'},
                {'name': 'brand', 'type': 'string'},
                {'name': 'category', 'type': 'string'},
                {'name': 'price', 'type': 'float'},
                {'name': 'features', 'type': 'string'}
            ]
        }
        try:
            self.client.collections.create(schema)
        except typesense.exceptions.ObjectAlreadyExists:
            pass

    @override
    def add_product(self, product_data: dict) -> None:
        self.client.collections['products'].documents.create({
            'id': product_data['uuid'],
            'title': product_data['title'],
            'description': product_data['description'],
            'brand': product_data['brand'],
            'category': product_data['category_id'],
            'price': product_data['price_after_discounts'],
            'features': product_data['features']
        })

    @override
    def search_similar(self, product_data: dict) -> None:
        search_parameters = {
            'q': search_query,
            'query_by': 'title,description',
            'num_typos': 2,
            'page': 1,
            'per_page': 5
        }
        return self.client.collections['products'].documents.search(search_parameters)
