# Task 1: Multilingual Sentiment & Escalation
# Handles sarcasm, urgency, and after-hours queues.

def analyze_sentiment(message, history):
    """
    Analyzes the message for: positive, neutral, negative, frustrated, urgent, sarcastic.
    Returns a confidence score.
    """
    # TODO: Integrate NLP model here
    return {"sentiment": "frustrated", "confidence": 0.85}

def check_escalation(sentiment, history, is_after_hours):
    """
    Triggers escalation based on repeated negatives, account compromise, etc.
    Records reason, activated condition, and conversation summary.
    """
    # TODO: Implement business logic for escalation triggers
    if sentiment["sentiment"] == "frustrated" and is_after_hours:
        return {
            "escalate": True, 
            "reason": "Urgent after-hours complaint", 
            "queue": "on-call",
            "summary": "Customer is frustrated after hours."
        }
    return {"escalate": False}
