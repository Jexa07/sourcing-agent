import re

def parse_job_description(job_text):
    # Define key skill-related patterns to look for
    skills_keywords = [
        "LLM", "large language model", "PyTorch", "TensorFlow", "ML", "MLOps",
        "Transformers", "Copilot", "ChatGPT", "AI", "code generation", 
        "fine-tune", "neural networks", "model evaluation"
    ]

    parsed = {
        "location": None,
        "skills": [],
        "company": None,
        "title": None
    }

    # Extract location
    loc_match = re.search(r"(Mountain View|San Francisco|CA|remote)", job_text, re.IGNORECASE)
    parsed["location"] = loc_match.group(0) if loc_match else None

    # Extract skills
    found_skills = [skill for skill in skills_keywords if skill.lower() in job_text.lower()]
    parsed["skills"] = list(set(found_skills))

    # Extract title
    title_match = re.search(r"(Software Engineer, ML Research)", job_text)
    if title_match:
        parsed["title"] = title_match.group(0)

    # Extract company
    company_match = re.search(r"(Windsurf|Codeium)", job_text)
    if company_match:
        parsed["company"] = company_match.group(0)

    return parsed
