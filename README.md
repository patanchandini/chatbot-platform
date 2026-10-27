# Chatbot Platform Backend

A fully functional, tested, and documented backend for a customer support chatbot. 

## Features
*   **Sentiment Analysis:** Detects sarcasm, frustration, and neutral tones.
*   **Escalation Routing:** Automatically routes urgent after-hours tickets to the on-call queue.
*   **Prompt Injection Defense:** Safely ignores malicious documents injected into user queries.
*   **OCR Processing:** Mock extraction of text from images.
*   **SLA Prioritization:** Calculates ticket priority based on keywords.

## Testing
The project includes a comprehensive test suite. To run it:
```bash
python -m pytest tests/