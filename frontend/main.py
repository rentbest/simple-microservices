from fastapi import FastAPI
import httpx
import time


app = FastAPI()
BACKEND_URL = "http://localhost:8000/users"


@app.get("/")
def read_root():
    return {"message": "Frontend is running!"}


@app.get("/users")
async def get_users():
    start_time = time.perf_counter()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BACKEND_URL)
        finish_time = time.perf_counter()
        print(f"time: {finish_time - start_time}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}
