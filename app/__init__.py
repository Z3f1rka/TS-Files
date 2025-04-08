from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import file_router
from app.core import settings


# TODO: настроить нормально CORS
def create_app() -> FastAPI:
    app = FastAPI(swagger_ui_parameters={"url": f"http://{settings.API_HOST}:{settings.API_PORT}{settings.PREFIX}/openapi.json"})
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(file_router)
    return app
