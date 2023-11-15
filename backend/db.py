from sqlalchemy import create_engine, Column, Integer, String, Date, MetaData, Table
from databases import Database
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData()

players = Table(
    "players",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, index=True),
    Column("rating", Integer),
    Column("rating_date", Date),
)

database = Database(DATABASE_URL)
