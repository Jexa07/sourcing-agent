import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Sourcing Agent", layout="wide")
st.markdown("""
    <style>
        .css-1v3fvcr {
            background-color: #0e1117;
        }
        .css-18ni7ap {
            background-color: #0e1117;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Synapse AI Hackathon – Sourcing Agent")
st.caption("Built by Arpita")

st.subheader("🔍 Top 10 Candidates")

# Load data from JSON
with open("data/outputs.json", "r") as f:
    candidates = json.load(f)

# Convert to DataFrame for table view
df = pd.DataFrame(candidates)

# Display clickable links using HTML rendering
df["linkedin_url"] = df["linkedin_url"].apply(lambda url: f"<a href='{url}' target='_blank'>Profile</a>")

# Apply conditional formatting to fit_score column
def highlight_scores(val):
    try:
        return f"background-color: {'#00b894' if float(val) >= 9.0 else '#2d3436'}"
    except:
        return ""

styled_df = df[["name", "linkedin_url", "company", "fit_score"]].style.applymap(highlight_scores, subset=["fit_score"]).format({"linkedin_url": lambda x: x})

st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)
st.caption("⚠️ Company info may be outdated — based on public search results, not live LinkedIn profiles.")

# Select candidate for detailed view
st.markdown("---")
st.subheader("🧑‍💼 Choose a candidate to view details")

names = [candidate["name"] for candidate in candidates]
selected_name = st.selectbox("Candidate Name", names)

selected_candidate = next(c for c in candidates if c["name"] == selected_name)

st.markdown(f"**Company:** {selected_candidate['company']}")
st.markdown(f"**LinkedIn:** <a href='{selected_candidate['linkedin_url']}' target='_blank'>Profile</a>", unsafe_allow_html=True)
st.markdown(f"**Fit Score:** {selected_candidate['fit_score']}")
st.markdown("**Score Breakdown:**")
st.json(selected_candidate["score_breakdown"])

st.markdown("**Outreach Message:**")
st.info(selected_candidate["outreach_message"])

st.markdown("---")
st.caption("© 2025 Arpita Pani – All rights reserved")