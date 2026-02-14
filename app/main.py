from fastapi import FastAPI

app = FastAPI(title="python_learn API", version="0.1.0")


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {"message": "Welcome to FastAPI"}

