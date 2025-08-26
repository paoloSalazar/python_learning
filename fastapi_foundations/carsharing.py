from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    """Welcome message for the Carsharing service."""
    return {"message": "Welcome to Carsharing Service!"}

