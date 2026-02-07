from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.explain import router as explain_router

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(explain_router,prefix="/api")
