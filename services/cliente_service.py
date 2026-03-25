from models.pessoa import Pessoa
from models.endereco import Endereco

from services.api_cep import busca_endereco_por_cep
from utils.validar_cpf import validar_cpf

from typing import List, Dict, Optional

clientes: list[Pessoa] = []


def criar_pessoa(dados):

    # validar CPF
    if not validar_cpf(dados["cpf"]):
        raise ValueError("CPF inválido")
     # 🔥 verifica duplicidade
    if buscar_cliente(dados["cpf"]):
        raise ValueError("CPF já cadastrado")

    # buscar Enderço na Api
    endereco_api = busca_endereco_por_cep(dados["cep"])
    
    if not endereco_api:
        raise ValueError("CEP inválido")


    # cria objeto Enderço
    endereco = Endereco(
        endereco_api["logradouro"],
        endereco_api["bairro"],
        endereco_api["cidade"],
        endereco_api["estado"]
    )

    # cria obejeto Pessoa
    pessoa = Pessoa(
        nome=dados["nome"],
        data_nascimento=dados["data_nascimento"],
        cpf=dados["cpf"],
        cep=dados["cep"],
        email=dados["email"],
        endereco=endereco
    )


    clientes.append(pessoa) # salva na lista 
    return pessoa


# ------------------------
# Lista de cliente cadastrado
# ------------------------

def lista_cliente_cadastrado() -> None:
    if not clientes:
        print("Nenhum cliente cadastrado!")
        return

    print(f"Total de clientes cadastrados: {len(clientes)}")

    for i, c in enumerate(clientes, start=1):
        print(f'Cliente {i}')
        print(c)
        print('---------------')

# ------------------------
# BUSCAR Cliente cadastrado por cpf 
# ------------------------

def buscar_cliente(cpf: str) -> Optional[Pessoa]:
    for c in clientes:
        if c.cpf == cpf:
            return c
    return None



# ------------------------
# Excluir Cliente
# ------------------------

def excluir_cliente(cpf: str) -> str:
    cliente = buscar_cliente(cpf)

    if not cliente:
        return "Cliente não encontrado"
    
    clientes.remove(cliente)
    return "Cliente Removindo com sucesso"
