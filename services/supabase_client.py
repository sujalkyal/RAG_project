# File: services/supabase_client.py
from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

async def get_resume_chunks(candidate_ids):
    results = []
    for cid in candidate_ids:
        data = supabase.table("candidate_embeddings").select("*").eq("candidate_id", cid).execute().data
        results.extend(data)
    return results

async def get_interview_chunks(candidate_ids):
    results = []
    for cid in candidate_ids:
        data = supabase.table("interview_embeddings").select("*").eq("candidate_id", cid).execute().data
        results.extend(data)
    return results

async def get_job_chunks(job_id):
    return supabase.table("job_embeddings").select("*").eq("job_id", job_id).execute().data
