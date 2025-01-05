from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.insurer import InsurerCreate, InsurerRead
from app.schemas.user import User
from app.models.insurer import Insurer
from app.cruds.insurer import create_insurer
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import get_current_admin_user

router = APIRouter()

@router.post("/", response_model=InsurerRead)
def create(insurer: InsurerCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    result = create_insurer(db=db,insurer=insurer)
  
    return result