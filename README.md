# Sourcing Agent 🔍

Welcome to **Arpita's Autonomous Sourcing Agent** – a powerful, fast, and Gen Z-friendly tool that searches, scores, and connects ML talent with top-tier opportunities.

> ⚙️ Powered by Python + Streamlit + SerpAPI
> 🔗 Live Demo: [https://youtu.be/YDY5Q3Fs8PY]
> 🧑‍💼 Job Role: ML Research Engineer @ Windsurf (Codeium)

---

## 🚀 Features

✅ **Job-Aware Search**

> Parses a detailed JD and crafts smart Google Search queries to find real LinkedIn profiles.

✅ **Fit Scoring Algorithm**

> Calculates fit scores (1–10) based on:
> `Education`, `Career Trajectory`, `Company`, `Skills`, `Location`, and `Tenure`.

✅ **AI-Powered Outreach Generator**

> GPT-driven, personalized LinkedIn messages tailored to each candidate's strengths.

✅ **Interactive Streamlit UI**

> Clean, wide-screen view to explore top candidates, view breakdowns, and copy messages instantly.

✅ **Export to CSV + HTML**

> Neat outputs for recruiters to share, store, and analyze.

---

## 📸 Demo Video (Loom) – *Coming Soon*

You'll see:

* 📥 A job description being parsed
* 🔗 LinkedIn profiles discovered
* 📊 Fit scores calculated
* 💌 Outreach messages generated
* 🖥️ Streamlit app in action!

---

## 🧪 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/Jexa07/sourcing-agent.git
cd sourcing-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a `.env` file in the root folder:

```
SERPAPI_KEY=your-serpapi-key-here
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```bash
.
├── app.py                # Streamlit frontend
├── main.py               # End-to-end pipeline script
├── core/                 # Logic modules: scraping, scoring, parsing
├── utils/                # Logger, helpers
├── data/                 # Inputs & outputs
├── .env                  # Your API key (not committed)
├── requirements.txt      # Dependencies
└── README.md             # This file ❤️
```

---

## 📊 Sample Output

```json
{
  "name": "Jane Smith",
  "linkedin_url": "https://linkedin.com/in/janesmith",
  "company": "OpenAI",
  "fit_score": 9.2,
  "score_breakdown": {
    "education": 9.5,
    "trajectory": 9.0,
    "company": 9.0,
    "skills": 10.0,
    "location": 8.0,
    "tenure": 9.0
  },
  "outreach_message": "Hi Jane, I came across your profile..."
}
```

---

## 💡 Bonus Ideas (Planned)

* [ ] Confidence Scoring when data is incomplete
* [ ] GitHub/Twitter enhancement for deeper signals
* [ ] FastAPI endpoint for submission API
* [ ] Batch job support (10+ jobs)

---

## 👋 About Me

Hey! I'm **Arpita Pani**, a CSE student with a passion for intelligent systems and sleek UX.
This project was an absolute thrill to build — reach out if you'd like to connect!

🔗 [LinkedIn](https://www.linkedin.com/in/arpita-pani) | 🐙 [GitHub](https://github.com/Jexa07)

---

## 📜 License

MIT License – free to use, remix, and level up the future of sourcing.
