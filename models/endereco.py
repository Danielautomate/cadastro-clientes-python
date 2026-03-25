

class Endereco:
    def __init__(self, cep: str, rua: str, numero: str, bairro: str, cidade: str, estado: str) -> None:
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado



    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}, {self.estado} - CEP: {self.cep}"



