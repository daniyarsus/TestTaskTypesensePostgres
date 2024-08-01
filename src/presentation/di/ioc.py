from bindme import container

from src.domain.marketplace.interfaces import ImporterServiceInterface
from src.domain.marketplace.services import ImporterServiceImplement
from src.infrastructure.db.postgres.interfaces import PublicSkuPostgresRepositoryInterface
from src.infrastructure.db.postgres.repositories import PublicSkuPostgresRepositoryImplement
from src.infrastructure.searchers.typesense.interfaces import ProductsTypesenseRepositoryInterface
from src.infrastructure.searchers.typesense.repositories import ProductsTypeSenseRepositoryImplement


def setup_ioc(container: container) -> None:
    container.register(
        abstract_class=ImporterServiceInterface,
        concrete_class=ImporterServiceImplement
    )
    container.register(
        abstract_class=PublicSkuPostgresRepositoryInterface,
        concrete_class=PublicSkuPostgresRepositoryImplement
    )
    container.register(
        abstract_class=ProductsTypesenseRepositoryInterface,
        concrete_class=ProductsTypeSenseRepositoryImplement
    )
