#app/routes
from fastapi import APIRouter

router = APIRouter(
    tags=['docs'],
    prefix= ['/docs']

)


@router.post("/")
async def upload_document():
    pass

@router.get("/")
async def list_documents():
    pass

@router.get("/{document_id}")
async def get_document(document_id: int):
    pass