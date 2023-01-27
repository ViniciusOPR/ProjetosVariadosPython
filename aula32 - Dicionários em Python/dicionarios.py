import copy

# d1 = {'chave1': 'valor da chave'}
d1 = dict(chave1='Valor da chave', chave2='Valor de outra chave')
d1['nova chave'] = 'valor da chave'

# As chaves precisam ser únicas

print(d1['chave1'])

d2 = {'str': 'valor', 123: 'Outro valor', (1, 2, 3, 4): 'tupla', }
d2['naoexiste'] = 'Agora existe'
if 'naoexiste' in d2:
    print(d2['naoexiste'])

# del d2['str']

print('str' in d2)
print('str' in d2.keys())
print('str' in d2.values())

print(len(d2))


if d2.get('str') is not None:
    print(d2.get('str'))


d2.update({'Nova_chave': 'valor'})
for k, v in d2.items():
    print(k, v)


clientes = {
    'cliente1': {
        'nome': 'luiz',
        'sobrenome': 'otávio',
    },

    'cliente2': {
        'nome': 'carol',
        'sobrenome': 'almeida',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['luiz', 'otavio']}
v = copy.deepcopy(d3)

v[1] = 'luiz'
v['d'][0] = 'Joãozinho'

print(d1)
print(v)

d3.pop(1)
d3.popitem()

d1.update(d2)
print(d3)
print(d1)