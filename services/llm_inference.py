# File: services/llm_inference.py
import requests

def call_llm(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3-chatqa:8b",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload, timeout=60)
    return response.json()["response"]
