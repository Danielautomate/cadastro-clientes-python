# 📋 Sistema de Cadastro de Clientes

Sistema de cadastro de clientes desenvolvido em Python com arquitetura em camadas (MVC), validação de CPF com algoritmo oficial da Receita Federal, validação de email em 3 níveis e integração com a API ViaCEP para busca automática de endereços.

---

## 🚀 Funcionalidades

- ✅ Cadastrar novo cliente com busca automática de endereço pelo CEP
- ✅ Listar todos os clientes cadastrados
- ✅ Buscar cliente por CPF
- ✅ Atualizar email e/ou endereço do cliente
- ✅ Excluir cliente com confirmação
- ✅ Validação de CPF com dígitos verificadores oficiais da Receita Federal
- ✅ Validação de email em 3 níveis (básico, regex e DNS)
- ✅ Menu interativo no terminal
- ✅ Tratamento de erros em todas as operações

---

## 🗂️ Estrutura do Projeto

```
cadastro-clientes-python/
├── main.py                          # Ponto de entrada do sistema
├── menu/
│   └── menu_principal.py            # Menu e opções do terminal
├── controllers/
│   └── cliente_controller.py        # Coleta input e trata erros
├── services/
│   ├── api_cep.py                   # Integração com API ViaCEP
│   └── cliente_service.py           # Lógica de negócio
├── models/
│   ├── pessoa.py                    # Classe Pessoa (cliente)
│   └── endereco.py                  # Classe Endereco
├── utils/
│   ├── validar_cpf.py               # Validação oficial de CPF
│   ├── validar_email.py             # Função principal de email
│   ├── validar_email_basico.py      # Nível 1 — básico
│   ├── validar_email_regex.py       # Nível 2 — regex
│   └── validar_email_dns.py         # Nível 3 — DNS
└── tests/
    ├── __init__.py
    ├── test_validar_cpf.py
    ├── test_validar_email.py
    ├── test_api_cep.py
    └── test_cliente_service.py
```

---

## 🏗️ Arquitetura — MVC

O projeto segue o padrão **MVC (Model - View - Controller)**:

| Camada | Arquivo | Responsabilidade |
|---|---|---|
| View | `menu/` | Exibe opções e captura escolha do usuário |
| Controller | `controllers/` | Coleta input, trata erros e exibe mensagens |
| Service | `services/` | Lógica de negócio, validações e regras |
| Model | `models/` | Estrutura dos dados (Pessoa e Endereco) |
| Utils | `utils/` | Funções auxiliares reutilizáveis |

```
main.py → menu → controller → service → models/utils
```

Cada camada tem uma responsabilidade única e não sabe o que as outras fazem por dentro.

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- Biblioteca `requests`

---

## 📦 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/Danielautomate/cadastro-clientes-python.git

# 2. Entre na pasta do projeto
cd cadastro-clientes-python

# 3. Instale as dependências
pip install requests
```

---

## ▶️ Como executar

```bash
python main.py
```

O menu aparecerá no terminal:

```
==================================================
    SISTEMA DE CADASTRO DE CLIENTES
==================================================
  [1] Cadastrar novo cliente
  [2] Listar clientes
  [3] Buscar cliente por CPF
  [4] Atualizar cliente
  [5] Excluir cliente
  [0] Sair
==================================================
```

---

## ✅ Validações implementadas

### CPF — algoritmo oficial da Receita Federal
- Verifica se é string com 11 dígitos numéricos
- Remove pontos e traço automaticamente
- Rejeita CPFs com todos os dígitos iguais (ex: 111.111.111-11)
- Calcula e valida os **2 dígitos verificadores** pelo algoritmo oficial

### Email — 3 níveis de validação

| Nível | Função | O que verifica | Internet? |
|---|---|---|---|
| 1 | `validar_email_basico` | tem `@` e `.` no lugar certo | ❌ Não |
| 2 | `validar_email_regex` | formato completo com regex | ❌ Não |
| 3 | `validar_email_dns` | se o domínio existe na internet | ✅ Sim |

O sistema usa o **nível 2 por padrão**. O nível 3 pode ser ativado quando necessário.

### CEP
- Remove traço e espaços automaticamente
- Verifica se tem exatamente 8 dígitos numéricos
- Consulta a API ViaCEP com timeout de 5 segundos
- Trata erros de conexão e domínio inexistente

---

## 🧪 Testes

```bash
# Rodar todos os testes
python -m unittest discover tests -v

# Rodar arquivo específico
python -m unittest tests.test_validar_cpf -v
python -m unittest tests.test_validar_email -v
python -m unittest tests.test_api_cep -v
python -m unittest tests.test_cliente_service -v
```

Os testes usam `unittest.mock` para simular a API ViaCEP sem precisar de internet.

---

## 🔌 API utilizada

**ViaCEP** — API gratuita para consulta de CEPs brasileiros

```
https://viacep.com.br/ws/{cep}/json/
```

Retorna: logradouro, bairro, cidade (localidade) e estado (uf).

---

## 🛡️ Tratamento de erros

Todos os erros são capturados no controller e exibidos de forma amigável:

| Exceção | Quando acontece | Mensagem exibida |
|---|---|---|
| `ValueError` | CPF, email ou CEP inválido | `❌ Erro de validação: ...` |
| `ConnectionError` | sem internet ou timeout | `❌ Erro de conexão: ...` |
| `Exception` | qualquer outro erro | `❌ Erro inesperado: ...` |

---

## 📚 Conceitos aplicados

- Programação Orientada a Objetos (POO)
- Encapsulamento com atributos privados (`__atributo`)
- `@property` e `@setter` para acesso controlado
- Variável de classe para geração automática de ID
- Arquitetura em camadas MVC
- Tratamento de exceções com `try/except` específicos
- Requisições HTTP com `requests` e timeout
- Expressões regulares com `re`
- Consulta DNS com `socket`
- Testes unitários com `unittest`
- Mock de APIs com `unittest.mock`
- Dispatch table (dicionário de funções)
- `if __name__ == "__main__"` para proteção de execução

---

## 👨‍💻 Autor

Desenvolvido por **Daniel** como projeto de aprendizado em Python.

---

## 📄 Licença

Este projeto está sob a licença MIT.
