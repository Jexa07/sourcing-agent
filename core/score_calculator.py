def score_candidate(candidate, jd_context):
    breakdown = {}
    weights = {
        "education": 0.2,
        "trajectory": 0.2,
        "company": 0.15,
        "skills": 0.25,
        "location": 0.1,
        "tenure": 0.1
    }

    # Education
    elite_schools = ["MIT", "Stanford", "Harvard", "UC Berkeley", "CMU", "UIUC"]
    education = candidate.get("education", "")
    breakdown["education"] = 9.5 if education in elite_schools else 6.0

    # Trajectory (based on tenure years)
    tenure_years = candidate.get("tenure_years", 0)
    breakdown["trajectory"] = (
        9.0 if tenure_years >= 3 else
        7.0 if tenure_years >= 2 else 4.0
    )

    # Company relevance
    good_companies = ["OpenAI", "Anthropic", "Windsurf", "Google", "Meta"]
    company = candidate.get("company", "")
    breakdown["company"] = 9.0 if company in good_companies else 6.0

    # Skills match — dynamic from JD!
    skills = candidate.get("skills", [])
    jd_skills = jd_context.get("skills", [])
    overlap = len(set(skills).intersection(set(jd_skills)))
    breakdown["skills"] = min(10.0, 5.0 + 1.5 * overlap)

    # Location match
    location = candidate.get("location", "")
    jd_location = jd_context.get("location", "")
    if jd_location in location:
        breakdown["location"] = 10.0
    elif "CA" in location:
        breakdown["location"] = 8.0
    else:
        breakdown["location"] = 6.0

    # Tenure
    breakdown["tenure"] = (
        9.0 if tenure_years >= 3 else
        7.0 if tenure_years >= 2 else 4.0
    )

    # Weighted final score
    fit_score = sum(breakdown[k] * weights[k] for k in breakdown)

    return {
        "name": candidate["name"],
        "linkedin_url": candidate["linkedin_url"],
        "fit_score": fit_score,
        "score_breakdown": breakdown,
        "company": company or "your company"
    }

def score_candidates(candidates, jd_context):
    return [score_candidate(c, jd_context) for c in candidates]