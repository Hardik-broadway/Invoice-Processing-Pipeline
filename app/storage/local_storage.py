# app/storage/local_storage.py
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.common.interfaces.storage import Storage

UPLOAD_DIR = Path("uploads")


class LocalStorage(Storage):
    async def save(
        self,
        file: UploadFile,
    ) -> tuple[str, int]:

        UPLOAD_DIR.mkdir(exist_ok=True)

        original_name = file.filename or "document.pdf"

        extension = Path(original_name).suffix

        stored_filename = f"{uuid4()}{extension}"

        contents = await file.read()

        (UPLOAD_DIR / stored_filename).write_bytes(contents)

        return stored_filename, len(contents)

    async def delete(self, filename: str) -> None:

        path = UPLOAD_DIR / filename

        if path.exists():
            path.unlink()
