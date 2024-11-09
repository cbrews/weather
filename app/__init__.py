from dotenv import load_dotenv

from app.api import api
from app.db import migrate
from app.models import *  # noqa: F403
from app.routes import load_routes

load_dotenv(".env")
migrate()
load_routes()

__all__ = ["api"]
