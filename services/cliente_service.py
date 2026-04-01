from models.pessoa import Pessoa
from models.endereco import Endereco

from services.api_cep import busca_endereco_por_cep
from utils.validar_cpf import validar_cpf
from utils.validar_email import validar_email_dns

from typing import  Optional

clientes: list[Pessoa] = []


def criar_pessoa(dados) -> Pessoa:

    # validar CPF
    if not validar_cpf(dados["cpf"]):
        raise ValueError("CPF inválido")
    
     # verifica duplicidade
    if buscar_cliente(dados["cpf"]):
        raise ValueError("CPF já cadastrado")

    #chamado esta validação antes que ja não gasta uma requisão HTTP s e o email esta errado no inicio
    validar_email_dns(dados["email"])

    # Busca o endereço na API do ViaCEP
    endereco_api = busca_endereco_por_cep(dados["cep"])
    
    if not endereco_api:
        raise ValueError("CEP inválido")


    # cria objeto Enderço
    endereco = Endereco(
        cep=endereco_api["cep"],
        rua=endereco_api["logradouro"],
        numero=dados.get("numero", "S/N"),  
        bairro=endereco_api["bairro"],
        cidade=endereco_api["cidade"],
        estado=endereco_api["estado"]
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


# ==============================================================
# LISTAR CLIENTES
# ==============================================================

def lista_cliente_cadastrado() -> None:
    if not clientes:
        print("Nenhum cliente cadastrado!")
        return
    
    print(f"\n{'='*50}")
    print(f"Total de clientes cadastrados: {len(clientes)}")
    print(f"\n{'='*50}")

    for i, c in enumerate(clientes, start=1):
        print(f'Cliente {i}')
        print(c)
        print('---------------')

# ==============================================================
# BUSCAR CLIENTE POR CPF
# ==============================================================

def buscar_cliente(cpf: str) -> Optional[Pessoa]:
    for cliente in clientes:
        if cliente.cpf == cpf:
            return clientes
    return None



# ==============================================================
# EXCLUIR CLIENTE
# ==============================================================

def excluir_cliente(cpf: str) -> str:
    cliente = buscar_cliente(cpf)

    if not cliente:
        return "Cliente não encontrado"
    
    clientes.remove(cliente)
    return f"Cliente '{cliente.nome}' removido com sucesso."

# ==============================================================
# ATUALIZAR CLIENTE
# ==============================================================

def atualizar_cliente(cpf: str, dados: dict) -> str:
    cliente = buscar_cliente(cpf)

    if not cliente:
        return "Cliente não encontrado."
    

    if dados.get("email"):
        validar_email_dns(dados["email"])     # valida antes de salvar
        cliente.email = dados["email"]    # setter chamado aqui

    if dados.get("cep"):
        endereco_api = busca_endereco_por_cep(dados["cep"])
        novo_endereco = Endereco(
            cep=endereco_api["cep"],
            rua=endereco_api["logradouro"],
            numero=dados.get("numero", "S/N"),
            bairro=endereco_api["bairro"],
            cidade=endereco_api["cidade"],
            estado=endereco_api["estado"]
        )
        cliente.cep = dados["cep"]
        cliente.endereco = novo_endereco

    return f"Cliente '{cliente.nome}' atualizado com sucesso."