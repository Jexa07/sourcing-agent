from core.job_input import parse_job_description
from core.linkedin_scraper import google_search_linkedin
from core.profile_parser import extract_profile_data
from core.score_calculator import score_candidates
from core.message_generator import generate_outreach_messages
from core.exporter import export_to_csv, export_to_html
from utils.logger import log
import json
import os

OUTPUT_PATH_JSON = os.path.join("data", "outputs.json")
OUTPUT_PATH_CSV = os.path.join("data", "outputs.csv")
OUTPUT_PATH_HTML = os.path.join("data", "outputs.html")

if __name__ == "__main__":
    log("🚀 Parsing job description...")
    with open("data/job.txt", "r", encoding="utf-8") as f:
        job_text = f.read()

    job_description = parse_job_description(job_text)

    log("📄 Extracted Context:")
    print(job_description)

    log("🔍 Searching for real candidates...")
    query = f'site:linkedin.com/in "ML Engineer" "LLM" "{job_description["location"]}"'
    raw_candidates = google_search_linkedin(query)

    log("👓 Extracting profile data...")
    parsed_candidates = extract_profile_data(raw_candidates)

    log("📊 Scoring candidates...")
    scored_candidates = score_candidates(parsed_candidates, job_description)

    log("💌 Generating outreach messages...")
    top_candidates = [
        {
            **candidate,
            "outreach_message": generate_outreach_messages([candidate], job_description)[0]
        }
        for candidate in scored_candidates[:10]
    ]

    log("📁 Saving final results to outputs.json...")
    with open(OUTPUT_PATH_JSON, "w", encoding="utf-8") as f:
        json.dump(top_candidates, f, indent=4)

    log("🧾 Exporting to CSV & HTML...")
    export_to_csv(top_candidates, OUTPUT_PATH_CSV)
    export_to_html(top_candidates, OUTPUT_PATH_HTML)

    log("✅ Done! Check data/outputs.json, outputs.csv, and outputs.html")