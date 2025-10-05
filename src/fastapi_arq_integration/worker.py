from arq.connections import RedisSettings

from src.fastapi_arq_integration.settings import settings


async def run_job(ctx):
    print("run_job")


async def startup(ctx):
    print("startup")


async def shutdown(ctx):
    print("shutdown")


class WorkerSettings:
    functions = [run_job]
    redis_settings = RedisSettings(
        host=settings.redis.host,
        port=settings.redis.port,
        database=settings.redis.database,
    )
