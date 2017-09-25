# pythonViaCEP
Classe que retorna o endereço a partir do CEP via JSON(API)

exemplo:
n = rcep('06622640')

print(n['cep'])
print(n['logradouro'])
print(n['complemento'])
print(n['bairro'])
print(n['localidade'])
print(n['uf'])
print(n['unidade'])

