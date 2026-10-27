def manage_session(user_id, language="en", **kwargs):
    # Return a dictionary representing the active session
    return {
        "user_id": user_id,
        "language": language,
        "active": True,
        "message": f"Session started for user {user_id} in {language}."
    }