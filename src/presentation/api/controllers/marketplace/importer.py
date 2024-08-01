from bindme import inject
from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse

from src.domain.marketplace.interfaces import ImporterServiceInterface


class ImporterController:
    @inject
    def __init__(
            self,
            importer_service: ImporterServiceInterface
    ) -> None:
        self.router = APIRouter(prefix="/api/v1/marketplace/importer")
        self._importer_service = importer_service
        self._routes()

    def _routes(self):
        @self.router.post("/process")
        async def process_data_endpoint(request: UploadFile = File(...)) -> JSONResponse:
            await self._importer_service.process_data(dto=request)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "good!!!"}
            )
