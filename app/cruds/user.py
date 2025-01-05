from app.models.user import User as UserModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.schemas.user import UserCreate, User, UserLogin


def create_user(db: Session, user: UserCreate):
    try:
        db_user = UserModel(
            user_name=user.user_name,
            email=user.email,
            password=user.password
        )
    
        db.add(db_user)
        db.commit()  # Comita a transação
        db.refresh(db_user)  # Atualiza para pegar os campos gerados (e.g., id)
        return User.from_orm(db_user)  # Retorna o modelo Pydantic User
    
    except IntegrityError as e:
        # Captura violação de constraint única (ex: email ou username já existente)
        db.rollback()  # Desfaz a transação
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists."
        )
    except Exception as e:
        # Para outros erros inesperados
        db.rollback()  # Desfaz a transação
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )


        
def get_user_by_username(db: Session, user_name: str):
    db_user = db.query(UserModel).filter(UserModel.user_name == user_name).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

def get_user_to_login(db: Session, user_name: str):
    db_user = db.query(UserModel).filter(UserModel.user_name == user_name).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user # UserLogin.from_orm(db_user)

def get_user_by_id(db: Session, user_id: int):
    db_user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user    

def delete_user(db: Session, user_id: int):
    # Buscar o usuário pelo ID
    db_user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    
    # Verificar se o usuário existe
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Deletar o usuário
    db.delete(db_user)
    db.commit()  # Commit da transação para efetivar a exclusão

    return {"detail": "User deleted successfully"}


def grant_admin(db: Session, user_id: int):
    # Fetch the user by ID
    db_user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    
    if not db_user:
        raise ValueError(f"User with ID {user_id} not found")
    
    # Update the admin field
    db_user.admin = True
    db.commit()
    db.refresh(db_user)  # Refresh the instance to reflect changes in the DB
    
    return {"Message": f"User {db_user.user_name} updated sucesfully"}