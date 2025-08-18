import datetime
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Path
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Investment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    coin: str
    quantity: float
    buy: bool | None = Field(default=None)
    timestamp: datetime.datetime | None = Field(default=datetime.datetime.now())


engine = create_engine(
    "sqlite:///portfolio.db", echo=True, connect_args={"check_same_thread": False}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/api/portfolio")
async def get_investment(coin: Annotated[str, Path()]):
    with Session(engine) as session:
        investments = session.exec(select(Investment)).all()
    return investments

@app.get("/api/portfolio/{coin}")
async def get_investment(coin: Annotated[str, Path()]):
    with Session(engine) as session:
        investments = session.exec(select(Investment).where(Investment.coin == coin)).all()
    return investments

@app.post("/api/portfolio/new")
async def new_investment(investment: Investment):
    with Session(engine) as session:
        session.add(investment)
        session.commit()
        session.refresh(investment)
    return investment

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)