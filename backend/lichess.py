import httpx
from fastapi import APIRouter, Path, Response
from typing import List
import csv

router = APIRouter()

@router.get("/get_top_players")
async def get_top_players():
    url = "https://lichess.org/api/player"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

@router.get("/get_rating_history/{username}", response_model=List[List[int]])
async def get_rating_history(username: str = Path(..., title="The username of the user")):
    url = f"https://lichess.org/api/user/{username}/rating-history"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@router.get("/players/rating-history-csv", response_class=Response)
async def get_top_players_rating_history_csv():
    top_players = await get_top_players()

    # Assuming top_players is a list of player usernames, modify as needed
    csv_data = []
    for username in top_players:
        rating_history = await get_rating_history(username)
        if rating_history:
            # Extract the relevant data, e.g., username, rating from 30 days ago, and subsequent ratings
            row = [username, rating_history[0][-1]] + [rating[-1] for rating in rating_history[1:]]
            csv_data.append(row)

    # Create the CSV file in-memory
    csv_content = "\n".join([",".join(map(str, row)) for row in csv_data])
    
    # Set appropriate headers for CSV file download
    response = Response(content=csv_content, media_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="rating_history.csv"'

    return response