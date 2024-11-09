from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.db import session_fastapi_dependency as session
from app.exceptions import NotFound

api = FastAPI(dependencies=[Depends(session)])


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
