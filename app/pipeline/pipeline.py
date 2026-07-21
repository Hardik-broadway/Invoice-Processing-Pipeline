from pathlib import Path
from stages.ocr import run_ocr, extract_text
from stages.pdf import pdf_to_images
from stages.address import extract_address


def process_invoice(pdf_path: str) -> str:
    
    images = pdf_to_images(pdf_path)
    ocr_result = run_ocr(images)
    text = extract_text(ocr_result)
    address = extract_address(text)
    return address




if __name__ == "__main__":
    address = process_invoice("C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/app/uploads/Invoice206027.pdf")
    print(address)
