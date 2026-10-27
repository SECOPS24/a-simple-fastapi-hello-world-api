from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI(
    title="Hello World API",
    description="A simple FastAPI Hello World API for the team",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GreetingResponse(BaseModel):
    message: str
    timestamp: str
    version: str


class PersonalGreetingResponse(BaseModel):
    message: str
    name: str
    timestamp: str
    version: str


class HealthResponse(BaseModel):
    status: str
    timestamp: str


@app.get("/", response_model=GreetingResponse, tags=["Greeting"])
def root():
    """Return a simple Hello World greeting."""
    return GreetingResponse(
        message="Hello, World!",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0"
    )


@app.get("/hello/{name}", response_model=PersonalGreetingResponse, tags=["Greeting"])
def greet_person(name: str):
    """Return a personalized greeting for the given name."""
    return PersonalGreetingResponse(
        message=f"Hello, {name}! Welcome to our API.",
        name=name,
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0"
    )


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    """Health check endpoint to verify the API is running."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat()
    )


@app.get("/team", tags=["Team"])
def team_greeting():
    """A special greeting for the team."""
    return {
        "message": "Hello, Team! Great to have you here.",
        "members": "Everyone is awesome!",
        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
