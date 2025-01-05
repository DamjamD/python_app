from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin, User
from app.cruds.user import  get_user_by_username
from app.utils import verify_password, create_access_token
from app.database import get_db
from app.schemas.auth import Token

router = APIRouter()


def authenticate_user(user_name: str, password: str, db: Session):
    user = get_user_by_username(db, user_name)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )

    return user


@router.post("/")
def default():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,  # Define o código de status como 400
        detail="Incorrect request",  # Mensagem de erro detalhada
    )


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: UserLogin, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(form_data.user_name, form_data.password, db)
        access_token = create_access_token({"sub": user.user_name})
        return Token(access_token=access_token, token_type="bearer")
    except HTTPException as e:
        print(f"Authentication failed: {e.detail}")
        raise e

