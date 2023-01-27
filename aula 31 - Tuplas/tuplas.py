#t1 = (1, 2, 3, 'a', 'BallChoke', 'RedBull')
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
t4 = (10, 20, 30) * 5
t3 = t1 + t2
t5 = 1, 2, 3, 4, 5
print(t1)
print(t1[3])
print(t1[2:])

print(t3)

t5 = list(t5)
t5[1] = 3000
print(t5)
for v in t1:
    print(v)
