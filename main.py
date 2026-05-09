from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from idpservice.routes import router as idp_router
from chatbotservice.routes import router as chatbot_router
from ecommerceservice.routes import router as ecommerce_router

app = FastAPI(title="Enterprise AI Platform", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(idp_router, prefix="/api/idp")
app.include_router(chatbot_router, prefix="/api/chatbot")
app.include_router(ecommerce_router, prefix="/api/ecommerce")

@app.get("/")
def healthcheck():
    return {"status": "running", "message": "Enterprise AI Platform API is live"}
