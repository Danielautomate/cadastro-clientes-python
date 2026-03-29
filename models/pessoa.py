from datetime import date
from models.endereco import Endereco



class Pessoa:
    
    contador: int = 0

    def __init__(self, nome: str, data_nascimento: str, cpf:str, endereco: Endereco | None, cep: str, email: str) -> None:
        Pessoa.contador += 1

        self.__codigo = Pessoa.contador
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__cep = cep
        self.__endereco = endereco
        self.__email = email

        self.__data_cadstro = date.today()


# ======================
#     PROPERTIES
# ======================

    @property
    def codigo(self) -> int:
        return self.__codigo


    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
   
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novo_email: str):
        self.__email = novo_email
    
    @property
    def cep(self) -> str:
        return self.__cep

    @cep.setter
    def cep(self, novo_cep: str):
        self.__cep = novo_cep
    
    @property
    def endereco(self) -> Endereco | None:
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco: Endereco):
        self.__endereco = novo_endereco
    
    @property 
    def data_cadastro(self) -> date:
        return self.__data_cadastro


# ======================
# MÉTODO STRING
# ======================
    
    def __str__(self) -> str:

        endereco_str = ""

        if self.__endereco:
            endereco_str = str(self.__endereco)

        return (
            f"Código:           {self.__codigo}\n"
            f"Nome:             {self.__nome}\n"
            f"CPF:              {self.__cpf}\n"
            f"Data Nascimento:  {self.__data_nascimento}\n"
            f"Email:            {self.__email}\n"
            f"Data Cadastro:    {self.__data_cadastro}\n"
            f"Endereço:         {endereco_str}\n"
        )
     