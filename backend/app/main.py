from fastapi import FastAPI

app = FastAPI(
    title="The Fifth Flavor API",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "The Fifth Flavor API",
    }
