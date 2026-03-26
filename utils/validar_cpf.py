# =====================================================
# FUNÇÃO 4
# Validação básica de CPF (APENAS PARA TESTES)
#
# Regras atuais:
# ✔ CPF deve ser string
# ✔ Deve possuir 11 caracteres
# ✔ Deve conter apenas números
#
# OBS:
# Ainda NÃO valida os dígitos oficiais do CPF
# =====================================================
def validar_cpf(cpf: str) -> bool:

    # verifica se o CPF é texto
    if not isinstance(cpf, str):
        raise TypeError("CPF deve ser uma string")
    cpf = cpf.replace(".", "").replace("-", "").strip()

    # verifica tamanho e se contém somente números
    if len(cpf) != 11 or not cpf.isdigit():
        raise TypeError("CPF deve ter 11 digitos númericos")
    
    if len(set(cpf)) == 1:
        raise ValueError("CPF invalido: Todos os digitos São iguais")
    
    return True



