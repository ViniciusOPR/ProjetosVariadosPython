"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend;
min, max
range
"""

lista = ['a', 'b', 'Casa', 'd', 10.87, 12]
print(lista)
print(lista[2])
print(lista[-1])
print(lista[0:3])
print(lista[0::2])


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1.extend(l2)
l2.append('b')
l2.insert(0, 'banana')


print(l1)
print(l2)
l2.pop()
del(l2[3:5])
print(l2)
print(max(l3))
print(min(l3))

l4 = list(range(0, 100, 5))
print(l4)

l5 = [1, 2, 3, 4, 5, 6, 7]
soma = 0
for valor in l5:
    soma = soma + valor
print(soma)

l6 = ['string', True, 10, 12.56]

for elem in l6:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

"""
secreto = 'Kratos'
digitados = []
chances = 3


while True:
    if chances <= 0:
        print('Você perdeu')

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra')
        continue
    digitados.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta')
    else:
        print(f'a letra "{letra}" NÃO existe na palavra secreta')
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)

    if secreto_temporario == secreto:
        print(f'Que legal, você ganhou!!! A palavra era: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
"""