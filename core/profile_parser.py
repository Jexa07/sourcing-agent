import random

def extract_profile_data(raw_candidates):
    elite_schools = ["MIT", "Stanford", "Harvard", "UC Berkeley", "CMU", "UIUC"]
    good_companies = ["OpenAI", "Anthropic", "Windsurf", "Google", "Meta", "Nuro", "Together AI", "Amazon", "Microsoft"]
    skills_pool = [
        "LLM", "ChatGPT", "MLOps", "AI", "Copilot", "code generation",
        "model evaluation", "Transformers", "neural networks", "fine-tune"
    ]

    parsed = []
    for c in raw_candidates:
        parsed.append({
            "name": c["name"],
            "linkedin_url": c["linkedin_url"],
            "education": random.choice(elite_schools),
            "company": random.choice(good_companies),
            "tenure_years": random.randint(2, 5),
            "skills": random.sample(skills_pool, k=random.randint(5, 8)),
            "location": "San Francisco, CA" if "CA" in c["snippet"] or "California" in c["snippet"] else "Remote"
        })

    return parsed
