"""
-----------------------------------------------------------------------------------------------
Título: Sistema de colchones
Fecha:23/9/2024
Autor:Ezequiel Oliveto / Facundo Urban / Sofia Blanc / Milagros Hermansson / Juliana Rivas

Descripción:
Colchi es un sistema de gestión de inventario y sucursales para una empresa de colchones. 
Permite registrar, modificar y visualizar información de colchones y sucursales, así como 
realizar compras, ventas y cambios de precios. Incluye funcionalidades para la gestión de stock y 
administración de sucursales de manera eficiente.

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

# [1]
def verMatriz(matriz):
    for fila in matriz:
        print(fila)

# [2]
def verInformacionSobreLosColchones(colchones):
    opciones=len(colchones)+1
    while True:
                print()
                print("---------------------------")
                print("MENÚ DE LOS COLCHONES      ")
                print("---------------------------")
                print("[ 0 ] Toda la informacion de los modelos de colchones")
                for elem in colchones: 
                    print("[",elem,"]","Toda la informacion de los modelos de",colchones[elem]["Modelo"])
                print("---------------------------")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    if opcion!="0":
                        print(colchones[opcion])
                        break
                    else:
                        for op in colchones.items():
                            print(op)
                        
                
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                
                print()

# [3]
def verInformacionSobreLasSucursales(sucursales):
    opciones=len(sucursales)+1
    while True:
        print()
        print("---------------------------")
        print("MENÚ DE LAS SUCURSALES     ")
        print("---------------------------")
        print("[ 0 ] Toda la informacion de las sucursales")
        for elem in sucursales: 
            print("[",elem,"]","Toda la informacion de los modelos de",sucursales[elem]["Sucursal"])
        print("---------------------------")
        print()

                
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            if opcion!="0":
                print(sucursales[opcion])
                break
            else:
                print(sucursales)
                    
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

# [4]
def añadirColchonesAlStock():
    ...

# [5]
def eliminarColchonesDelStock():
    ...

# [6]
def cambiarPrecioColchon():
    ...

# [7]
def eliminarModelosDeColchones(colchones):
    opciones=len(colchones)+1
    while True:
        print()
        print("---------------------------------------------")
        print("MENÚ PARA ELIMINAR UN MODELO DE COLCHON      ")
        print("---------------------------------------------")
        for elem in colchones: 
            print("[",elem,"]",colchones[elem]["Modelo"])
        print("---------------------------")
        print()
                
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            print()
            print()
            print("Se a eliminado la ",colchones[opcion]["Modelo"])
            del colchones [(opcion)]
            print()
            print()
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

# [8]
def eliminarSucursales(sucursales):
    opciones=len(sucursales)+1
    while True:
        print()
        print("---------------------------------------")
        print("MENÚ PARA ELIMINAR UN SUCURSAL         ")
        print("---------------------------------------")
        for elem in sucursales: 
            print("[",elem,"]",sucursales[elem]["Sucursal"])
        print("---------------------------")
        print()
                
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            print()
            print()
            print("Se a eliminado la ",sucursales[opcion]["Sucursal"])
            del sucursales [(opcion)]
            print()
            print()
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

# [9]
def preguntarPrecioColchones(): 
    ...

# [10]
def añadirNuevosModelosDeColchones():
    ...

# [11]
def añadirNuevasSucursal(nombreSucursal,direccionSucursal,stockMaximoSucursal):
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







    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():

    colchones = {
    "1": {
        "Modelo": "Colchones de muelles",
        "Precio": "$400.000",
        "Medidas": "200x150 cm"
    },
    "2": {
        "Modelo": "Colchones de espuma",
        "Precio": "$600.000",
        "Medidas": "190x140 cm"
    },
    "3": {
        "Modelo": "Colchones de espuma viscoelástica",
        "Precio": "$500.000",
        "Medidas": "200x160 cm"
    },
    "4": {
        "Modelo": "Colchones híbridos",
        "Precio": "$400.000",
        "Medidas": "200x180 cm"
    },
    "5": {
        "Modelo": "Colchones de látex",
        "Precio": "$600.000",
        "Medidas": "190x120 cm"
    },
    "6": {
        "Modelo": "Colchones ortopédicos",
        "Precio": "$800.000",
        "Medidas": "210x180 cm"
    },
    "7": {
        "Modelo": "Colchones hinchables",
        "Precio": "$200.000",
        "Medidas": "180x120 cm"
    }
}


    sucursales = {
    "1": {
        "Sucursal": "Sucursal Central",
        "Direccion": "Libertad 330",
        "Stock Maximo": 500
    }, 
    "2": {
        "Sucursal": "Sucursal Norte",
        "Direccion": "Rivadavia 450",
        "Stock Maximo": 300
    }, 
    "3": {
        "Sucursal": "Sucursal Sur",
        "Direccion": "San Martín 120",
        "Stock Maximo": 400
    }, 
    "4": {
        "Sucursal": "Sucursal Este",
        "Direccion": "Belgrano 890",
        "Stock Maximo": 100
    }, 
    "5": {
        "Sucursal": "Sucursal Oeste",
        "Direccion": "Mitre 230",
        "Stock Maximo": 150
    }, 
    "6": {
        "Sucursal": "Sucursal Plaza",
        "Direccion": "Sarmiento 670",
        "Stock Maximo": 300
    }, 
    "7": {
        "Sucursal": "Sucursal Mercado",
        "Direccion": "Moreno 520",
        "Stock Maximo": 200
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


    
    #-------------------------------------------------------------------------------------------------------------------------------------
    while True:
        opciones = 11+1
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
            print("[10] Añadir nuevos modelos de colchones")
            print("[11] Añadir nuevas sucursal ")
            print("---------------------------")
            
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
        
        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        



        elif opcion == "1":
            verMatriz(matriz)


        elif opcion == "2":
            verInformacionSobreLosColchones(colchones)


        elif opcion == "3":
            verInformacionSobreLasSucursales(sucursales)
            

        elif opcion == "4":   
            añadirColchonesAlStock()
        

        elif opcion == "5":   
            eliminarColchonesDelStock()


        elif opcion == "6":   
            cambiarPrecioColchon()


        elif opcion == "7":   
            eliminarModelosDeColchones(colchones)

            
        elif opcion == "8":   
            eliminarSucursales(sucursales)


        elif opcion == "9":   
            preguntarPrecioColchones()


        elif opcion == "10":  
            añadirNuevosModelosDeColchones()


        elif opcion == "11":  
            añadirNuevasSucursal(nombreSucursal,direccionSucursal,stockMaximoSucursal)


        input("\nPresione ENTER para volver al menú.")
        print("\n\n")



# Punto de entrada al programa
main()

