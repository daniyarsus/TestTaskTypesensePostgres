from typing import override, NoReturn

from bindme import inject

from src.domain.marketplace.interfaces import ImporterServiceInterface
from src.domain.marketplace.usecases import ProcessDataUseCase
from src.infrastructure.db.postgres.interfaces import PublicSkuPostgresRepositoryInterface
from src.infrastructure.searchers.typesense.interfaces import ProductsTypesenseRepositoryInterface


class ImporterServiceImplement(ImporterServiceInterface):
    @inject
    def __init__(
            self,
            public_sku_postgres_repo: PublicSkuPostgresRepositoryInterface,
            products_typesense_repo: ProductsTypesenseRepositoryInterface,
    ) -> None:
        self._public_sku_postgres_repo = public_sku_postgres_repo
        self._products_typesense_repo = products_typesense_repo

    @override
    async def process_data(self, dto) -> dict:
        use_case = ProcessDataUseCase(
            public_sku_postgres_repo=self._public_sku_postgres_repo,
            products_typesense_repo=self._products_typesense_repo
        )
        return await use_case(
            file=dto
        )
