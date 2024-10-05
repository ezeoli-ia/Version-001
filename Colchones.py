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
# [0]
def crearMatriz(colchones,sucursales,stock):
    matriz=[]
    for f in range(len(sucursales)+1):
        if f !=0:
            matriz.append([sucursales[str(f)]["Sucursal"]])
        else:
            matriz.append([""])
        for c in range(len(colchones)):
            if f ==0:
                matriz[f].append(colchones[str(c+1)]["Modelo"])
            else:
                NO=colchones[str(c+1)]["Modelo"]
                matriz[f].append(stock[str(f)][NO])

    return matriz


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


    stock={
        #Sucursal Central
 '1': {'Colchones de muelles': 270,
       'Colchones de espuma': 510,
       'Colchones de espuma viscoelástica': 490,
       'Colchones híbridos': 430,
       'Colchones de látex': 50,
       'Colchones ortopédicos': 590,
       'Colchones hinchables': 370},

        ##Sucursal Norte
 '2': {'Colchones de muelles': 390,
       'Colchones de espuma': 200,
       'Colchones de espuma viscoelástica': 350,
       'Colchones híbridos': 270,
       'Colchones de látex': 110,
       'Colchones ortopédicos': 530,
       'Colchones hinchables': 60},

        #Sucursal Sur
 '3': {'Colchones de muelles': 340,
       'Colchones de espuma': 180,
       'Colchones de espuma viscoelástica': 550,
       'Colchones híbridos': 570,
       'Colchones de látex': 410,
       'Colchones ortopédicos': 520,
       'Colchones hinchables': 130},

        #Sucursal Este
 '4': {'Colchones de muelles': 470,
       'Colchones de espuma': 400,
       'Colchones de espuma viscoelástica': 520,
       'Colchones híbridos': 350,
       'Colchones de látex': 50,
       'Colchones ortopédicos': 490,
       'Colchones hinchables': 440},

        #Sucursal Oeste
 '5': {'Colchones de muelles': 150,
       'Colchones de espuma': 330,
       'Colchones de espuma viscoelástica': 360,
       'Colchones híbridos': 480,
       'Colchones de látex': 510,
       'Colchones ortopédicos': 150,
       'Colchones hinchables': 550},

        #Sucursal Plaza
 '6': {'Colchones de muelles': 590,
       'Colchones de espuma': 120,
       'Colchones de espuma viscoelástica': 30,
       'Colchones híbridos': 580,
       'Colchones de látex': 410,
       'Colchones ortopédicos': 270,
       'Colchones hinchables': 40},

        #Sucursal Mercado
 '7': {'Colchones de muelles': 380,
       'Colchones de espuma': 60,
       'Colchones de espuma viscoelástica': 390,
       'Colchones híbridos': 310,
       'Colchones de látex': 210,
       'Colchones ortopédicos': 290,
       'Colchones hinchables': 430}
    }
    
    
    matriz=crearMatriz(colchones,sucursales,stock)

 
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

