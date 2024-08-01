import uvicorn
from bindme import container
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utilities import add_timer_middleware

from src.presentation.api.controllers import setup_controllers
from src.presentation.di import setup_ioc


def build_app() -> FastAPI:
    app = FastAPI(
        title="AgroBazar AUTH service Swagger UI",
        version="1.0.0"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    setup_ioc(container=container)
    setup_controllers(app=app)
    add_timer_middleware(app=app, show_avg=True)

    return app


if __name__ == "__main__":
    uvicorn.run(
        app="src.presentation.main:build_app",
        factory=True,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )
