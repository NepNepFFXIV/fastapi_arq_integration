from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.fastapi_arq_integration.database import postgres
from src.fastapi_arq_integration.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    await postgres.connect(
        settings.postgres.postgres_url,
        settings.postgres.min_connections,
        settings.postgres.max_connections,
    )
    yield
    await postgres.close()


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )

    return app


app = create_app()
