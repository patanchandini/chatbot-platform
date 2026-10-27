from modules.ticketing_sla.priority_calculator import calculate_priority

def test_high_priority():
    result = calculate_priority("The server is down and this is urgent!")
    assert result["priority"] == "high"
    assert result["sla_hours"] == 1

def test_low_priority():
    result = calculate_priority("I have a general question about my bill.")
    assert result["priority"] == "low"