

class Endereco:
    def __init__(self, cep: str, rua: str, numero: str, bairro: str, cidade: str, estado: str) -> None:
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado




    # ----------------------------------------------------------
    # PROPERTY
    # ----------------------------------------------------------

    @property
    def cep(self) -> str:
        return self.__cep

    @property
    def rua(self) -> str:
        return self.__rua

    @property
    def numero(self) -> str:
        return self.__numero

    @property
    def bairro(self) -> str:
        return self.__bairro

    @property
    def cidade(self) -> str:
        return self.__cidade

    @property
    def estado(self) -> str:
        return self.__estado


    def __str__(self) -> str:
        return (
            f"{self.__rua}, {self.__numero} - "
            f"{self.__bairro}, {self.__cidade}/{self.__estado} "
            f"- CEP: {self.__cep}"
        )


