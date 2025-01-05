from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, user , insurer, policy

# Inicializa o banco de dados
Base.metadata.create_all(bind=engine)

# Cria a instância do FastAPI
app = FastAPI()

# Inclui as rotas
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(insurer.router, prefix="/insurer", tags=['Insurer'])
app.include_router(policy.router, prefix="/policy", tags=['Policy'])
