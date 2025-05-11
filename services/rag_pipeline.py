import httpx
from services.supabase_client import fetch_resume_embeddings, fetch_job_embedding
from services.llm_prompts import build_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3-chatqa:8b"

async def call_llm(prompt):
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", OLLAMA_URL, json={"model": MODEL, "prompt": prompt}) as response:
            text = ""
            async for chunk in response.aiter_lines():
                if chunk.strip():
                    partial = eval(chunk.strip())
                    text += partial.get("response", "")
            return text

async def handle_query(query, job_id, candidate_ids):
    resumes = fetch_resume_embeddings(candidate_ids)
    job = fetch_job_embedding(job_id)
    prompt = build_prompt(query, resumes, job["content"])
    return await call_llm(prompt)
