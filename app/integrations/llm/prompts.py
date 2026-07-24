# app/integrations/llm/prompts.py
INVOICE_EXTRACTION_PROMPT = """
You are given two inputs.

1. Invoice image
2. OCR text

The invoice image is the primary source for:

- page layout
- tables
- headers
- Bill To
- Ship To
- Supplier

The OCR text is only to improve recognition of small or blurry text.

If the image and OCR disagree,
prefer the invoice image.
{raw_text}
"""
