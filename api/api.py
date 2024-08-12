from fastapi import FastAPI
from routers import health_check
from routers import root
from routers import predict

app = FastAPI()

app.include_router(health_check.router)
app.include_router(root.router)
app.include_router(predict.router)