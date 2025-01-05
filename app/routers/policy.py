from fastapi import APIRouter, Depends
from app.schemas.policy import PolicyCreate, PolicyRead
from app.models.policy import Policy as PolicyModel
from app.schemas.user import User
from app.cruds.policy import create_policy
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import get_current_user, okay_message

router = APIRouter()

@router.post("/") #, response_model = PolicyRead)
def create(policy: PolicyCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    current_user.user_id
    
    print(policy)

    result = create_policy(db=db, policy=policy, user_id=current_user.user_id,insurer_id=1)
    

    
    return result


#def create(policy: PolicyCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#      return policy