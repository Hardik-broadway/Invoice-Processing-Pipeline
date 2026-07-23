# app/integrations/llm/prompts.py
INVOICE_EXTRACTION_PROMPT = """
You are an expert invoice extraction system.

Extract structured invoice information from the OCR text.

Rules:

- Use only information explicitly present in the OCR text.
- Never guess or infer values.
- If a field cannot be found, return null.
- Preserve all invoice numbers exactly.
- Preserve dates exactly.
- Preserve addresses exactly.
- Put charge to in the supplier object and deliver to in the customer object.
- Preserve monetary values exactly.
- Include every line item found.
- Return data matching the provided schema.

OCR Text:

{raw_text}
"""
