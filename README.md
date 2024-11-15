# Setup

## Docker

Start database dependencies locally
```
docker compose up
```

Also make sure you add this to your hosts file:
```
127.0.0.1 weather.local
```

## Python (API)

Setup your environment for local development
```
python -m tools.setup
python -m tools.seed-us-cities
```

Start fastapi locally
```
./tool/start.sh
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
yarn dev --host
```