from controllers.cliente_controller import(
    controller_cadastrar,
    controller_listar,
    controller_buscar,
    controller_atualizar,
    controller_excluir,
    )


def exibir_menu() -> None:
    print("\n" + "=" * 50)
    print("    SISTEMA DE CADASTRO DE CLIENTES")
    print("=" * 50)
    print("  [1] Cadastrar novo cliente")
    print("  [2] Listar clientes")
    print("  [3] Buscar cliente por CPF")
    print("  [4] Atualizar cliente")
    print("  [5] Excluir cliente")
    print("  [0] Sair")
    print("=" * 50)


def executar_opcao(opcao: str) -> bool:
    opcoes = {

        "1": controller_cadastrar,
        "2": controller_listar,
        "3": controller_buscar,
        "4": controller_atualizar,
        "5": controller_excluir,


    }
    if opcao == "0":
        return False
    elif opcao in opcoes:
        opcoes[opcao]()

    else:
        print("\n Opção inválida. Digite um número entre 0 e 5.")

    return True

def iniciar_menu() -> None:
    print("\nBem-vindo ao Sistema de Cadastro de Clientes!")
    continuar = True
    while continuar:
        exibir_menu()
        opcao = input("\nDigite a opção desejada: ").strip()
        continuar = executar_opcao(opcao)
    
    print("\nSistema encerrado. Até logo! ")