from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return {"message": "Hello, Render! Connected to PostgreSQL!"}
    except Exception as e:
        return {"message": f"Error connecting to PostgreSQL: {str(e)}"}