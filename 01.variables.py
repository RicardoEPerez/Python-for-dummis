# las variables se deben poner en minúsculas o con snake_case
mi_Var_Str = 'mi variable'
print(mi_Var_Str)

mi_Var_Int = 0
print(mi_Var_Int)

mi_Var_Bool = True
print(mi_Var_Bool)

#! para concatenar es con "," y print convierte a todo en algo que pueda imprimirlo de forma automática
print(mi_Var_Str,mi_Var_Int,mi_Var_Bool,"alv")

# * para convertir int a str se usa la función "str()"
mi_Var_Int_to_Str = str(mi_Var_Int)
print(type(mi_Var_Int_to_Str))

# Funciones del sistema
#* len() da el tamaño de la cadena (solo str) 
print(len(mi_Var_Str))


#* variables en una sola linea
# no se recomienda mucho, complica el mantenimiento del código
name , lastname, nickname, age= 'rice' , 'cook', 'cookie', 123
print('mi llamar',name , lastname, 'me conocen como' ,nickname, 'mi edad' ,age)

#convertir un int a float
int_Var = float(5)
print(int_Var)

#! para que una variable "no cambie" su tipo se indica cual se va a usar (pero solo sirve para indicar de forma visual no forzamos nada)
dire: str ='mi dirección'
dire = 32
print(type(dire))