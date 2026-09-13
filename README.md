# Your Simple Finances (YSF)

A personal finance backend built with FastAPI. Currently in development.

## Status

**Early development.** The core transaction and user endpoints are functional, but the AI assistant endpoint is still in progress. Authentication, persistence, and the frontend are not implemented yet.

## What it does

YSF is a REST API that allows users to:

- Register financial transactions (income and expenses).
- Calculate totals (income, outcome, balance).
- Retrieve the transaction list.
- Get AI-powered financial advice (in progress).

The project follows a **YOAK (Your Own API Key)** model: users provide their own AI provider API key, so the app never pays for AI usage and users keep control of their credentials.

## Tech stack

- **Python 3.10+**
- **FastAPI** — web framework
- **Pydantic** — request/response validation
- **pandas** — data handling
- **Groq API** — LLM provider (for the AI assistant)
- **Uvicorn** — ASGI server

## Project structure
```
your-simple-finances/
├── Backend/
│   ├── AI_Client.py         # AI integration (Groq)
│   ├── financial_Info.py    # Financial data model and calculations
│   └── user_Info.py         # User model
├── main.py                  # FastAPI app and endpoints
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```


## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Polo404-not-found/your-simple-finances.git
cd your-simple-finances
```
### 2. Start a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. install dependencies & start the web server

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000.
Interactive docs (Swagger UI): http://127.0.0.1:8000/docs

### API Endpoints

Method	Endpoint	                Description	            Status
POST	/transactions/add	        Add a new transaction	[x]

GET	    /transactions/calculate	    Calculate totals	    [x]

GET	    /transactions/print	        List all transactions	[x]

POST	/user/info	                Save user info	        [x]

POST	/ia/ask	                    Ask the AI assistant	[] In progress

#### Example request
``` bash
curl -X POST http://127.0.0.1:8000/transactions/add \
  -H "Content-Type: application/json" \
  -d '{"type": "Income", "amount": 1500.0, "description": "Salary"}'
Example response
json
{
  "message": "Transaction added successfully",
  "transaction": ["Income", 1500.0, "Salary"]
}
```

## Architecture

The project is organized in layers:
API layer (main.py) — HTTP endpoints, request validation, error handling.
Domain layer (financial_Info.py, user_Info.py) — business logic and data models.
Integration layer (AI_Client.py) — external AI provider communication.
This separation keeps the code testable and makes it easy to swap components (e.g., change the AI provider without touching the domain logic).

## Known limitations

This is an early-stage project. The following issues are known and on the roadmap:
No authentication. Any client can call the API. Auth (JWT or session-based) is planned.
Shared global state. All users currently share the same in-memory data. Per-user sessions are planned.
No persistence. Data is lost when the server restarts. A database (SQLite → PostgreSQL) is planned.
No rate limiting. The API is vulnerable to abuse.
No tests. Test coverage with pytest is planned.
AI endpoint incomplete. The /ia/ask endpoint is not functional yet.

## Roadmap
```
[] Complete the AI assistant endpoint.
[] Implement per-user sessions (in-memory).
[] Add authentication (JWT).
[] Add persistence with SQLite.
[] Migrate to PostgreSQL.
[] Write unit and integration tests with pytest.
[] Add rate limiting.
[] Build the frontend.
[] Add Docker support.
```
## What I learned

Building YSF taught me:
Designing REST APIs with FastAPI.
Validating requests with Pydantic.
Separating concerns across layers (API, domain, integration).
The security implications of shared state and missing auth.
The YOAK model and how to design around user-provided credentials.
Why global state in a web server is a bad idea (concurrency, isolation, testing).

## About
This project is part of my learning journey as a backend developer. I'm a Systems Engineering student passionate about architecture, security, and clean code. Feedback is welcome.
