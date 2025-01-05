import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Variáveis de configuração
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
TOKEN_TIME = os.getenv("DEFAULT_TOKEN_LIFE")