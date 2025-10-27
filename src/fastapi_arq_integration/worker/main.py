from arq.connections import RedisSettings

from src.fastapi_arq_integration.api.dependency import get_repository
from src.fastapi_arq_integration.database import postgres
from src.fastapi_arq_integration.settings import settings

from .functions import insert_operation


async def startup(ctx):
    await postgres.connect(
        settings.postgres.postgres_url,
        settings.postgres.min_connections,
        settings.postgres.max_connections,
    )
    repository = get_repository()
    ctx["repository"] = repository


async def shutdown(ctx):
    await postgres.close()


class WorkerSettings:
    functions = [insert_operation]
    redis_settings = RedisSettings(
        host=settings.redis.host,
        port=settings.redis.port,
        database=settings.redis.database,
    )
    on_startup = startup
    on_shutdown = shutdown
