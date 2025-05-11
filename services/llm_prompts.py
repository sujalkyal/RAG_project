# File: services/llm_prompts.py
def build_prompt(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    return f"""Question: {question}\n\nAnswer the question based on the following context:\n{context}\nAnswer:"""
