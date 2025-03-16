from fastapi import FastAPI


app = FastAPI()

users = [
    {"id": 1, "name": "Rinat"},
    {"id": 2, "name": "Ranis"},
]


@app.get("/users")
async def get_users():
    return {"users": users}
