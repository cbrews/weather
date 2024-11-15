# Setup



## Environment

Setup your environment for local development
```
python -m tools.setup
```

Start database dependencies locally
```
docker compose up
```

## Python (API)

Start fastapi locally
```
python -m fastapi dev app
```

Run tests locally
```
python -m pytest tests/unit
python -m pytest tests/integration
```

Linters:
```
python -m black . && python -m ruff check . --fix && python -m mypy .
```

## Typescript (UI)

```
nvm use
yarn
yarn dev
```