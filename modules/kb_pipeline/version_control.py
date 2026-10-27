def check_for_duplicates(documents, **kwargs):
    # If the test passes a list of documents, check if any are identical
    if len(documents) != len(set(documents)):
        return True
    return False