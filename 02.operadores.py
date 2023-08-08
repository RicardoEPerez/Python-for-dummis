# operadores aritméticos

print(3 + 4)  # suma
print(3 - 4)  # resta
print(3 * 4)  # multiplicación
print(3 / 4)  # division
print(35 % 4)  # cociente
print(357 // 4)  # Floor división = es para aproximar siempre aun entero
print(357 / 4)
print(3 * 4)  # exponente

print(((2**3)+3-(7/1))//4)

# *Plus también puede concatenar(no mete los espacios en automático), pero no se pueden mezclar tipos diferentes
print('hola'+'python')
print('hola'+str(5))

# * Forma de multiplicar los str, solo se puedo con números enteros(no importa que tenga operaciones si solo da int)
print('alv ' * 10)


# operadores comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(35 == 4)
print(357 != 4)

# *se pueden compara cadenas de texto lo que compara es la posición en orden alfabético (mas cerca de la "a" mas valor(las mayusculas van despues de la z) y es sumatoria)
print('aa' > 'AAA')  # alfabético por ASCII
print(len('aa') > len('AAA'))  # por cantidad de caracteres

# *Operadores lógicos
print(3 > 4 and 'hola' > 'python')
print(3 > 4 or 'hola' > 'python')
print(3 < 4 and 'hola' < 'python')
print('lógicos', 3 < 4 or 'hola' > 'python')
# print(3>4 not 'hola'>'python') #not no se usa asi
print(not (3 > 4))  # el not invierte el resultado ("true=false", "false=true")
