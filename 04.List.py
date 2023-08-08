# Listas

mi_lista = list()
mi_otra_lista = []
# * ambos son lista no importa que uno parezca array

print(len(mi_lista))
print(type(mi_lista))
print(len(mi_otra_lista))
print(type(mi_otra_lista))

mi_lista = [35, 15, 35, 12, 48, 35, 15, 21]

print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [35, 1.72, 'Ricardo', 'Ardilla']
print(mi_otra_lista)

print(mi_otra_lista[0])  # * asi es como se accede a un dato en especifico
print(mi_otra_lista[1])  # * asi es como se accede a un dato en especifico
# * asi es como se accede a un dato en especifico (se puede de el ultimo lugar al primero [se empieza desde -1])
print(mi_otra_lista[-1])
print(mi_lista.count(15))
print(type(mi_otra_lista[2]))  # * si respeta el tipo de dato en lugar

# añadir elemento al final
mi_otra_lista.append('BocchiDev')
print(mi_otra_lista)

# añadir elemento donde quiera
mi_otra_lista.insert(1, 'camello')
print(mi_otra_lista)

mi_otra_lista[1] = 'rata'  # *editar elemento a voluntad
print(mi_otra_lista)


# eliminar elemento (el primero que coincida)
mi_otra_lista.remove('rata')
print(mi_otra_lista)
mi_lista.remove(15)
print(mi_lista)


print(mi_lista.pop())  # * quita la ultima posición, pero la puede retornar
print(mi_lista.pop(2))  # * se puede colocar el indice a quitar
print(mi_lista)

del mi_lista[2]  # * para eliminar el elemento por su ubicación
print(mi_lista)

mi_nueva_lista = mi_lista.copy()  # *copiar lista
mi_lista.clear()  # *vaciar lista
print(mi_lista)
print(mi_nueva_lista)

# invierte el order
mi_nueva_lista.reverse()
print(mi_nueva_lista)

# ordenar
# * se le pueden poner multiples parámetros de forma predeterminada usa el orden alfabético/numérico
mi_nueva_lista.sort()
print(mi_nueva_lista)

# Sub-listas
print(mi_nueva_lista[0:2])
