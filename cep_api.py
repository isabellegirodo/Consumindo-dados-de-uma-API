import requests

class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.verifica_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Cep inválido')
        
    def __str__(self):
        return self.formatar_cep()

    def verifica_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formatar_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def acessar_api(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        requisicao = requests.get(url)
        dados = requisicao.json()
        return f"{dados['logradouro']} | {dados['bairro']} | {dados['localidade']} | {dados['uf']}"
    