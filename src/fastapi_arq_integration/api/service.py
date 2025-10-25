from random import randint

from src.fastapi_arq_integration.api.models import Operation
from src.fastapi_arq_integration.api.repository import Repository
from src.fastapi_arq_integration.redis import redis


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def select_operation(self) -> Operation | None:
        product_id = randint(1, 1000)
        return await self.repository.select_operation(product_id)

    async def insert_operation(self, description: str) -> None:
        await redis.redis_pool.enqueue_job(
            "insert_operation",
            description,
        )
