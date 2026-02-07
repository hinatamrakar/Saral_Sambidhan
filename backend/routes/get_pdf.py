from fastapi.responses import FileResponse
from fastapi import APIRouter
router=APIRouter()

# PDF route
@router.get("/pdf/Constitution")
async def get_pdf():
    return FileResponse("resources/Constitution.pdf")

