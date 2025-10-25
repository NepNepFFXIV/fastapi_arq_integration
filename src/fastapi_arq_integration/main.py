from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.fastapi_arq_integration.database import postgres
from src.fastapi_arq_integration.redis import redis
from src.fastapi_arq_integration.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    await postgres.connect(
        settings.postgres.postgres_url,
        settings.postgres.min_connections,
        settings.postgres.max_connections,
    )
    await redis.connect(
        settings.redis.host,
        settings.redis.port,
        settings.redis.database,
    )
    yield
    await redis.close()
    await postgres.close()


def create_app() -> FastAPI:
    from src.fastapi_arq_integration.api.router import router

    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )

    app.include_router(router)

    return app


app = create_app()
