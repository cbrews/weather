from typing import Any, Generator

import dotenv
import pytest
from fastapi.testclient import TestClient

from app.api import api
from app.db import drop_all, migrate


def pytest_configure(config: Any) -> None:
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


def pytest_sessionstart(session: Any) -> None:
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    dotenv.load_dotenv(".env-test")
    drop_all()
    migrate()


def pytest_sessionfinish(session: Any, exitstatus: Any) -> None:
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """


def pytest_unconfigure(config: Any) -> None:
    """
    called before test process is exited.
    """


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    yield TestClient(api)
