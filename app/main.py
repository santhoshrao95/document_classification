from fastapi import FastAPI
from app.api.endpoints import pdf

app = FastAPI(title="Document Classification API")

app.include_router(pdf.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
