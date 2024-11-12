from dotenv import load_dotenv
from typer import Exit, Typer, echo, style

from app.db import migrate
from app.models import *  # noqa: F403
from tools.env import Env

cli = Typer()


@cli.command()
def setup() -> None:
    echo("Generating .env file for local environments...")
    env = Env()
    try:
        env.generate_dotenv("local", ".env")
        env.generate_dotenv("test-local", ".env-test")
    except ValueError as e:
        echo(style(e, bold=True))
        raise Exit()

    echo("Loading local test environment...")
    load_dotenv(".env")

    echo("Migrating database...")
    migrate()

    echo(
        style(
            "Make sure you re-run this whenever you edit the env.yaml file!", bold=True
        )
    )


if __name__ == "__main__":
    cli()
