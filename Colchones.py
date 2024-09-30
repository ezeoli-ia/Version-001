"""
-----------------------------------------------------------------------------------------------
Título: Sistema de colchones
Fecha:23/9/2024
Autor:Ezequiel Oliveto / Facundo Urban / Sofia Blanc / Milagros Hermansson / Juliana Rivas

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


def comprarVentaDeColchones():

    return


def añadirYEliminarStock():
    #Esta funcion permite sumar un numero en una fila(sucursal) y columna(modelo) en la matriz que hace referencia al stock.

    return

def añadirNuevosModelosDeColchones():
    #Mili y Juli
    # Esta funcion recibira el modelo y los datos del colchon que se quiere añadir al diccionario.

    return

def añadirNuevasSucursales(nombreSucursal,direccionSucursal,stockMaximoSucursal):
    # Esta funcion recibira numero de sucursal, nombre, direccion y stock maximo. Agregara a el diccionario 
    # "sucursales" los datos.
    # Crear un diccionario interno con la información de la sucursal
    DiccSucursales=sucursales()
    sucursalInfo={
        "nombre":nombreSucursal,
        "direccion":direccionSucursal,
        "stockMaximo":stockMaximoSucursal,
        
    }
    numeroSucursal = len(DiccSucursales) + 1
    # Agregar el diccionario interno al diccionario externo
    DiccSucursales["Sucursal"+numeroSucursal] = sucursalInfo
    
    """
    nombreSucursal=input("Ingrese el nombre de la sucursal nueva: ")
    direccionSucursal=input("Ingrese la dirección de la nueva sucursal: ")
    stockMaximoSucursal=int(input("Ingese el stock maximo de la sucursal nueva: "))
    
    crearSucursal(nombreSucursal,direccionSucursal,stockMaximoSucursal)
    """

    return

def eliminarModelosDeColchones():
    #Esta funcion recibira los datos que se quieran eleminar de la matriz.
    
    return

def eliminarSucursales():
    #Esta funcion recibira los datos que se quieran eleminar de la matriz.
    
    return

def preguntarPrecioColchones(): 
    #Esta funcion permite ver el precio de cada modelo de colchon
    
    return

def cambiarPrecioColchon():
    #Esta funcion hace posible cambiar el precio a cualquier modelo de colchon

    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    
    matriz = [
    [" ", "Colchones de muelles", "Colchones de espuma", "Colchones de espuma viscoelástica", "Colchones híbridos", "Colchones de látex", "Colchones ortopédicos", "Colchones hinchables"],
    ["Sucursal Central", 1, 1, 1, 1, 1, 1, 1],
    ["Sucursal Norte", 1, 1, 1, 1, 1, 1, 1],
    ["Sucursal Sur", 1, 1, 1, 1, 1, 1, 1],
    ["Sucursal Este", 1, 1, 1, 1, 1, 1, 1],
    ["Sucursal Oeste", 1, 1, 1, 1, 1, 1, 1, 1],
    ["Sucursal Plaza", 1, 1, 1, 1, 1, 1, 1],
    ["Sucursal Mercado", 1, 1, 1, 1, 1, 1, 1],
]

    colchones = {
    "1":{
        "Modelo":"Colchones de muelles",
        "Precio":"$400000",
    },
    "2":{
        "Modelo":"Colchones de espuma",
        "Precio":"$600000"
    },
     "3":{
        "Modelo":"Colchones de espuma viscoelástica",
        "Precio":"$500000"
    }
    ,
     "4":{
        "Modelo":"Colchones híbridos",
        "Precio":"$400000"
    }
    ,
     "5":{
        "Modelo":"Colchones de látex",
        "Precio":"$600000"
    }
    ,
     "6":{
        "Modelo":"Colchones ortopédicos",
        "Precio":"$800000"
    }
    ,
     "7":{
        "Modelo":"Colchones hinchables",
        "Precio":"$200000"
    }
    }

    sucursales = {
    "1": {
        "nombre": "Sucursal Central",
        "direccion": "Libertad 330",
        "stock Maximo": 500
    }, 
    "2": {
        "nombre": "Sucursal Norte",
        "direccion": "Rivadavia 450",
        "stock Maximo": 300
    }, 
    "3": {
        "nombre": "Sucursal Sur",
        "direccion": "San Martín 120",
        "stock Maximo": 400
    }, 
    "4": {
        "nombre": "Sucursal Este",
        "direccion": "Belgrano 890",
        "stock Maximo": 100
    }, 
    "5": {
        "nombre": "Sucursal Oeste",
        "direccion": "Mitre 230",
        "stock Maximo": 150
    }, 
    "6": {
        "nombre": "Sucursal Plaza",
        "direccion": "Sarmiento 670",
        "stock Maximo": 300
    }, 
    "7": {
        "nombre": "Sucursal Mercado",
        "direccion": "Moreno 520",
        "stock Maximo": 200
    }
}
    
    stock = {
        "1":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        },
        "2":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        },
        "3":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        },
        "4":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        },
        "5":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        },
        "6":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        },
        "7":{
            "Colchones de muelles":100,
            "Colchones de espuma":150,
            "Colchones de espuma viscoelástica":200,
            "Colchones híbridos":100,
            "Colchones de látex":140,
            "Colchones ortopédicos":300,
            "Colchones hinchables":240,
        }
        }
    #-------------------------------------------------------------------------------------------------------------------------------------
    while True:
        opciones = 8
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Ver Matriz")
            print("[2] Ver informacion sobre los colchones")
            print("[3] Ver informacion sobre las sucursales")
            print("[4] Añadir colchones al stock")
            print("[5] Eliminar colchones del stock")
            print("[6] Cambiar precio de los colchones")
            print("[7] Eliminar modelo de colchon")
            print("[8] Eliminar sucursal")
            print("[9] Ver lista de precios")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys
        
        elif opcion == "1":
            for fila in matriz:
                print(fila)

        elif opcion == "2": 
            while True:
                print()
                print("---------------------------")
                print("MENÚ DE LOS COLCHONES      ")
                print("---------------------------")
                print("[0] Toda la informacion de los modelos de colchones")
                print("[1] Informacion sobre los colchones de muelles")
                print("[2] Informacion sobre los colchones de espuma")
                print("[3] Informacion sobre los colchones de espuma viscoelástica")
                print("[4] Informacion sobre los colchones híbridos")
                print("[5] Informacion sobre los colchones látex")
                print("[6] Informacion sobre los colchones ortopédicos")
                print("[7] Informacion sobre los colchones hinchables")
                print("---------------------------")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    if opcion!="0":
                        print(colchones[opcion])
                    else:
                        print(colchones)
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

        elif opcion == "3":
   
            while True:
                print()
                print("---------------------------")
                print("MENÚ DE LAS SUCURSALES     ")
                print("---------------------------")
                print("[0] Toda la informacion de las sucursales")
                print("[1] Informacion sobre la Sucursal Central")
                print("[2] Informacion sobre la Sucursal Norte")
                print("[3] Informacion sobre la Sucursal Sur")
                print("[4] Informacion sobre la Sucursal Este")
                print("[5] Informacion sobre la Sucursal Oeste")
                print("[6] Informacion sobre la Sucursal Plaza")
                print("[7] Informacion sobre la Sucursal Mercado")
                print("---------------------------")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    if opcion!="0":
                        print(sucursales[opcion])
                    else:
                        print(colchones)

                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
        elif opcion == "4":   
            ...
        
        elif opcion == "5":   
            ...

        elif opcion == "6":   
            ...

        elif opcion == "7":   
            ...

        elif opcion == "8":   
            ...

        elif opcion == "9":   
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")



# Punto de entrada al programa
main()

