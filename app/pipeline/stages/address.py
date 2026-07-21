from app.pipeline.stages.ocr import run_ocr

def extract_address(text: str) -> str | None:
    lines = [line.strip() for line in text.splitlines()]

    start = NoneSTART_MARKERS = {
    "DELIVER TO",
    "SHIP TO",
    "BILL TO",
}

    for i, line in enumerate(lines):
        if line.upper() == "DELIVER TO":
            start = i + 1
            break

    if start is None:
        return None

    stop_words = {
        "CONTACT",
        "INVOICE DATE",
        "ORDER NO",
        "CLERK",
        "PAYMENT DUE BY",
        "CON NOTE",
        "CARRIER",
        "ITEM CODE",
    }

    address = []

    for line in lines[start:]:
        if line.upper() in stop_words:
            break

        if line:
            address.append(line)

    return "\n".join(address)