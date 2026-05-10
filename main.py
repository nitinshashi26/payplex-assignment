from fastapi import FastAPI
from products.routes import router as product_router
from recommendations.routes import router as rec_router

app = FastAPI(title="PayPlex AI E-commerce API", version="1.0")
app.include_router(product_router, prefix="/api/products")
app.include_router(rec_router, prefix="/api/recommend")

@app.get("/")
def alive():
    return {"status": "ok", "service": "AI E-commerce"}
