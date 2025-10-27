from typing import TypedDict

from src.fastapi_arq_integration.api.repository import Repository


class WorkerContext(TypedDict):
    repository: Repository
