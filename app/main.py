import uvicorn
from fastapi import FastAPI, HTTPException

# Sibling imports (No "app." prefix) to support running directly inside the app folder
from schemas import AgentRequest
from agent import AutonomousAgent

app = FastAPI(
    title="Autonomous Multi-Agent Document Generation Service",
    description="Production-ready asynchronous orchestration layer using the Gemini API."
)

# Instantiate the agent core
agent = AutonomousAgent()

@app.post("/agent")
async def run_agent(payload: AgentRequest):
    """
    Accepts a natural language business request, dynamically maps out an execution plan,
    runs the generation tasks in parallel with safe rate limiting, runs a critique check,
    and returns a structured status along with a compiled Word Document file path.
    """
    # Validation: Ensure the request is not empty or just whitespace
    if not payload.request or not payload.request.strip():
        raise HTTPException(status_code=422, detail="Input 'request' field cannot be empty.")
    if not payload.request or len(payload.request.strip()) < 10:
        raise HTTPException(status_code=422, detail="Request is too short. Please provide a descriptive business request (min 10 characters).")

    try:
        # payload.request maps explicitly to the core JSON requirement {"request": "..."}
        tasks_completed, document_file_path = await agent.execute(payload.request)
        
        return {
            "status": "success",
            "message": "Business document compiled successfully.",
            "tasks_executed": tasks_completed,
            "generated_artifact": document_file_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"System orchestration exception: {str(e)}")

if __name__ == "__main__":
    # Standard string module reference for Uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)