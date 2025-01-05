from sqlalchemy.orm import Session
from app.cruds.user import get_user_by_username
from app.models import User  # Importe o modelo User caso precise

# Função para verificar se o usuário é admin
def check_user_admin(username: str, db: Session) -> bool:
    user = get_user_by_username(db, username)
    if user is None:
        return False  # Usuário não encontrado
    return user.admin  # Retorna se o usuário tem privilégio de admin
