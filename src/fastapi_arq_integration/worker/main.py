from arq.connections import RedisSettings

from src.fastapi_arq_integration.database import postgres
from src.fastapi_arq_integration.settings import settings

from .functions import function_a, function_b


async def startup(ctx):
    await postgres.connect(
        settings.postgres.postgres_url,
        settings.postgres.min_connections,
        settings.postgres.max_connections,
    )


async def shutdown(ctx):
    await postgres.close()


class WorkerSettings:
    functions = [function_a, function_b]
    redis_settings = RedisSettings(
        host=settings.redis.host,
        port=settings.redis.port,
        database=settings.redis.database,
    )
