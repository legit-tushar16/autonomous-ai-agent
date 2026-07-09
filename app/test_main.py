# app/test_main.py
from fastapi.testclient import TestClient
from main import app

# Initialize the test client
client = TestClient(app)

def test_agent_endpoint_validation():
    """Test that the API correctly rejects invalid JSON payloads."""
    # Sending missing 'request' field
    response = client.post("/agent", json={"wrong_key": "Draft a policy"})
    assert response.status_code == 422 # FastAPI Unprocessable Entity

def test_agent_endpoint_success():
    """
    Integration test for the autonomous agent. 
    Note: In a true CI/CD pipeline, we would mock the Gemini LLM client 
    here to prevent actual API calls and save credits.
    """
    payload = {
        "request": "Write a one-paragraph summary of the importance of unit testing."
    }
    response = client.post("/agent", json=payload)
    
    # Check if the API request was successful
    assert response.status_code == 200
    
    # Check if the response contains the expected keys
    data = response.json()
    assert data["status"] == "success"
    assert "generated_artifact" in data
    assert data["generated_artifact"].endswith(".docx")