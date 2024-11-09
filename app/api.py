from fastapi import Depends, FastAPI

from app.db import session_fastapi_dependency as session

api = FastAPI(dependencies=[Depends(session)])
