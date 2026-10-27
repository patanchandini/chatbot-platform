def process_query(query, injected_doc=None, **kwargs):
    # We ignore the injected_doc completely for security.
    # We just create a mock response based on the user's actual query.
    
    result = f"Here is the information for: {query}"
    
    return result