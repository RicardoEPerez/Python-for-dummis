# set
#!Los set no son una estructura ordenada, son realmente un hash para el almacenamiento
mi_set = set()
print(type(mi_set))

mi_otro_set = {}
print(type(mi_otro_set))  # * inicialmente es un diccionario

# *Se a convertido en un set (eso lo cambia dependiendo de como se llene la información)
mi_otro_set = {"gato", 'azul', 125}
print(type(mi_otro_set))
print(len(mi_otro_set))

# print(mi_otro_set[2])#* no se puede acceder a datos específicos

mi_otro_set.add('ardilla')
print(mi_otro_set)

# no guarda repetidos
mi_otro_set.add('ardilla')
print(mi_otro_set)

# forma de buscar un dato en el set (retorna un bool)
print('ardilla' in mi_otro_set)
print('rojo' in mi_otro_set)

# Permite eliminar datos poniendo el dato en concreto
mi_otro_set.remove('gato')
print(mi_otro_set)

# vaciar el set
mi_otro_set.clear()
print(mi_otro_set)

# Convertir set a list
mi_set = {"gato", 'azul', 125}
mi_list = list(mi_set)
print(mi_list)
# !Esto no se recomienda ya que nunca se sabe en que posición van a quedar los elementos
print(type(mi_list))

mi_otro_set = {'java', 'js', 'python'}

mi_nuevo_set = mi_otro_set.union(mi_set)  # * unir 2 set diferentes
print(mi_nuevo_set)
#* los union ignoran los repetidos

print(mi_nuevo_set.difference(mi_set))