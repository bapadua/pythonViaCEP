import requests
import json


class rcep():
    def __init__(self, cep):
        self.cep = str(cep)
        self.url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
        re = self.requisicao()
        self.logradouro = re['logradouro']
        self.cep = re['cep']
        self.complemento = re['complemento']
        self.bairro = re['bairro']
        self.localidade = re['localidade']
        self.uf = re['uf']
        self.unidade = re['unidade']
    def getUrl(self):
        return self.url

    def requisicao(self):
        try:
            req = requests.get(self.url)
            dic = json.loads(req.text)
            return dic
        except Exception as e:
            print('Erro: ', e)
            exit()

