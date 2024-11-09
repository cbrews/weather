import yaml
from typer import Exit, Typer, echo, style

cli = Typer()


@cli.command()
def generate_env(env: str) -> None:
    """
    Quick utility to generate .env from env.yaml file
    """
    with open("env.yaml") as env_yaml:
        env_data = yaml.safe_load(env_yaml)
        env_block = env_data.get(env, None)

        if env_block is None:
            echo(style(f'No environment block found for "{env}"', bold=True))
            echo(f"Use one of: {', '.join(env_data.keys())}")
            raise Exit()

        with open(".env", "w", encoding="utf-8") as fd:
            fd.writelines([f"{key}={value}\n" for key, value in env_block.items()])


if __name__ == "__main__":
    cli()
