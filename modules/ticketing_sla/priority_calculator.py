def calculate_priority(issue_description, **kwargs):
    text = issue_description.lower()
    if "urgent" in text or "down" in text or "broken" in text:
        return {"priority": "high", "sla_hours": 1}
    elif "slow" in text or "bug" in text:
        return {"priority": "medium", "sla_hours": 8}
    else:
        return {"priority": "low", "sla_hours": 24}