from modules.multilingual_sessions.session_manager import manage_session

def test_create_session():
    result = manage_session("user123", language="es")
    assert result["user_id"] == "user123"
    assert result["language"] == "es"
    assert result["active"] is True

# --- ADD THIS NEW TEST FUNCTION ---
def test_default_language():
    result = manage_session("user456")
    assert result["language"] == "en"  # Checks if it defaults to English
    assert result["active"] is True