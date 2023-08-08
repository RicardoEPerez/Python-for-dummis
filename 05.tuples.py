# tuples/tupla
#!Son como listas chafas pero con la cualidad de se inmutables los datos internos

mi_tupla = tuple()
mi_otra_tupla = ()
print(type(mi_tupla))
print(type(mi_otra_tupla))

mi_tupla = (22, 1.72, 'Ricardo', 'batman')
print(mi_tupla[0])

print(mi_tupla.count('batman'))
print(mi_tupla.index('batman'))  # * indica en que lugar se encuentra el dato

# mi_tupla[1] = 1.85  # *va a tirar error, los tuplas son inmutables

mi_otra_tupla = (12, 35, 185, 65, 2.2)

la_wea = mi_otra_tupla + mi_tupla  # *se pueden sumar en una nueva tupla
print(la_wea)
print(type(la_wea))
