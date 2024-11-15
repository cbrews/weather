import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.db import session_fastapi_dependency as session
from app.exceptions import NotFound
from app.routes import get_routers
from app.settings import settings

logger = logging.getLogger(__name__)


# Handling for startup, shutdown
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    config = settings()
    logger.info(f"Starting FastAPI application {config.app}")
    yield


# App initialization
api = FastAPI(lifespan=lifespan, dependencies=[Depends(session)])

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in get_routers():
    api.include_router(router)


# Exception handlers
@api.exception_handler(NotFound)
def handle_not_found(request: Request, exc: NotFound) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"code": "NOT_FOUND", "object": exc.obj, "message": str(exc)},
    )


@api.exception_handler(Exception)
def handle_unknown_exception(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"code": "INTERNAL_SERVER_ERROR", "message": str(exc)},
    )
