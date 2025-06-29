import csv
from bs4 import BeautifulSoup

def export_to_csv(candidates, path):
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "linkedin_url", "company", "fit_score", "score_breakdown", "outreach_message"])
        writer.writeheader()
        for candidate in candidates:
            writer.writerow({
                "name": candidate["name"],
                "linkedin_url": candidate["linkedin_url"],
                "company": candidate["company"],
                "fit_score": candidate["fit_score"],
                "score_breakdown": candidate["score_breakdown"],
                "outreach_message": candidate["outreach_message"]
            })

def export_to_html(candidates, path):
    html = "<html><head><style>table, th, td {border: 1px solid black; border-collapse: collapse; padding: 8px;}</style></head><body>"
    html += "<h2>Top Candidates</h2><table><tr><th>Name</th><th>LinkedIn</th><th>Company</th><th>Score</th><th>Breakdown</th><th>Message</th></tr>"

    for c in candidates:
        html += f"<tr><td>{c['name']}</td>"
        html += f"<td><a href='{c['linkedin_url']}' target='_blank'>Profile</a></td>"
        html += f"<td>{c['company']}</td>"
        html += f"<td>{c['fit_score']}</td>"
        html += f"<td>{c['score_breakdown']}</td>"
        html += f"<td>{c['outreach_message'].replace(chr(10), '<br>')}</td></tr>"

    html += "</table></body></html>"

    # Prettify
    soup = BeautifulSoup(html, "html.parser")
    pretty_html = soup.prettify()

    with open(path, "w", encoding="utf-8") as f:
        f.write(pretty_html)