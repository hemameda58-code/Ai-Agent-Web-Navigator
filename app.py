import os
import json
import requests
import asyncio
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__, template_folder="templates")

# ---------------- Gemini API ----------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

# ---------------- Default Prompt ----------------
CASUAL_PROMPT = """
You are a friendly, casual, and informative assistant. 
Answer user queries clearly and helpfully.
Do not attempt to answer questions that require current factual data; instead, indicate 'yes' so Google can be used.
"""

# ---------------- Gemini Query ----------------
async def generate_gemini_response(prompt: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            ).text.strip()
        )
    except Exception as e:
        print("Gemini API error:", e)
        return "Sorry, I couldn't generate a response."

# ---------------- Google Search ----------------
API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("CSE_ID")

async def search_google_api(query: str):
    results = []
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": API_KEY, "cx": CSE_ID, "q": query}
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        for item in data.get("items", []):
            results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })
    except Exception as e:
        print("Google API error:", e)
    return results

# ---------------- Hybrid Agent ----------------
async def web_navigator_agent(user_input: str):
    sources = []
    answer_source = "gemini"

    # Step 1: Gemini casual response
    answer = await generate_gemini_response(
        f"{CASUAL_PROMPT}\nUser: {user_input}\nAssistant:"
    )

    # Step 2: If Gemini says "yes", fetch Google and format answer
    if answer.lower() == "yes":
        sources = await search_google_api(user_input)
        if sources:
            answer_source = "google"
            chunk_size = 3
            summaries = []

            for i in range(0, len(sources), chunk_size):
                chunk = sources[i:i+chunk_size]
                chunk_text = "\n".join([
                    f"**Title:** {r['title']}\nSnippet: {r['snippet']}\nLink: {r['link']}"
                    for r in chunk
                ])
                chunk_prompt = f"""
The user asked: "{user_input}"

You are given a set of Google search results. 
Summarize them in a clear, concise, and friendly way. Highlight the titles and make it easy to read. 
Default: concise summary. Only detail if user asked for 'detailed'.

Google Search Results:
{chunk_text}
Assistant:"""
                summary = await generate_gemini_response(chunk_prompt)
                summaries.append(summary)

            answer = "\n\n".join(summaries)
        else:
            answer = "Sorry, I couldn't find relevant information."

    return {
        "query": user_input,
        "ai_answer": answer,
        "sources": sources,
        "answer_source": answer_source
    }

# ---------------- Flask Routes ----------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message")

    # Run async agent in Flask
    output = asyncio.run(web_navigator_agent(user_input))
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

