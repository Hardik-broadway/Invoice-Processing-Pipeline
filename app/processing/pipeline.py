from pathlib import Path

def process_invoice(pdf_path: str) -> str:
    images = pdf_to_images(pdf_path)
    ocr_result = run_ocr(images)
    address = extract_address(ocr_result)
    return address