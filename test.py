# # from pathlib import Path

# # from app.processing.stages.pdf import pdf_to_images

# # images = pdf_to_images(Path("C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/app/uploads/Invoice206027.pdf"))

# # print(f"Pages: {len(images)}")
# # print(images[0])

# from app.processing.stages.pdf import pdf_to_images
# from app.processing.stages.ocr import run_ocr


# # print(type(ocr_engine))

# images = pdf_to_images(
#     "C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/app/uploads/Invoice206027.pdf"
# )

# results = run_ocr(images)

# # print(results)

from app.pipeline.stages.pdf import pdf_to_images
from app.pipeline.stages.ocr import run_ocr
from app.pipeline.stages.address import extract_address

# Convert PDF to images
images = pdf_to_images("C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/uploads/Invoice206027.pdf")

# Run OCR
ocr_results = run_ocr(images)
page = ocr_results[0][0]

for text, box in zip(page["rec_texts"], page["rec_boxes"]):
    print(box, text)
# # Get the recognized text from the first page
# text = "\n".join(page["rec_texts"])
# address = extract_address(text)
# print("===== OCR TEXT =====")
# print(address)

# text = "\n".join(page["rec_texts"])

# address = extract_address(text)

# print(address)

# # print("\n===== EXTRACTED ADDRESS =====")
# # address = extract_address(text)
# # print(address)

# from pprint import pprint

# images = pdf_to_images("C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/app/uploads/Invoice206027.pdf")
# ocr_results = run_ocr(images)
# page = ocr_results[0][0]

# print(page.keys())
# for line in page["rec_texts"]:
#     print(line)

# # print(type(ocr_results))
# # print(len(ocr_results))

# # print(type(ocr_results[0]))
# # pprint(ocr_results[0])