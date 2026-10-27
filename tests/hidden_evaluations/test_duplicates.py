from modules.kb_pipeline.version_control import check_for_duplicates

def test_has_duplicates():    # <--- MUST start with 'test_'
    docs = ["apple", "banana", "apple"]
    assert check_for_duplicates(docs) is True

def test_no_duplicates():     # <--- MUST start with 'test_'
    docs = ["apple", "banana", "orange"]
    assert check_for_duplicates(docs) is False