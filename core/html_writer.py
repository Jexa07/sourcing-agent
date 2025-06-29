# core/html_writer.py

def generate_prettified_html(candidates):
    html = """<html>
  <head>
    <style>
      table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        padding: 8px;
      }
    </style>
  </head>
  <body>
    <h2>Top Candidates</h2>
    <table>
      <tr>
        <th>Name</th>
        <th>LinkedIn</th>
        <th>Company</th>
        <th>Score</th>
        <th>Breakdown</th>
        <th>Message</th>
      </tr>
"""
    for candidate in candidates:
        html += f"""      <tr>
        <td>{candidate['name']}</td>
        <td><a href='{candidate['linkedin_url']}' target='_blank'>Profile</a></td>
        <td>{candidate['company']}</td>
        <td>{candidate['fit_score']}</td>
        <td>{candidate['score_breakdown']}</td>
        <td>{candidate['outreach_message'].replace('\n', '<br>')}</td>
      </tr>
"""
    html += """    </table>
  </body>
</html>
"""
    return html