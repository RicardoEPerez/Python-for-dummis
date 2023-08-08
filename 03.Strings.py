#strings
mi_Str='ejemplo'
mi_Str_ej="otro ejemplo"

print(len(mi_Str))
print(len(mi_Str_ej))
print(mi_Str,mi_Str_ej)
mi_Str='TEXTO CON\nsalto de linea'
print(mi_Str)

mi_Str='TEXTO CON\ttabulation'
print(mi_Str)
#se pueden mezclar los tipos especiales

#*Formateo

name,lastname,age = 'nameless','last nameless' , 54
"""
! %s str
! %d int
! %f float
"""
print('Mi nombre es {} {} y mi edad es {}'.format(name,lastname,age))
print('Mi nombre es %s %s y mi edad es %d' %(name,lastname,age)) #* la mejor manera de hacerlo si se debe tener bien el formato de la variable
print(f'Mi nombre es {name} {lastname} y mi edad es {age}') # segunda mejor forma(no olvides la"f")