from app.models.policy import Policy as PolicyModel
from app.schemas.policy import PolicyCreate, PolicyRead
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

def create_policy(db: Session, policy: PolicyCreate, user_id: int, insurer_id: int):
    
    db_policy = PolicyModel(
        created_by_user_id = user_id,
        start_date= policy.start_date,
        end_date= policy.end_date,
        gross_commission = policy.gross_commission,
        store_commission = policy.store_commission,
        commission_rate = policy.commission_rate,
        transmition_date =  policy.transmition_date,
        customer_name = policy.customer_name,
        insurer_id = insurer_id
    )
    db.add(db_policy)
    
    db.add(db_policy)
    db.commit()  
    db.refresh(db_policy)  
    return db_policy
    
    return None

'''
def create_policy(db: Session, policy: PolicyCreate):
    print('Cheguei Para atualizar')
    print(policy)

    try:
        db_policy = PolicyModel( policy_name = policy.policy_name)
    
        db.add(db_policy)
        db.commit()  
        db.refresh(db_policy)  
        return db_policy 
    
    except IntegrityError as e:
        # Captura violação de constraint única (ex: email ou username já existente)
        db.rollback()  # Desfaz a transação
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="policy already exists."
        )
    except Exception as e:
        # Para outros erros inesperados
        db.rollback()  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )
    return


def delete_policy(db: Session, policy_id: int):
    return

def update_policy(db: Session, policy_id: int):
    return

'''