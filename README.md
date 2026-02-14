# FastAPI Bootstrap

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run

```bash
fastapi dev app/main.py
```

## Endpoints

- `GET /` returns a welcome message
- `GET /health` returns service status
- `GET /docs` opens the Swagger UI
