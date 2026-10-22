# Task 5: Multimodal & OCR
# Handles invoices, blurred images, and background queuing.

def process_uploaded_file(file_path, message_context):
    """
    Uses OCR to extract order IDs, dates, amounts. Masks PII in logs.
    """
    # TODO: Implement OCR and reconciliation with the message
    return {"extracted_data": {"order_id": "12345", "amount": "$50"}}

def handle_slow_processing(file_id):
    """
    If processing > 30 seconds, move to background queue and notify customer.
    """
    # TODO: Implement async background queue
    return {"status": "queued", "notified_customer": True}
