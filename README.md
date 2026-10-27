# Hello World API

A simple, production-ready FastAPI Hello World API built for the team.

## Features

- `GET /` — Returns a Hello World greeting
- `GET /hello/{name}` — Returns a personalized greeting
- `GET /health` — Health check endpoint
- `GET /team` — Special team greeting
- Auto-generated interactive docs via Swagger UI and ReDoc

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Run Locally

1. **Clone the repo and navigate to the project directory**

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server**
   ```bash
   python main.py
   ```
   Or with uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Visit the API**
   - API Root: [http://localhost:8000](http://localhost:8000)
   - Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Run with Docker

1. **Build the Docker image**
   ```bash
   docker build -t hello-world-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 hello-world-api
   ```

## API Endpoints

| Method | Endpoint        | Description                        |
|--------|-----------------|------------------------------------|
| GET    | `/`             | Hello World greeting               |
| GET    | `/hello/{name}` | Personalized greeting by name      |
| GET    | `/health`       | Health check                       |
| GET    | `/team`         | Special team greeting              |
| GET    | `/docs`         | Swagger UI interactive docs        |
| GET    | `/redoc`        | ReDoc API documentation            |

## Example Requests

```bash
# Hello World
curl http://localhost:8000/

# Personalized greeting
curl http://localhost:8000/hello/Alice

# Health check
curl http://localhost:8000/health

# Team greeting
curl http://localhost:8000/team
```

## Example Responses

**GET /**
```json
{
  "message": "Hello, World!",
  "timestamp": "2024-01-01T12:00:00.000000",
  "version": "1.0.0"
}
```

**GET /hello/Alice**
```json
{
  "message": "Hello, Alice! Welcome to our API.",
  "name": "Alice",
  "timestamp": "2024-01-01T12:00:00.000000",
  "version": "1.0.0"
}
```

**GET /health**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000000"
}
```
