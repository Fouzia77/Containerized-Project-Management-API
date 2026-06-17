from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.services.auth_service import (
    register_user,
    login_user
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)



@router.post("/register", status_code=201)
def register(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = register_user(
        db,
        email,
        password
    )


    if not user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    return {
        "message": "User created",
        "id": user.id
    }




@router.post("/login")
def login(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        email,
        password
    )


    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    return {
        "access_token": token,
        "token_type": "bearer"
    }