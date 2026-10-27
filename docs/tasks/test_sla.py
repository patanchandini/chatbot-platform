from modules.ticketing_sla.priority_calculator import calculate_priority

def test_high_priority():
    # Assuming the task says "urgent" makes it high priority
    result = calculate_priority("urgent")
    assert result == "high"