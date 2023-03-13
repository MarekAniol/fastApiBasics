import uvicorn
from fastapi import FastAPI
from item_router import router


app = FastAPI()


app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "Word2"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)