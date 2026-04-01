
from services.cliente_service import(criar_pessoa, lista_cliente_cadastrado, buscar_cliente, 
                                     excluir_cliente, atualizar_cliente)

# ==============================================================
# CONTROLLER: CADASTRAR
# ==============================================================


def controller_cadastrar() -> None:
    print("\n" + "="*50)
    print(" CADASTRAR NOVO CLIENTE")
    print("="*50)


    try:
        nome = input("Nome completo: ").strip()
        cpf = input("CPF (somente números): ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        email = input("Email: ").strip()
        cep = input("CEP (somente números): ").strip()
        numero = input("Numero da Residencia: ").strip()


    #dicionario de forma organizada pra armazenar os dados do usuario digitado
    #dados de uma vez so chamado função.
        dados = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "email": email,
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


def controller_listar() -> None:
    print("\n" + "="*50)
    print("  CLIENTES CADASTRADOS")
    print("="*50)
    lista_cliente_cadastrado()



# ==============================================================
# CONTROLLER: BUSCAR
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

    try:
        cpf = input("Digite o CPF do cliente (somente números): ").strip()
        cliente = buscar_cliente(cpf)

        if not cliente:
            print(f"\n Nenhum cliente encontrado com o CPF: {cpf}")
            return

        print(f"\nCliente encontrado: {cliente.nome}")
        print("Deixe em branco para não alterar o campo. \n")

        novo_email = input(f"Novo email (atual: {cliente.email}): ").strip()
        novo_cep = input(f"Novo CEP (atual: {cliente.cep}): ").strip()
        novo_numero = input(f"Novo número da residência (se mudou o CEP): ").strip()


        dados = {}
        if novo_email:
            dados["email"] = novo_email
        if novo_cep:
            dados["cep"] = novo_cep
        if novo_numero:
            dados["numero"] = novo_numero


        if not dados:
            print("\ Nenhum dado informado. Nada foi alterado.")
            return
        mensagem = atualizar_cliente(cpf, dados)
        print(f"\n {mensagem}")

    except ValueError as e:
        print(f"\n❌ Erro de validação: {e}")
    except ConnectionError as e:
        print(f"\n❌ Erro de conexão: {e}")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
    

# ==============================================================
# CONTROLLER: EXCLUIR
# ==============================================================

def controller_excluir() -> None:
    print("\n" + "="*50)
    print("  EXCLUIR CLIENTE")
    print("="*50)



    try:
        cpf = input("Digite o CPF do cliente a excluir (somente números): ").strip()
        cleinte = buscar_cliente(cpf)

        if not cleinte:
            print(f"\n Nenhum cliente encontrado com o CPF: {cpf}")
            return

        print(f"\nCliente encontrado{cleinte.nome}")
        confirmacao = input("Confimar exlusão? (s/n): ").strip().lower()

        if confirmacao == 's':
            mensagem = excluir_cliente(cpf)
            print(f"\n✅ {mensagem}")
        else:
            print("\n Exclusão cancelada.")

        
    except Exception as e:
        print(f"\n❌ Erro: {e}")