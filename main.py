import contextlib
from typing import AsyncIterator

import uvicorn
from fastapi import FastAPI

import orm
from api import user
from app.settings import settings


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    orm.db_manager.init(settings.database_url)
    yield
    await orm.db_manager.close()


app = FastAPI(title="Very simple example", lifespan=lifespan)
app.include_router(user.router, prefix="/api/users", tags=["users"])

if __name__ == "__main__":
    # There are a lot of parameters for uvicorn, you should check the docs
    uvicorn.run(
        app,
        host=settings.app_host,
        port=settings.app_port,
    )
