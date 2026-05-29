import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Pointing to your LM studio exactly as requested
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

SYSTEM_PROMPT = """
You are the Focus-Lock Core Engine. Analyze the software interaction telemetry vector and output a strict JSON response.

Expected Input format: "Switches: X, Typing Jitter: Y, Error Rate: Z"

Return EXACTLY this JSON structure and nothing else:
{
  "fatigue_tier": "Low / Moderate / Critical Burst",
  "primary_cognitive_risk": "Short phase sentence summarizing the behavior (e.g., Executive Dysfunction Loop)",
  "remediation_payload": "A 1-sentence micro-cooldown directive written in a sharp, authoritative, yet supportive tone.",
  "lockdown_steps": [
    "Step 1: Immediate action (e.g., Close active IDE)",
    "Step 2: Micro physiological adjustment",
    "Step 3: Reset metric parameter"
  ]
}
"""

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# THIS IS THE ROUTE THAT WAS MISSING (404)
@app.post("/api/analyze")
async def analyze_telemetry(data: dict):
    telemetry_stream = data.get("telemetry", "")
    try:
        response = client.chat.completions.create(
            model="gemma-4-local",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": telemetry_stream}
            ],
            temperature=0.2,
        )
        return {"result": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))