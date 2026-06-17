from fastapi import APIRouter, Depends

from src.database.models import User
from src.core.dependencies import get_current_user


router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)



@router.get("/me")
def get_me(
    user: User = Depends(get_current_user)
):

    return {
        "id": user.id,
        "email": user.email
    }