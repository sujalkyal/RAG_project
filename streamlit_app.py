import streamlit as st
import requests

st.title("RAG Hiring Assistant")

job_id = st.text_input("Job ID", "job_123")  # Now treated as string
candidate_ids_input = st.text_input("Candidate IDs (comma separated)", "candidate_1,candidate_2")
question = st.text_area("Ask your question")

if st.button("Submit"):
    candidate_ids = [cid.strip() for cid in candidate_ids_input.split(",")]

    payload = {
        "job_id": job_id,
        "candidate_ids": candidate_ids,
        "question": question
    }

    with st.spinner("Thinking..."):
        try:
            res = requests.post("http://localhost:8000/chat", json=payload)
            if res.status_code == 200:
                st.success(res.json().get("response", "No response"))
            else:
                st.error(f"Server error: {res.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
