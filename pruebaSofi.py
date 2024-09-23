"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:TP04-10 | PALABRAS DE FRASE ORDENADAS
Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas 
por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre 
cada una

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS y DICCIONARIOS



#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
def precioColchones():
    for Modelo, Precio in diccColchones.items():
        print(Modelo, Precio)
    
   
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    diccColchones = {
    "Colchon1":{
        "Modelo":"SIG",
        "Precio":"$40000",
    },
    "Colchon2":{
        "Modelo":"FGS",
        "Precio":"$60000"
    },
     "Colchon3":{
        "Modelo":"FGS",
        "Precio":"$60000"
    }
    }   
    precioColchones(diccColchones)


# Punto de entrada al programa
main()
