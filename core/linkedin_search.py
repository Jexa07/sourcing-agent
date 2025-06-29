def search_candidates(job_description):
    print("🔎 Simulating LinkedIn search...")

    return [
        {
            "name": "Alice Zhang",
            "linkedin_url": "https://linkedin.com/in/alice-zhang",
            "education": "Stanford",
            "tenure_years": 3,
            "company": "OpenAI",  # ✅ ADD THIS
            "location": "Mountain View, CA",
            "skills": ["LLM", "ML", "Transformers", "MLOps", "AI", "ChatGPT", "Copilot", "code generation", "model evaluation"]
        },
        {
            "name": "Ben Carter",
            "linkedin_url": "https://linkedin.com/in/ben-carter",
            "education": "MIT",
            "tenure_years": 2,
            "company": "Anthropic",  # ✅ ADD THIS
            "location": "San Francisco, CA",
            "skills": ["ML", "AI", "LLM", "TensorFlow", "Copilot", "MLOps", "Transformers"]
        }
    ]
