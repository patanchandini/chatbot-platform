# Task 6: Multilingual & Sessions
# Handles 30-minute idle timeouts, 24-hour restores, and language switching.

def manage_session(session_id, last_active_time, current_time):
    """
    Ends session after 30 mins of inactivity.
    If customer returns within 24 hours, restore summary.
    """
    # TODO: Implement session expiry and restore logic
    return {"session_active": False, "action": "summary_restored"}

def handle_mixed_language(message, history):
    """
    Preserves names, order IDs. Requests clarification if confidence is low.
    """
    # TODO: Implement language detection and context preservation
    return {"language": "ES-EN", "confidence": 0.9}
