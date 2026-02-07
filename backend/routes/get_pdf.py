from fastapi.responses import FileResponse

# PDF route
@app.get("/pdf/Constitution")
async def get_pdf():
    return FileResponse("resources/Constitution.pdf")