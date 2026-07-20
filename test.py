# from pathlib import Path

# from app.processing.stages.pdf import pdf_to_images

# images = pdf_to_images(Path("C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/app/uploads/Invoice206027.pdf"))

# print(f"Pages: {len(images)}")
# print(images[0])

from app.processing.stages.ocr import ocr_engine

print(type(ocr_engine))