from fastapi import FastAPI
from routers import item_router


app = FastAPI()


app.include_router(item_router.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "Word2"}
