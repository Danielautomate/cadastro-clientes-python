import socket
import re

PADRAO_EMAIL = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validar_email(email:  str) -> bool:
# Verifica se é uma string
    if not isinstance(email, str):
    
        raise TypeError("Email deve ser uma string")
    
    #removendo os espaços
    email = email.strip()
    #Vericar se está vazio
    if not email:
        raise ValueError("Email não poder ser vazio")
    
    # valida o fromato primeiro com regex . porque não adianta consulta DNS se formato ja estive errado
    if not PADRAO_EMAIL.match(email):
        raise ValueError(f" Email com formato inválido: {email}")


    # Extrai o domínio — parte depois do @
    # "joao@gmail.com".split("@")[1] → "gmail.com"
    dominio = email.split("@")[1] 

    
    try:
        # Consulta o DNS da internet perguntando se o domínio existe
        # getaddrinfo(host, port) devolve lista de endereços IP
        # Se o domínio não existir lança socket.gaierror
        socket.getaddrinfo(dominio, None)
        return True

    except socket.gaierror:
        # gaierror = "get address info error"
        # domínio não foi encontrado na internet
        raise ValueError(f"Domínio '{dominio}' não existe na internet")

    except OSError:
        # OSError cobre problemas gerais de rede
        raise ConnectionError("Erro de conexão ao verificar domínio")
    

