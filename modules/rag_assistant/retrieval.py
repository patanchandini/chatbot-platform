# Task 4: RAG-based Knowledge Assistant
# Handles metadata filtering, citations, and prompt-injection defense.

def retrieve_policy(query, customer_date, metadata):
    """
    Selects latest applicable policy, ignoring future/expired policies for current questions.
    """
    # TODO: Implement historical policy retrieval based on specified date
    return {"document": "policy_v2.pdf", "citation": "Section 4.2"}

def generate_answer(query, retrieved_docs):
    """
    Refuses or clarifies if evidence is missing. Ignores malicious embedded instructions.
    """
    # TODO: Detect unsupported claims and prompt injection
    return {"answer": "Here is your answer...", "safe": True}
