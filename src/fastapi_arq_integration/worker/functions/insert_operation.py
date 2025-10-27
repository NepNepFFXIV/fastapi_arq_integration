from src.fastapi_arq_integration.worker.worker_context import WorkerContext


async def insert_operation(ctx: WorkerContext, description: str):
    repository = ctx["repository"]
    await repository.insert_operation(description)
