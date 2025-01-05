from app.models.insurer import Insurer as InsurerModel
from app.schemas.insurer import InsurerCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

def create_insurer(db: Session, insurer: InsurerCreate):
    print('Cheguei Para atualizar')
    print(insurer)

    try:
        db_insurer = InsurerModel( insurer_name = insurer.insurer_name)
    
        db.add(db_insurer)
        db.commit()  
        db.refresh(db_insurer)  
        return db_insurer 
    
    except IntegrityError as e:
        # Captura violação de constraint única (ex: email ou username já existente)
        db.rollback()  # Desfaz a transação
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insurer already exists."
        )
    except Exception as e:
        # Para outros erros inesperados
        db.rollback()  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )
    return


def delete_insurer(db: Session, insurer_id: int):
    return

def update_insurer(db: Session, insurer_id: int):
    return

