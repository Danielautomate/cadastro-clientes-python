
from services.cliente_service import(criar_pessoa, lista_cliente_cadastrado, buscar_cliente, 
                                     excluir_cliente, atualizar_cliente)

# ==============================================================
# CONTROLLER: CADASTRAR
# ==============================================================


def controller_casdastrar() -> None:
    print("\n" + "="*50)
    print(" CADASTRAR NOVO CLIENTE")
    print("="*50)


    try:
        nome = input("Nome completo: ").strip()
        cpf = input("CPF (somente números): ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").stip()
        email = input("Email: ").strip()
        cep = input("CEP (somente números): ").strip()
        numero = input("Numero da Residencia: ").strip()


    #dicionario de forma organizada pra armazenar os dados do usuario digitado
    #dados de uma vez so chamado função.
        dados = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "cep": cep,
        "numero": numero,
        }


    #chama o service  passado o dicionario

        cliente= criar_pessoa(dados)

        print(f"\n✅ Cliente cadastrado com sucesso!")
        print(f"   Código: {cliente.codigo}")
        print(f"   Nome:   {cliente.nome}")




    except ValueError as e:
        print(f"\n❌ Erro de validação: {e}")

    except ConnectionError as e:
        print(f"\n❌ Erro de conexão: {e}")

    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")



# ==============================================================
# CONTROLLER: LISTAR
# ==============================================================

def controller_buscar() -> None:
    print("\n" + "="*50)
    print(" BUSCA CLIENTE")
    print("="*50)

    try:
        cpf = input("Digite o CPF do cliente  (somente números): ").strip()
        
        cliente = buscar_cliente(cpf)

        if cliente:
            print(f"\n✅ Cliente encontrado:")
            print(cliente) 
        else:
            print(f"\n⚠️  Nenhum cliente encontrado com o CPF: {cpf}")

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        







# ==============================================================
# CONTROLLER: ATUALIZAR
# ==============================================================
def controller_atualizar() -> None:
    print("\n" + "="*50)
    print(" ATUALIZAR CLIENTE")
    print("="*50)

# ==============================================================
# CONTROLLER: EXCLUIR
# ==============================================================

def controller_excluir() -> None:
    pass