from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
async def root():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return {"message": "Hello, Vercel! Connected to PostgreSQL!"}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Error connecting to PostgreSQL: {str(e)}"}
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))