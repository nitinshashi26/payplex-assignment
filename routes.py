from fastapi import APIRouter, Query
from .recommender import recommend_for_user

router = APIRouter(tags=["Recommendations"])

@router.get("/")
def recommend(user_id: int = Query(...)):
    return {"user_id": user_id, "recommendations": recommend_for_user(user_id)}
