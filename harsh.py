import os

# Gerar uma chave secreta segura de 256 bits
secret_key = os.urandom(32).hex()  # Gera uma chave hexadecimal de 32 bytes
print(secret_key)
