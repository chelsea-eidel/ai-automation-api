# AI Automation API

## Overview
A FastAPI-based service that uses LLMs to convert unstructured text into actionable and structured outputs.

## Features
- Summarization
- Task extraction
- Structured JSON extraction

## Tech Stack
- Python
- FastAPI
- Pydantic
- OpenAI API
- Docker
- pytest

## Architecture

```
Client
  ↓
FastAPI API
  ↓
LLM Service
  ↓
OpenAI API
```

## Example Use Cases
- Extract school reminders into tasks
- Summarize long notes or emails
- Convert messy text into structured JSON

## Running Locally

```bash
pip install -r requirements.txt
cp .env.example .env  # add your OPENAI_API_KEY
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## Running with Docker

```bash
docker build -t ai-automation-api .
docker run -p 8000:8000 --env-file .env ai-automation-api
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |
| `OPENAI_MODEL` | No | Model to use (default: `gpt-4.1-mini`) |

## API Endpoints

### `GET /health`
Returns service health status.

**Response**
```json
{ "status": "ok" }
```

---

### `POST /summarize`
Summarizes a block of text.

**Request**
```json
{ "text": "Long article or note text here..." }
```

**Response**
```json
{ "summary": "A concise summary of the provided text." }
```

---

### `POST /extract/tasks`
Extracts actionable tasks from text.

**Request**
```json
{ "text": "Please submit the report by Friday and schedule a meeting with the team next Monday." }
```

**Response**
```json
{
  "tasks": [
    { "title": "Submit the report", "due_date": "Friday", "priority": null },
    { "title": "Schedule a meeting with the team", "due_date": "next Monday", "priority": null }
  ]
}
```

---

### `POST /extract/structured`
Converts text into a JSON structure matching a described schema.

**Request**
```json
{
  "text": "John Smith, age 34, software engineer at Acme Corp.",
  "schema_description": "An object with fields: name (string), age (number), job_title (string), company (string)"
}
```

**Response**
```json
{
  "data": {
    "name": "John Smith",
    "age": 34,
    "job_title": "Software Engineer",
    "company": "Acme Corp"
  }
}
```

## Running Tests

```bash
pytest
```

## Future Improvements
- Authentication
- Persistent storage
- Retry handling
- Background job queue
- GitHub Actions CI
