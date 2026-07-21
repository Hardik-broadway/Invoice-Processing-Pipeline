import os
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"
from PIL import Image
from paddleocr import PaddleOCR
from paddleocr import PaddleOCR
import numpy as np

ocr_engine = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    )

# def run_ocr(images):
#     results = []


#     for image in images:
#         print(type(image))
#         image_np = np.array(image)
#         print(type(image_np))
#         result = list(ocr_engine.predict([image_np]))
#         results.append(result)
#     return results
def run_ocr(images: list[Image.Image]):
    results = []
    for image in images:
        image_np = np.asarray(image)
        page_result = ocr_engine.predict(image_np)
        results.append(page_result)
    return results


def extract_text(ocr_results: list) -> str:
    lines = []

    for page in ocr_results:
        lines.extend(page[0]["rec_texts"])

    return "\n".join(lines)

