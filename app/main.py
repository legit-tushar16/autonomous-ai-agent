import uvicorn
from fastapi import FastAPI, HTTPException
# 1. ADD THIS IMPORT
from google.genai.errors import ClientError 

# Sibling imports 
from schemas import AgentRequest
from agent import AutonomousAgent

app = FastAPI(
    title="Autonomous Multi-Agent Document Generation Service",
    description="Production-ready asynchronous orchestration layer using the Gemini API."
)

agent = AutonomousAgent()

@app.post("/agent")
async def run_agent(payload: AgentRequest):
    # Validation
    if not payload.request or not payload.request.strip():
        raise HTTPException(status_code=422, detail="Input 'request' field cannot be empty.")
    if len(payload.request.strip()) < 10:
        raise HTTPException(status_code=422, detail="Request is too short. (min 10 characters).")

    try:
        tasks_completed, document_file_path = await agent.execute(payload.request)
        return {
            "status": "success",
            "message": "Business document compiled successfully.",
            "tasks_executed": tasks_completed,
            "generated_artifact": document_file_path
        }
    
    
    except ClientError as e:
        # Check if the error string contains the 429 code
        error_msg = str(e)
        if "429" in error_msg:
            raise HTTPException(
                status_code=429, 
                detail="API rate limit exceeded. Please wait a moment and retry."
            )
        # If it's a different ClientError, raise it as a 500
        raise HTTPException(status_code=500, detail=f"Gemini API Client Error: {error_msg}")

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"System orchestration exception: {str(e)}")
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)