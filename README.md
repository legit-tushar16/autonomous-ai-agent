# Autonomous AI Agent Pipeline

This repository contains my submission for the Python AI Engineer challenge. It is a fully asynchronous, self-correcting agentic pipeline built with FastAPI and the Gemini 3.1 Flash-Lite model.

## Features & Architecture
* **Autonomous Planning:** Uses strict Pydantic schemas to dynamically generate execution tasks based on the prompt.
* **Concurrent Execution:** Utilizes `asyncio.gather` for parallel processing, throttled by a semaphore to respect API rate limits.
* **Reflection & Self-Correction (Actor-Critic):** Evaluates its own drafts against formatting guardrails and forces a rewrite if hallucinations or errors are detected.
* **Dynamic Compilation:** Compiles approved sections into a clean `.docx` file using modern `pathlib` for absolute pathing.

## Setup Instructions

1. **Clone the repository:**
   git clone https://github.com/legit-tushar16/autonomous-ai-agent.git
   cd autonomous-ai-agent

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Set your environment variable:**
   export GEMINI_API_KEY="your_api_key_here"

4. **Run the server:**
   cd app
   python -m uvicorn main:app --reload

5. **Execute via Swagger UI:**
   Navigate to `http://127.0.0.1:8000/docs` to test the `/agent` endpoint.

## Testing
To run the included test suite for endpoint validation:
pytest test_main.py -v