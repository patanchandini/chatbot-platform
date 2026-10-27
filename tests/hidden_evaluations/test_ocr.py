from modules.multimodal_ocr.image_processor import extract_text_from_image

def test_image_processing():
    result = extract_text_from_image("receipt.png")
    assert "Extracted text" in result