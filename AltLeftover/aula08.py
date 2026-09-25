'''
Tuplas
'''

#declaração
tuple_a = (110, 205, 202, 410, 110)

print(tuple_a[2])

#tuple_a[2] = 10 - ERROR

for i in tuple_a:
    print(i)

for i, v in enumerate(tuple_a):
    print(f'{i}: {v}')

#métodos
print(tuple_a.count(110))

print(tuple_a.index(110))

tuple_array = (
    ['Davi', 'João', 'Rafael', 'Ana'],
    [100, 200, 300, 400],
    ('a', 'b', 'c')
)

print(tuple_array[0])

tuple_array[0][2] = 'Rafaela'

print(tuple_array[0])

list_a = [100, 200, 300, 400]
tuple_lista_a = tuple(list_a)
list_tuple_a = list(tuple_array)

#conversão de estruturas
#converter uma tupla para uma lista
tuple_sal = (1100, 5200, 3500, 4500)
print(tuple_sal.__dir__, ' ', tuple_sal)

list_aux = list(tuple_sal)

list_aux.append(4500)

tuple_sal = tuple(list_aux)
print(tuple_sal.__dir__, ' ', tuple_sal)



