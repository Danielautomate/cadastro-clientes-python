
import requests



def busca_endereco_por_cep(cep: str):
    cep = cep.replace("-", "").strip()

    if len(cep) != 8:
        raise ValueError("CEP Inválido")
    

    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(url)

        if resposta.status_code != 200:
            raise Exception("Erro ao consulta CEP")
        
        dados = resposta.json()

        if "erro" in dados:
            raise ValueError("CEP não enconcotrado")
        
        return{
            "logradouro": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf"),

        }
    

    except requests.exceptions.RequestException:
        raise ConnectionAbortedError("Erro de conexão com API de CEP")