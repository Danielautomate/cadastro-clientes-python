# =====================================================
# VALIDAÇÃO DE CPF
#
# Regras:
# ✔ CPF deve ser string
# ✔ Deve possuir 11 caracteres numéricos
# ✔ Não pode ter todos os dígitos iguais
# ✔ Valida os dígitos verificadores oficiais
#   pelo algoritmo da Receita Federal
# =====================================================

def validar_cpf(cpf: str) -> bool:

    # verifica se o CPF é texto
    if not isinstance(cpf, str):
        raise TypeError("CPF deve ser uma string")

    # remove pontos e traço se vier formatado
    cpf = cpf.replace(".", "").replace("-", "").strip()

    # verifica tamanho e se contém somente números
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF deve ter 11 dígitos numéricos")  # ✅ ValueError

    # rejeita CPFs com todos os dígitos iguais
    if len(set(cpf)) == 1:
        raise ValueError("CPF inválido: todos os dígitos são iguais")

    # --------------------------------------------------
    # Cálculo do 1º dígito verificador
    # multiplica cada dígito pelo peso 10,9,8,...,2
    # se resto < 2 → dígito = 0
    # se resto >= 2 → dígito = 11 - resto
    # --------------------------------------------------
    soma = sum(int(d) * peso for d, peso in zip(cpf, range(10, 1, -1)))
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto

    if primeiro_digito != int(cpf[9]):
        raise ValueError("CPF inválido: dígito verificador incorreto")

    # --------------------------------------------------
    # Cálculo do 2º dígito verificador
    # mesma lógica mas com pesos 11,10,9,...,2
    # --------------------------------------------------
    soma = sum(int(d) * peso for d, peso in zip(cpf, range(11, 1, -1)))
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto

    if segundo_digito != int(cpf[10]):
        raise ValueError("CPF inválido: dígito verificador incorreto")

    return True

