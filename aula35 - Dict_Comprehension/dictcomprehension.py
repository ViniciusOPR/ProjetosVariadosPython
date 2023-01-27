l1 = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]
# d1 = {x: y for x, y in l1}
d1 = dict(l1)
print(d1)

d2 = {x for x in range(5)}
print(d2, type(d2))

d3 = {f'chave_{x}': x**2 for x in range(5)}
print(d3, type(d3))
