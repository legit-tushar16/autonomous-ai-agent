# 🤖 Autonomous AI Agent Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini_3.1_Flash-8E75B2.svg?logo=googlebard&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An asynchronous, self-correcting agentic pipeline designed to plan, execute, audit, and compile professional enterprise documents autonomously.

---

## ✨ Key Features

* **🧠 Autonomous Planning:** Utilizes strict Pydantic schemas to dynamically generate multi-step execution tasks based on ambiguous user prompts.
* **⚡ Concurrent Execution:** Implements `asyncio.gather` for parallel processing, strictly throttled by a semaphore to respect API rate limits.
* **🛡️ Reflection & Self-Correction:** Employs an Actor-Critic pattern to evaluate its own drafts against formatting guardrails, forcing rewrites if hallucinations or errors are detected.
* **📂 Dynamic Compilation:** Merges approved sections into a clean `.docx` file using modern `pathlib` for bulletproof absolute pathing.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[User Request] --> B[FastAPI Endpoint]
    B --> C{Phase 1: Planning}
    C -->|Pydantic Schema| D[Task List Generated]
    
    D --> E(Phase 2: Concurrent Execution)
    E -->|asyncio.gather| F[Draft Section 1]
    E -->|asyncio.gather| G[Draft Section 2]
    
    F --> H{Phase 3: Reflection Loop}
    G --> H
    
    H -->|Failed QA| E
    H -->|Passed QA| I(Phase 4: Compilation)
    
    I --> J[python-docx Output]
    J --> K[Final .docx File]