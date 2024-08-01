from abc import ABC, abstractmethod
from typing import NoReturn


class PublicSkuPostgresRepositoryInterface(ABC):
    @abstractmethod
    async def add_one(
            self,
            product_data
    ) -> NoReturn:
        raise NotImplementedError("<get_one> method must be implemented!>")

    @abstractmethod
    async def update_one(
            self,
            similar_uuids,
            product_uuid
    ) -> NoReturn:
        raise NotImplementedError("<update_one> method must be implemented!")

    @abstractmethod
    async def fetch_all(self) -> NoReturn:
        raise NotImplementedError("<fetch_all> method must be implemented!")
