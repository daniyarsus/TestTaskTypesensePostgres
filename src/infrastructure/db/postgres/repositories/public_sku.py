from typing import override
import json

from src.infrastructure.db.postgres.interfaces import PublicSkuPostgresRepositoryInterface
from src.infrastructure.db.postgres.settings import get_postgres_settings


class PublicSkuPostgresRepositoryImplement(PublicSkuPostgresRepositoryInterface):
    @override
    async def add_one(
            self,
            product_data
    ) -> None:
        conn = await get_postgres_settings().get_async_postgres_connect()
        async with conn.transaction():
            await conn.execute(
                '''
                INSERT INTO public.sku (uuid, marketplace_id, product_id, title, description, brand, 
                          seller_id, seller_name, first_image_url, category_id, category_lvl_1, category_lvl_2, 
                          category_lvl_3, category_remaining, features, rating_count, rating_value, 
                          price_before_discounts, discount, price_after_discounts, bonuses, sales, currency, 
                          barcode, similar_sku) 
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, 
                        $18, $19, $20, $21, $22, $23, $24, $25)
                ''',
                product_data['uuid'], int(product_data['marketplace_id']), product_data['product_id'],
                product_data['title'], product_data['description'], product_data['brand'],
                product_data['seller_id'], product_data['seller_name'], product_data['first_image_url'],
                product_data['category_id'], product_data['category_lvl_1'], product_data['category_lvl_2'],
                product_data['category_lvl_3'], product_data['category_remaining'],
                json.dumps(product_data['features']),
                product_data['rating_count'], product_data['rating_value'], product_data['price_before_discounts'],
                product_data['discount'], product_data['price_after_discounts'], product_data['bonuses'],
                product_data['sales'], product_data['currency'], product_data['barcode'], product_data['similar_sku']
            )

    @override
    async def update_one(
            self,
            product_uuid,
            similar_uuids
    ) -> None:
        conn = await get_postgres_settings().get_async_postgres_connect()
        async with conn.transaction():
            await conn.execute('UPDATE public.sku SET similar_sku = $1 WHERE uuid = $2', similar_uuids, product_uuid)

    @override
    async def fetch_all(self):
        conn = await get_postgres_settings().get_async_postgres_connect()
        return await conn.fetch('SELECT uuid, title, description FROM public.sku')