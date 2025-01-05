from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, User, UserDetail
from app.cruds.user import create_user, get_user_by_id, delete_user, grant_admin
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import get_current_user, hash_password, get_current_admin_user



router = APIRouter()

# Rota para criar um novo usuário
@router.post("/", response_model=User)
def create(user: UserCreate, db: Session = Depends(get_db)):
    user.password = hash_password(user.password)
    result = create_user(user=user, db=db)
   
    return  result
 
# Rota para obter um usuário por ID
@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@router.get("/detail/{user_id}", response_model=UserDetail)
def get_user_details(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_user = get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user



@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db), admin_user: User = Depends(get_current_admin_user)):
    # Verifica se o usuário que está tentando excluir é o mesmo ou se é um administrador

    if current_user.user_id != user_id and not current_user.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this user"
        )

    # Chama a função para excluir o usuário
    return delete_user(user_id=user_id, db=db)

@router.put('/grant_admin/{user_id}')
def grant_adm(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return grant_admin(user_id=user_id, db=db)
    
