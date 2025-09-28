# 🌐 Web Navigator AI Agent

---

## 🧾 Problem Statement Reference

* **Problem Statement ID:** HACXPB002
* **Problem Statement Chosen:** Web Navigator AI Agent
* **Reason for Choosing:**
  We wanted to solve a real-world automation challenge where users can interact with the web using natural language. This problem allows us to combine AI (Gemini) with browser automation, making it a practical, impactful solution that demonstrates both innovation and usability.

---

## 💡 Solution Overview

* **Proposed Approach:**
  We built a Flask-based AI agent that takes natural language instructions, processes them using Google Gemini API, and if necessary performs real-time Google search to fetch relevant information, summarize it, and return structured results to the user.

* **Key Features / Modules:**

  * Natural language understanding using Gemini API
  * Conditional Google Search using Custom Search API
  * Intelligent summarization of search results
  * REST API endpoint (`/ask`) to receive queries and return responses
  * Simple web UI for user interaction
  * Live deployment on Render with uptime monitoring

---

## 🏗 System Architecture

* **Architecture Diagram / Workflow:**

```
User → Flask Backend → Gemini API
                      ↘ Google Custom Search (if needed)
                        ↘ Summarized Results → Response to User
```

* **Data Flow Explanation:**

1. User sends a message from frontend.
2. Backend sends the message to Gemini API for interpretation.
3. If Gemini indicates factual lookup is needed, Google Custom Search API is used.
4. Search results are summarized by Gemini and sent back to the frontend.

---

## 🛠 Technology Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript (template-based)
* **Database:** None (stateless application)
* **ML/AI Frameworks:** Google Gemini API (LLM for reasoning, summarization)
* **APIs / Libraries:**

  * Google Gemini (genai library)
  * Google Custom Search API
  * Requests (for API calls)
  * Asyncio (for async tasks)

---

## 🔢 Algorithms & Models

* **Algorithm(s) Chosen:**

  * Gemini-2.5-flash model for natural language understanding & summarization
* **Reason for Choice:**

  * Fast inference, good at summarization and reasoning
* **Model Training & Testing:**

  * No local training required; we rely on Gemini’s pretrained capability

---

## 📊 Data Handling

* **Data Sources Used:**

  * Google Custom Search API results
* **Preprocessing Methods:**

  * Summarization of search results into user-friendly format
* **Storage / Pipeline Setup:**

  * Stateless; data flows through API and is not stored locally

---

## 📝 Implementation Plan

1. **Initial Setup & Environment:**

   * Flask project setup with templates folder
   * Installed required libraries (`flask`, `requests`, `google-genai`)
2. **Core Module Development:**

   * Implemented Gemini integration and search fallback
   * Designed hybrid agent function
3. **Integration & Testing:**

   * Connected API with frontend and tested query flow
4. **Final Deployment-ready Build:**

   * Deployed live on Render platform
   * Configured BetterUptime monitoring for continuous health checks

---

## ✅ Performance & Validation

* **Evaluation Metrics:**

  * Response time (under 3 seconds for Gemini queries)
  * Correctness of summaries
* **Testing Strategy:**

  * Manual testing with multiple user queries
  * Validated edge cases (no search results, slow response handling)

---

## 🚀 Deployment & Scalability

* **Deployment Plan:**

  * **Live URL:** [https://ai-agent-web-navigator.onrender.com/](https://ai-agent-web-navigator.onrender.com/)
  * Deployed using Render free web service hosting
  * Configured **BetterUptime** monitoring to ensure the app stays online and alerts us of downtime
* **Scalability Considerations:**

  * Can containerize using Docker for load-balanced deployments
  * Could integrate WebSocket for real-time streaming responses
  * Potential to add distributed task queues (Celery) for heavy workloads

---

## 👨‍👩‍👧‍👦 Team

| Name     | Role            | Contribution                                               |
| -------- | --------------- | ---------------------------------------------------------- |
| Member 1 | Team Leader     | Integrated Gemini & Google API, implemented backend        |
| Member 2 | Developer       | Built frontend templates and connected API endpoints       |
| Member 3 | Tester/Designer | Tested user queries, improved UX, and prepared video pitch |

---

## 🎥 Video Pitch

📹 [Google Drive Video Link – Set to “Anyone with the link can view”]

---

## 📂 GitHub Project Branch

🔗 [Link to your project branch]

---

## 📌 Next Steps

* Extend to **full browser automation** (Playwright/Selenium) to perform actions like clicking, scraping, and navigating websites.
* Add **voice input** for hands-free experience.
* Enhance summarization for longer results with pagination handling.
