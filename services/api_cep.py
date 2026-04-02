
import requests



def busca_endereco_por_cep(cep: str) -> dict:
    
    cep = cep.replace("-", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("CEP inválido: deve conter exatamente 8 números")
    

    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"

         # ------------------------------------------------------
            # MELHORIA: timeout=5 define que se a API não responder
            # em 5 segundos, lança uma exceção automaticamente.
            # Sem timeout, o programa pode travar esperando para sempre.
        # ------------------------------------------------------
       
        resposta = requests.get(url, timeout=5)

        # ------------------------------------------------------
        # status_code é o código de resposta HTTP.
        # 200 = sucesso. Outros exemplos:
        #   404 = não encontrado
        #   500 = erro no servidor
        # Se não for 200, algo deu errado no servidor da API.
        # ------------------------------------------------------

        if resposta.status_code != 200:
            raise Exception("Erro ao consultar a API de CEP")
        
        dados = resposta.json()

        if "erro" in dados:
            raise ValueError("CEP não encontrado")
        
        return{
            "cep": cep,
            "logradouro": dados.get("logradouro", ""),
            "bairro": dados.get("bairro", ""),
            "cidade": dados.get("localidade",""),
            "estado": dados.get("uf"),

        }
    
    except requests.exceptions.Timeout:
        raise ConnectionError("A API de CEP demorou demais para responder")

    except requests.exceptions.ConnectionError:
        raise ConnectionError("Sem conexão com a internet")

    except requests.exceptions.RequestException:
        raise ConnectionError("Erro de conexão com API de CEP")