a = lambda x, y: x * y
print(a(2, 2))

lista = [
    ['P1', 12],
    ['P2', 10],
    ['P3', 13],
    ['P4', 14],
    ['P5', 17],
    ['P6', 9],
]
print(lista)
lista.sort(key=lambda item: item[1])
print(lista)

# Outros códigos para ordenamento de listas

print(sorted(lista, key=lambda i: i[1], reverse=True))

