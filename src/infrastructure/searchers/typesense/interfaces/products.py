from abc import ABC, abstractmethod
from typing import NoReturn


class ProductsTypesenseRepositoryInterface(ABC):
    @abstractmethod
    def create_schema(self) -> NoReturn:
        raise NotImplementedError("<create_schema> must be implemented!>")

    @abstractmethod
    async def add_product(self, product_data: dict) -> NoReturn:
        raise NotImplementedError("<add_product> must be implemented!")

    @abstractmethod
    async def search_similar(self, search_query) -> NoReturn:
        raise NotImplementedError("<search_similar> must be implemented!")
