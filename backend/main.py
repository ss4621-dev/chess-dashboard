from fastapi import FastAPI, Depends, HTTPException
from db import database, players
import lichess
from lichess import get_top_players, get_rating_history

app = FastAPI()

app.include_router(lichess.router, prefix="/lichess", tags=["lichess"])


@app.on_event("startup")
async def startup_db():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()

@app.get("/top-players")
async def top_players():
    return await get_top_players()

@app.get("/player/{usename}/rating-history")
async def player_rating_history(username: str):
    return await get_rating_history(username)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)