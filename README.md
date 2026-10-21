# Multilingual AI Support Chatbot Platform

This repository contains the modular architecture for a comprehensive AI support chatbot, addressing six core requirements.

## Architecture
The project uses a monorepo structure. All modules share a `core` config and session state, but isolate their specific logic.

- `modules/sentiment_escalation/`: Handles sarcasm, urgency, and after-hours queues.
- `modules/ticketing_sla/`: Handles duplicate detection and SLA routing.
- `modules/kb_pipeline/`: Handles document versioning and maintenance windows.
- `modules/rag_assistant/`: Handles historical policy retrieval and prompt injection defense.
- `modules/multimodal_ocr/`: Handles invoice parsing and delayed background queues.
- `modules/multilingual_sessions/`: Handles 30-minute session expiries and 3+ languages.

## Testing (Hidden Evaluations)
The `tests/hidden_evaluations/` directory contains the mock scripts simulating the edge cases requested in the prompt, such as:
- Sarcastic messages
- Simulated SLA time changes
- Blurred image rejection
- Conflicting/Expired policies
- Prompt injection attempts

## Datasets
See the linked Google Drive folder for mock datasets used in these tests.
