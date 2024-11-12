import yaml


class Env:
    input_file: str

    def __init__(self, input_file: str = "env.yaml"):
        self.input_file = input_file
        self.env_data = {}

    def generate_dotenv(self, env: str, env_file: str = ".env") -> None:
        with open("env.yaml") as env_yaml:
            env_data = yaml.safe_load(env_yaml)

        env_block = env_data.get(env, None)

        if env_block is None:
            raise ValueError(
                f"No environment block found for \"{env}\". Use one of {', '.join(env_data.keys())}"
            )

        with open(env_file, "w", encoding="utf-8") as fd:
            fd.writelines([f"{key}={value}\n" for key, value in env_block.items()])
