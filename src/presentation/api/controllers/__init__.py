from fastapi import FastAPI

from .marketplace import ImporterController
from src.domain.marketplace.interfaces import ImporterServiceInterface

__all__ = ['setup_controllers']


def setup_controllers(app: FastAPI) -> None:
    app.include_router(
        router=ImporterController(
            importer_service=ImporterServiceInterface
        ).router
    )
