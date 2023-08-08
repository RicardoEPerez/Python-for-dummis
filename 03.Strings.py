# strings
mi_Str = 'ejemplo'
mi_Str_ej = "otro ejemplo"

print(len(mi_Str))
print(len(mi_Str_ej))
print(mi_Str, mi_Str_ej)
mi_Str = 'TEXTO CON\nsalto de linea'
print(mi_Str)

mi_Str = 'TEXTO CON\ttabulation'
print(mi_Str)
# se pueden mezclar los tipos especiales

# *Formateo

name, lastname, age = 'nameless', 'last nameless', 54
"""
! %s str
! %d int
! %f float
"""
print('Mi nombre es {} {} y mi edad es {}'.format(name, lastname, age))
# * la mejor manera de hacerlo si se debe tener bien el formato de la variable
print('Mi nombre es %s %s y mi edad es %d' % (name, lastname, age))
# segunda mejor forma(no olvides la"f")
print(f'Mi nombre es {name} {lastname} y mi edad es {age}')

# desempaquetado de caracteres
lenguaje = 'python'
# * Tienen que ser la misma cantidad de variable que los caracteres que va a desempaquetar
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Division(Slice)

# * corta y guarda la información en las posiciones marcadas pero menos uno en el valor final
len_Slice = lenguaje[1:3]
print(len_Slice)  # *Resultado = "yt"

len_Slice = lenguaje[1:]  # * del valor inicial hasta el final
print(len_Slice)  # * "ython"

# * Empieza del final al comienzo pero solo el carácter en la posición resultante
len_Slice = lenguaje[-2]
print(len_Slice)  # * o

# * Asigna el rango y evita los caracteres múltiplo del tercer valor
len_Slice = lenguaje[0:6:2]
print(len_Slice)  # * Pto

# Reverse
# * Solo invierte el texto (se tiene que iniciar desde -1)
rever_len = lenguaje[::-1]
print(rever_len)

# Funciones
print(lenguaje.capitalize())  # * Letra mayúscula inicial
print(lenguaje.upper())  # * Todo mayúsculas
print(lenguaje.lower())  # * Todo minúsculas
print(lenguaje.count('t'))  # * cuanta cuantas veces se repite un carácter

print(lenguaje.isnumeric())  # * te dice si es un numero el str
print('1'.isnumeric())

print(lenguaje.isupper())  # * te dice si esta en mayúsculas el str
print(lenguaje.islower())  # * te dice si esta en minúsculas el str

print(lenguaje.upper().isupper())  # * encadenando funciones

# * Te dice si empieza con algo el str (Cap sensible
print(lenguaje.startswith('py'))
