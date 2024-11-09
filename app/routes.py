from app.api import api


@api.get("/")
def root() -> dict[str, str]:
    return {"status": "ok"}
