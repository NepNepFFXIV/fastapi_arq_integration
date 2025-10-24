from arq import create_pool
from arq.connections import ArqRedis, RedisSettings


class Redis:
    __slots__ = ("_pool",)

    def __init__(self) -> None:
        self._pool: ArqRedis | None = None

    async def connect(self, host: str, port: int, database: int) -> None:
        if self._pool is not None:
            raise RuntimeError("Redis is already connected")

        self._pool = await create_pool(
            RedisSettings(
                host=host,
                port=port,
                database=database,
            )
        )

    async def close(self) -> None:
        if self._pool is None:
            raise RuntimeError("Redis is not connected")

        await self._pool.aclose()
        self._pool = None

    @property
    def redis_pool(self) -> ArqRedis:
        if self._pool is None:
            raise RuntimeError("Redis is not connected")
        return self._pool
