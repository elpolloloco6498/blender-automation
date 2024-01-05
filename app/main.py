from fastapi import FastAPI
from routers import generation

app = FastAPI()
app.include_router(generation.router)


@app.get("/")
async def version():
    return {"version": "0.0.1"}
