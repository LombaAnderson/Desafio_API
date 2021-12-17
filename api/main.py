from fastapi import FastAPI

from .routers import numbers

app = FastAPI(
    title="Challenge Cross Commerce",
    description="Made By:",
    version="0.0.1",
    contact={"name": "Anderson Lomba", "email": "andersonlomba@gmail.com"},
)

app.include_router(numbers.router)
