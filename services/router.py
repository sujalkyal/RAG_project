# File: services/router.py
from services.supabase_client import get_resume_chunks, get_job_chunks, get_interview_chunks
from services.embedding_utils import get_top_k_chunks
from services.llm_prompts import build_prompt
from services.llm_inference import call_llm
from models.schema import ChatRequest
from services.intent_classifier import classify_context

async def route_question(request: ChatRequest) -> str:
    # Step 1: Classify the intent if not provided
    context_type = request.context_type or classify_context(request.question)

    # Step 2: Fetch documents based on context
    if context_type == "resume":
        chunks = await get_resume_chunks(request.candidate_ids)
    elif context_type == "interview":
        chunks = await get_interview_chunks(request.candidate_ids)
    elif context_type == "job":
        chunks = await get_job_chunks(request.job_id)
    elif context_type == "compare":
        chunks = await get_resume_chunks(request.candidate_ids)
    else:
        return "Sorry, I couldn't understand the type of your question."

    # Step 3: Find top relevant chunks
    # print(f"Context type: {context_type}")
    # print(f"Number of chunks: {len(chunks)}")
    # print(f"Chunks: {chunks}")
    # if not chunks:
    #     return "No relevant information found."
    
    #top_chunks = get_top_k_chunks(request.question, chunks)

    # Step 4: Construct final prompt
    prompt = build_prompt(request.question, chunks)

    # Step 5: Call LLM
    return call_llm(prompt)
