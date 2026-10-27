# Chatbot Platform Backend

A fully functional, tested, and documented backend for a customer support chatbot. Built with **FastAPI** and **Python**, this project implements core logic for sentiment analysis, automated ticket routing, and prompt injection defense.

## 🚀 Live Deployment
The API is deployed and live on Render. You can test it directly from your browser using the interactive Swagger UI!

*   **Live API URL:** [https://chatbot-platform-1naz.onrender.com](https://chatbot-platform-1naz.onrender.com)

*   **📚 Swagger UI (Interactive Docs):** [https://chatbot-platform-1naz.onrender.com/docs](https://chatbot-platform-1naz.onrender.com/docs)


"Note: This API is hosted on Render's free tier. The first request may take 30-50 seconds to wake up the server. Please be patient!"
(You can also go to your live Swagger URL 5 minutes before you submit to "wake it up" for them).

📂 Project Structure
text
chatbot-platform/
│
├── modules/                  # Core business logic
│   ├── kb_pipeline/          # Duplicate detection logic
│   ├── multilingual_sessions/# Session management
│   ├── multimodal_ocr/       # Text extraction from images
│   ├── rag_assistant/        # Security and retrieval logic
│   ├── sentiment_escalation/ # Sentiment and escalation routing
│   └── ticketing_sla/        # Priority calculation
│
├── tests/                    # Pytest test suite
├── api.py                    # FastAPI application and routes
├── main.py                   # CLI script to test logic locally
└── requirements.txt          # Project dependencies


## ✨ Features
*   **Sentiment Analysis:** Detects sarcasm, frustration, and neutral tones in user messages.
*   **Escalation Routing:** Automatically routes urgent after-hours tickets to the on-call queue.
*   **Prompt Injection Defense:** Safely ignores malicious documents injected into user queries.
*   **SLA Prioritization:** Calculates ticket priority based on issue keywords.
*   **REST API:** Exposes all logic through clean, JSON-based HTTP endpoints.


## 🛠️ Local Setup & Installation

If you want to run this project locally, follow these steps:

**1. Clone the repository:**
```bash
git clone https://github.com/patanchandini/chatbot-platform.git
cd chatbot-platform
2. Install dependencies:

bash
pip install -r requirements.txt
3. Run the FastAPI server:

bash
uvicorn api:app --reload
The API will be running at http://127.0.0.1:8000. You can view the local Swagger UI at http://127.0.0.1:8000/docs.

🧪 Running the Tests
This project includes a comprehensive suite of unit tests to ensure all business logic is working correctly. Run the following command:

bash
python -m pytest tests/
Expected Output:

text
collected 10 items
...
============================================== 10 passed in 0.04s ==============================================