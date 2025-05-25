from time import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette import status


api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change to frontend URL if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


@api.get(path="/", description="Index.")
def root() -> dict[str, str]:
    return {
        "msg": "Hello! From FastAPI example."
    }

@api.get(path="/health", description="API Healthcheck.")
def healtcheck() -> dict:
    return {
        "status": "OK",
        "code": status.HTTP_200_OK
    }

@api.get(path="/time", description="Gives start cache time for test.")
def get_caching_time() -> dict:
    return {"time": time()}
