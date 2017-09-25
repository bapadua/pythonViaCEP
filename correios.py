class rcep():
    def __init__(self, cep):
        self.cep = str(cep)
        self.url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
        re = self.requisicao()
        self.logradouro = re['logradouro']
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
