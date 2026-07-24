from pathlib import Path

import pymupdf
from PIL import Image

DPI = 300


def pdf_to_images(pdf_path: Path) -> list[Image.Image]:
    """
    Convert all pages of a PDF into PIL Images.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of PIL Images, one per page.
    """
    images = []

    zoom = DPI / 72
    matrix = pymupdf.Matrix(zoom, zoom)

    with pymupdf.open(pdf_path) as pdf:
        for page in pdf:
            pixmap = page.get_pixmap(matrix=matrix)

            image = Image.frombytes(
                "RGB",
                (pixmap.width, pixmap.height),
                pixmap.samples,
            )

            images.append(image)

    return images
