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

Los numeros siguen igual incluso si se borran
Los precios son iguales en todas las sucursales
Cuando cambias algo cambia, cambia en todas las sucursales (se elimina un modelo, se elimina en todas las sucursales)
No hay funcion para volver a habilitar lo que esta deshabilitado 
Hay funciones que terminan al poner 0

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
def verMatriz(colchones,sucursales,stock):
    matriz=[]
    for f in range(len(sucursales)+1):
        if f !=0 and sucursales[str(f)]["Sucursal"]:
            matriz.append([sucursales[str(f)]["Sucursal"]])
        else:
            matriz.append([""])
        for c in range(len(colchones)):
            if colchones[str(f)]["Status"] == True:
                if f ==0 and colchones[str(c+1)]["Modelo"]== True:
                    matriz[f].append(colchones[str(c+1)]["Modelo"])
                else:
                    NO=colchones[str(c+1)]["Modelo"]
                    matriz[f].append(stock[str(f)][NO])

    for fil in range(len(matriz)):
        print( )
        for col in range(len(matriz[0])):
            print(f"{str(matriz[fil][col]):>20s}",end = '')
            
# [2]
def verInformacionSobreLosColchones(colchones,stock):
    opciones=len(colchones)+1
    while True:
                print()
                print("---------------------------")
                print("MENÚ DE LOS COLCHONES      ")
                print("---------------------------")
                print("[ 0 ] Toda la informacion de los modelos de colchones")
                for elem in colchones: 
                    if colchones[str(elem)]["Status"] == True:
                        print("[",elem,"]","Toda la informacion de los modelos de",colchones[elem]["Modelo"])
                print("---------------------------")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    if opcion!="0":
                        if colchones[str(opcion)]["Status"] == True:
                            print( )
                            print("-------------------------" )
                            print("Modelo :",colchones[opcion]["Modelo"])
                            print("Precio :",colchones[opcion]["Precio"])
                            print("Medidas :",colchones[opcion]["Medidas"])
                            print("-------------------------" )
                            print( )
                            break
                        else:
                            print()
                            input("Opción inválida. Presione ENTER para volver a seleccionar.")
                    else:
                        for i in range(len(colchones)):
                            aux = str(i +1)
                            if colchones[str(aux)]["Status"] == True:
                                print( )
                                print("-------------------------" )
                                print("Modelo :",colchones[aux]["Modelo"])
                                print("Precio :",colchones[aux]["Precio"])
                                print("Medidas :",colchones[aux]["Medidas"])
                                print("-------------------------" )
                        break
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
            if sucursales[str(elem)]["Status"] == True:
                print("[",elem,"]","Toda la informacion de los modelos de",sucursales[elem]["Sucursal"])
        print("---------------------------")
        print()

                
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            if opcion!="0":
                if sucursales[str(opcion)]["Status"] == True: 
                    print( )
                    print("-------------------------" )
                    print(sucursales[opcion]["Sucursal"])
                    print("Direccion :",sucursales[opcion]["Direccion"])
                    print("Stock Maximo :",sucursales[opcion]["Stock Maximo"])
                    print("-------------------------" )
                    print( )
                    break
                else:
                    print()
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            else:
                for i in range(len(sucursales)):
                    aux = str(i +1)
                    if sucursales[str(aux)]["Status"] == True:
                        print( )
                        print("-------------------------" )
                        print(sucursales[aux]["Sucursal"])
                        print("Direccion :",sucursales[aux]["Direccion"])
                        print("Stock Maximo :",sucursales[aux]["Stock Maximo"])
                        print("-------------------------" )
                break      
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

# [4]
def añadirColchonesAlStock(colchones, sucursales, stock):
    opciones=len(sucursales)+1
    print()
    print()
    while True:
        print("---------------------------")
        print("Sucursales disponibles:")
        print("---------------------------")

        #

        for sucursal_id, sucursal_info in sucursales.items():
            print("[ " + sucursal_id + " ] " + sucursal_info['Sucursal'])
        print("---------------------------")
        
        print()
        print( )
        sucursal_elegida = input("Seleccione el número de la sucursal donde desea agregar colchones: ")
        print()
        print()

        if sucursal_elegida in sucursales:
            print("Ha seleccionado la " + sucursales[sucursal_elegida]['Sucursal'] + ".")
            print()
            print()
            break  # Sale del bucle si la sucursal es válida
        else:
            print()
            print()
            print("Opción inválida. Por favor, elija un número de sucursal válido.")
            print()
            print()
            print()
            print()

    while True:
        print("---------------------------")
        print("Modelos de colchones disponibles:")
        print("---------------------------")
        for colchon_id, colchon_info in colchones.items():
            print("[ " + colchon_id + " ] " + colchon_info['Modelo'])
        print("---------------------------")
        print()
        colchon_elegido = input("Seleccione el número del colchón que desea agregar al stock: ")

        if colchon_elegido in colchones:
            print()
            print("Ha seleccionado el modelo " + colchones[colchon_elegido]['Modelo'] + ".")
            break  # Sale del bucle si el colchón es válido
        else:
            print()
            print()
            print("Opción inválida. Por favor, elija un número de colchón válido.")
            print()
            print()
            
    while True:
        print()
        print()
        cantidad = input("¿Cuántos colchones desea agregar al stock? ")

        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        else:
            print()
            print()
            print("Debe ingresar un número válido mayor a 0.")
            
    # Actualizar el stock
    stock[sucursal_elegida][colchones[colchon_elegido]["Modelo"]] += cantidad
    print()
    print("Se han agregado " + str(cantidad) + " colchones del modelo " + colchones[colchon_elegido]['Modelo'] + " al stock de la " + sucursales[sucursal_elegida]['Sucursal'] + ".") 
    print()

# [5]
def eliminarColchonesDelStock(colchones, sucursales, stock):
    while True:
        print()
        print("---------------------------")
        print("MENÚ PARA ELIMINAR COLCHONES DEL STOCK")
        print("---------------------------")
        
        # Mostrar las sucursales
        for sucursal in sucursales:
            print(f"[{sucursal}] {sucursales[sucursal]['Sucursal']}")
        print("---------------------------")

        sucursal_opcion = input("Seleccione una sucursal: ")

        if sucursal_opcion in sucursales:
            print()
            print()
            print()
            print(f"Sucursal seleccionada: {sucursales[sucursal_opcion]['Sucursal']}")
            print("---------------------------")
            # Mostrar los colchones disponibles en esa sucursal
            for colchon in colchones:
                print(f"[{colchon}] {colchones[colchon]['Modelo']} - Stock: {stock[sucursal_opcion][colchones[colchon]['Modelo']]}")
            print("---------------------------")
            print()
            colchon_opcion = input("Seleccione un colchón para eliminar del stock: ")

            if colchon_opcion in colchones:
                print()
                cantidad = int(input(f"¿Cuántos {colchones[colchon_opcion]['Modelo']} desea eliminar?: "))
                print()
                if cantidad <= stock[sucursal_opcion][colchones[colchon_opcion]['Modelo']]:
                    # Restar la cantidad del stock
                    stock[sucursal_opcion][colchones[colchon_opcion]['Modelo']] -= cantidad
                    print(f"Se han eliminado {cantidad} colchones de {colchones[colchon_opcion]['Modelo']} del stock de {sucursales[sucursal_opcion]['Sucursal']}.")
                else:
                    print("Error: No hay suficientes colchones en stock para eliminar esa cantidad.")
                break
            else:
                print("Opción inválida. Por favor, seleccione un colchón válido.")
        else:
            print()
            print("Opción inválida. Por favor, seleccione una sucursal válida.")

# [6]
def cambiarPrecioColchon(colchones):
    # Mostrar todos los colchones disponibles
    print()
    print()
    print("Colchones disponibles:")
    print("-----------------------")
    for key, colchon in colchones.items():
        print(f"{key}. {colchon['Modelo']} - Precio: {colchon['Precio']}")
        print("            -            ")
    
    # Seleccionar el colchón que se desea modificar
    print()
    print()
    colchon_id = input("Elige el número del colchón que deseas modificar: ")
    
    if colchon_id in colchones:
        # Mostrar el colchón seleccionado
        colchon_seleccionado = colchones[colchon_id]
        print(f"\nHas seleccionado: {colchon_seleccionado['Modelo']} - Precio actual: {colchon_seleccionado['Precio']}")
        
        # Pedir el nuevo precio
        print()
        nuevo_precio = input("Introduce el nuevo precio: $")
        
        # Actualizar el precio en el diccionario
        colchones[colchon_id]["Precio"] = (f"${nuevo_precio}")
        print()
        print(f"\nEl precio del {colchon_seleccionado['Modelo']} ha sido actualizado a ${nuevo_precio}.")
    else:
        print()
        print("ID de colchón no válido.")
    
    return colchones

# [7]
def eliminarModelosDeColchones(colchones):
    opciones=len(colchones)+1
    while True:
        print()
        print("---------------------------------------------")
        print("MENÚ PARA ELIMINAR UN MODELO DE COLCHON      ")
        print("---------------------------------------------")
        for elem in colchones:
            if colchones[str(elem)]["Status"] == True:
                print("[",elem,"]",colchones[elem]["Modelo"])
        print("---------------------------")
        print()
                
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            print()
            print()
            if colchones[str(opcion)]["Status"] == True: 
                print("Se a eliminado el modelo",colchones[opcion]["Modelo"],"en todas las sucursales")
                colchones [opcion]["Status"] = False
                print()
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                print()
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
            if sucursales[str(elem)]["Status"] == True:
                print("[",elem,"]",sucursales[elem]["Sucursal"])
        print("---------------------------")
        print()
                
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            print()
            print()
            if sucursales[str(opcion)]["Status"] == True: 
                print("Se a eliminado la",sucursales[opcion]["Sucursal"])
                sucursales[opcion]["Status"] = False
                print()
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                print()
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

# [9]
def preguntarPrecioColchones(colchones): 
    precios = {}
    for clave, valor in colchones.items():
        modelo = valor["Modelo"]
        precio = valor["Precio"]
        precios[modelo] = precio
    print(precios) 

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



# Agregar una funcion de fuera de linea (False)?



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():

    colchones = {
    "1": {
        "Status" : False,
        "Modelo": "Colchones de muelles",
        "Precio": "$400.000",
        "Medidas": "200x150 cm"
    },
    "2": {
        "Status" : False,
        "Modelo": "Colchones de espuma",
        "Precio": "$600.000",
        "Medidas": "190x140 cm"
    },
    "3": {
        "Status" : True,
        "Modelo": "Colchones de espuma viscoelástica",
        "Precio": "$500.000",
        "Medidas": "200x160 cm"
    },
    "4": {
        "Status" : True,
        "Modelo": "Colchones híbridos",
        "Precio": "$400.000",
        "Medidas": "200x180 cm"
    },
    "5": {
        "Status" : True,
        "Modelo": "Colchones de látex",
        "Precio": "$600.000",
        "Medidas": "190x120 cm"
    },
    "6": {
        "Status" : True,
        "Modelo": "Colchones ortopédicos",
        "Precio": "$800.000",
        "Medidas": "210x180 cm"
    },
    "7": {
        "Status" : True,
        "Modelo": "Colchones hinchables",
        "Precio": "$200.000",
        "Medidas": "180x120 cm"
    },
    "8": {
        "Status" : True,
        "Modelo": "Colchón de espuma de alta densidad",
        "Precio": "$700.000",
        "Medidas": "200x160 cm"
    },
    "9": {
        "Status" : True,
        "Modelo": "Colchón de muelles ensacados",
        "Precio": "$900.000",
        "Medidas": "210x180 cm"
    },
    "10": {
        "Status" : True,
        "Modelo": "Colchón de látex natural",
        "Precio": "$800.000",
        "Medidas": "200x150 cm"
    },
    "11": {
        "Status" : True,
        "Modelo": "Colchón plegable",
        "Precio": "$350.000",
        "Medidas": "190x120 cm"
    },
    "12": {
        "Status" : True,
        "Modelo": "Colchón futón",
        "Precio": "$500.000",
        "Medidas": "200x160 cm"
    },
    "13": {
        "Status" : True,
        "Modelo": "Colchón ecológico",
        "Precio": "$600.000",
        "Medidas": "200x180 cm"
    },
    "14": {
        "Status" : True,
        "Modelo": "Colchón para camping",
        "Precio": "$300.000",
        "Medidas": "190x140 cm"
    },
    "15": {
        "Status" : True,
        "Modelo": "Colchón ortopédico de espuma",
        "Precio": "$850.000",
        "Medidas": "210x190 cm"
    },
    "16": {
        "Status" : True,
        "Modelo": "Colchón viscoelástico básico",
        "Precio": "$700.000",
        "Medidas": "200x160 cm"
    },
    "17": {
        "Status" : True,
        "Modelo": "Colchón inflable de lujo",
        "Precio": "$600.000",
        "Medidas": "190x140 cm"
    },
    "18": {
        "Status" : True,
        "Modelo": "Colchón de espuma gruesa",
        "Precio": "$550.000",
        "Medidas": "200x160 cm"
    },
    "19": {
        "Status" : True,
        "Modelo": "Colchón con capa de gel",
        "Precio": "$950.000",
        "Medidas": "210x200 cm"
    },
    "20": {
        "Status" : True,
        "Modelo": "Colchón de muelles ortopédico",
        "Precio": "$900.000",
        "Medidas": "210x180 cm"
    },
    "21": {
        "Status" : True,
        "Modelo": "Colchón viscoelástico de lujo",
        "Precio": "$950.000",
        "Medidas": "200x150 cm"
    },
    "22": {
        "Status" : True,
        "Modelo": "Colchón doble de látex",
        "Precio": "$800.000",
        "Medidas": "200x180 cm"
    },
    "23": {
        "Status" : True,
        "Modelo": "Colchón de espuma económica",
        "Precio": "$300.000",
        "Medidas": "190x140 cm"
    },
    "24": {
        "Status" : True,
        "Modelo": "Colchón de muelles básicos",
        "Precio": "$400.000",
        "Medidas": "200x150 cm"
    },
    "25": {
        "Status" : True,
        "Modelo": "Colchón de espuma ortopédico",
        "Precio": "$900.000",
        "Medidas": "210x200 cm"
    },
    "26": {
        "Status" : True,
        "Modelo": "Colchón plegable compacto",
        "Precio": "$350.000",
        "Medidas": "190x120 cm"
    },
    "27": {
        "Status" : True,
        "Modelo": "Colchón inflable de espuma",
        "Precio": "$500.000",
        "Medidas": "190x140 cm"
    },
    "28": {
        "Status" : True,
        "Modelo": "Colchón de látex con memoria",
        "Precio": "$700.000",
        "Medidas": "200x160 cm"
    },
    "29": {
        "Status" : True,
        "Modelo": "Colchón ortopédico de muelles",
        "Precio": "$800.000",
        "Medidas": "210x180 cm"
    },
    "30": {
        "Status" : True,
        "Modelo": "Colchón ecológico de espuma",
        "Precio": "$600.000",
        "Medidas": "200x180 cm"
    }
}


    sucursales = {
    "1": {
        "Status" : False,
        "Sucursal": "Sucursal Central",
        "Direccion": "Libertad 330",
        "Stock Maximo": 500
    }, 
    "2": {
        "Status" : True,
        "Sucursal": "Sucursal Norte",
        "Direccion": "Rivadavia 450",
        "Stock Maximo": 300
    }, 
    "3": {
        "Status" : True,
        "Sucursal": "Sucursal Sur",
        "Direccion": "San Martín 120",
        "Stock Maximo": 400
    }, 
    "4": {
        "Status" : True,
        "Sucursal": "Sucursal Este",
        "Direccion": "Belgrano 890",
        "Stock Maximo": 100
    }, 
    "5": {
        "Status" : True,
        "Sucursal": "Sucursal Oeste",
        "Direccion": "Mitre 230",
        "Stock Maximo": 150
    }, 
    "6": {
        "Status" : True,
        "Sucursal": "Sucursal Plaza",
        "Direccion": "Sarmiento 670",
        "Stock Maximo": 300
    }, 
    "7": {
        "Status" : True,
        "Sucursal": "Sucursal Mercado",
        "Direccion": "Moreno 520",
        "Stock Maximo": 200
    }
}


    stock = {
    # Sucursal Central (Stock Máximo: 500)
    '1': {
        'Colchones de muelles': 50,
        'Colchones de espuma': 40,
        'Colchones de espuma viscoelástica': 30,
        'Colchones híbridos': 30,
        'Colchones de látex': 20,
        'Colchones ortopédicos': 20,
        'Colchones hinchables': 40,
        'Colchón de espuma de alta densidad': 40,
        'Colchón de muelles ensacados': 30,
        'Colchón de látex natural': 20,
        'Colchón plegable': 10,
        'Colchón futón': 10,
        'Colchón ecológico': 10,
        'Colchón para camping': 15,
        'Colchón ortopédico de espuma': 20,
        'Colchón viscoelástico básico': 20,
        'Colchón inflable de lujo': 15,
        'Colchón de espuma gruesa': 20,
        'Colchón con capa de gel': 15,
        'Colchón de muelles ortopédico': 10,
        'Colchón viscoelástico de lujo': 10,
        'Colchón doble de látex': 10,
        'Colchón de espuma económica': 20,
        'Colchón de muelles básicos': 10,
        'Colchón de espuma ortopédico': 20,
        'Colchón plegable compacto': 10,
        'Colchón inflable de espuma': 15,
        'Colchón de látex con memoria': 10,
        'Colchón ortopédico de muelles': 10,
        'Colchón ecológico de espuma': 10
    },

    # Sucursal Norte (Stock Máximo: 300)
    '2': {
        'Colchones de muelles': 30,
        'Colchones de espuma': 30,
        'Colchones de espuma viscoelástica': 20,
        'Colchones híbridos': 20,
        'Colchones de látex': 10,
        'Colchones ortopédicos': 15,
        'Colchones hinchables': 20,
        'Colchón de espuma de alta densidad': 15,
        'Colchón de muelles ensacados': 10,
        'Colchón de látex natural': 10,
        'Colchón plegable': 10,
        'Colchón futón': 10,
        'Colchón ecológico': 10,
        'Colchón para camping': 10,
        'Colchón ortopédico de espuma': 10,
        'Colchón viscoelástico básico': 10,
        'Colchón inflable de lujo': 5,
        'Colchón de espuma gruesa': 10,
        'Colchón con capa de gel': 10,
        'Colchón de muelles ortopédico': 10,
        'Colchón viscoelástico de lujo': 10,
        'Colchón doble de látex': 10,
        'Colchón de espuma económica': 10,
        'Colchón de muelles básicos': 10,
        'Colchón de espuma ortopédico': 10,
        'Colchón plegable compacto': 5,
        'Colchón inflable de espuma': 10,
        'Colchón de látex con memoria': 5,
        'Colchón ortopédico de muelles': 10,
        'Colchón ecológico de espuma': 10
    },

    # Sucursal Sur (Stock Máximo: 400)
    '3': {
        'Colchones de muelles': 40,
        'Colchones de espuma': 40,
        'Colchones de espuma viscoelástica': 30,
        'Colchones híbridos': 30,
        'Colchones de látex': 20,
        'Colchones ortopédicos': 20,
        'Colchones hinchables': 40,
        'Colchón de espuma de alta densidad': 30,
        'Colchón de muelles ensacados': 20,
        'Colchón de látex natural': 20,
        'Colchón plegable': 15,
        'Colchón futón': 20,
        'Colchón ecológico': 10,
        'Colchón para camping': 10,
        'Colchón ortopédico de espuma': 20,
        'Colchón viscoelástico básico': 10,
        'Colchón inflable de lujo': 10,
        'Colchón de espuma gruesa': 20,
        'Colchón con capa de gel': 20,
        'Colchón de muelles ortopédico': 10,
        'Colchón viscoelástico de lujo': 10,
        'Colchón doble de látex': 10,
        'Colchón de espuma económica': 10,
        'Colchón de muelles básicos': 20,
        'Colchón de espuma ortopédico': 20,
        'Colchón plegable compacto': 10,
        'Colchón inflable de espuma': 10,
        'Colchón de látex con memoria': 10,
        'Colchón ortopédico de muelles': 10,
        'Colchón ecológico de espuma': 10
    },

    # Sucursal Este (Stock Máximo: 100)
    '4': {
        'Colchones de muelles': 10,
        'Colchones de espuma': 10,
        'Colchones de espuma viscoelástica': 5,
        'Colchones híbridos': 5,
        'Colchones de látex': 5,
        'Colchones ortopédicos': 5,
        'Colchones hinchables': 10,
        'Colchón de espuma de alta densidad': 5,
        'Colchón de muelles ensacados': 5,
        'Colchón de látex natural': 5,
        'Colchón plegable': 5,
        'Colchón futón': 5,
        'Colchón ecológico': 5,
        'Colchón para camping': 5,
        'Colchón ortopédico de espuma': 5,
        'Colchón viscoelástico básico': 5,
        'Colchón inflable de lujo': 5,
        'Colchón de espuma gruesa': 5,
        'Colchón con capa de gel': 5,
        'Colchón de muelles ortopédico': 5,
        'Colchón viscoelástico de lujo': 5,
        'Colchón doble de látex': 5,
        'Colchón de espuma económica': 5,
        'Colchón de muelles básicos': 5,
        'Colchón de espuma ortopédico': 5,
        'Colchón plegable compacto': 5,
        'Colchón inflable de espuma': 5,
        'Colchón de látex con memoria': 5,
        'Colchón ortopédico de muelles': 5,
        'Colchón ecológico de espuma': 5
    },

    # Sucursal Oeste (Stock Máximo: 150)
    '5': {
        'Colchones de muelles': 20,
        'Colchones de espuma': 20,
        'Colchones de espuma viscoelástica': 15,
        'Colchones híbridos': 15,
        'Colchones de látex': 10,
        'Colchones ortopédicos': 10,
        'Colchones hinchables': 20,
        'Colchón de espuma de alta densidad': 10,
        'Colchón de muelles ensacados': 10,
        'Colchón de látex natural': 10,
        'Colchón plegable': 5,
        'Colchón futón': 10,
        'Colchón ecológico': 5,
        'Colchón para camping': 5,
        'Colchón ortopédico de espuma': 10,
        'Colchón viscoelástico básico': 5,
        'Colchón inflable de lujo': 5,
        'Colchón de espuma gruesa': 10,
        'Colchón con capa de gel': 10,
        'Colchón de muelles ortopédico': 5,
        'Colchón viscoelástico de lujo': 5,
        'Colchón doble de látex': 5,
        'Colchón de espuma económica': 5,
        'Colchón de muelles básicos': 10,
        'Colchón de espuma ortopédico': 10,
        'Colchón plegable compacto': 5,
        'Colchón inflable de espuma': 10,
        'Colchón de látex con memoria': 5,
        'Colchón ortopédico de muelles': 5,
        'Colchón ecológico de espuma': 5
    },

    # Sucursal Plaza (Stock Máximo: 300)
    '6': {
        'Colchones de muelles': 30,
        'Colchones de espuma': 30,
        'Colchones de espuma viscoelástica': 25,
        'Colchones híbridos': 25,
        'Colchones de látex': 20,
        'Colchones ortopédicos': 20,
        'Colchones hinchables': 30,
        'Colchón de espuma de alta densidad': 20,
        'Colchón de muelles ensacados': 15,
        'Colchón de látex natural': 10,
        'Colchón plegable': 10,
        'Colchón futón': 10,
        'Colchón ecológico': 10,
        'Colchón para camping': 10,
        'Colchón ortopédico de espuma': 10,
        'Colchón viscoelástico básico': 10,
        'Colchón inflable de lujo': 10,
        'Colchón de espuma gruesa': 10,
        'Colchón con capa de gel': 10,
        'Colchón de muelles ortopédico': 10,
        'Colchón viscoelástico de lujo': 10,
        'Colchón doble de látex': 10,
        'Colchón de espuma económica': 10,
        'Colchón de muelles básicos': 10,
        'Colchón de espuma ortopédico': 10,
        'Colchón plegable compacto': 10,
        'Colchón inflable de espuma': 10,
        'Colchón de látex con memoria': 10,
        'Colchón ortopédico de muelles': 10,
        'Colchón ecológico de espuma': 10
    },

    # Sucursal Mercado (Stock Máximo: 200)
    '7': {
        'Colchones de muelles': 20,
        'Colchones de espuma': 20,
        'Colchones de espuma viscoelástica': 15,
        'Colchones híbridos': 15,
        'Colchones de látex': 10,
        'Colchones ortopédicos': 10,
        'Colchones hinchables': 20,
        'Colchón de espuma de alta densidad': 10,
        'Colchón de muelles ensacados': 10,
        'Colchón de látex natural': 5,
        'Colchón plegable': 5,
        'Colchón futón': 5,
        'Colchón ecológico': 5,
        'Colchón para camping': 5,
        'Colchón ortopédico de espuma': 10,
        'Colchón viscoelástico básico': 5,
        'Colchón inflable de lujo': 5,
        'Colchón de espuma gruesa': 10,
        'Colchón con capa de gel': 10,
        'Colchón de muelles ortopédico': 5,
        'Colchón viscoelástico de lujo': 5,
        'Colchón doble de látex': 5,
        'Colchón de espuma económica': 5,
        'Colchón de muelles básicos': 10,
        'Colchón de espuma ortopédico': 10,
        'Colchón plegable compacto': 5,
        'Colchón inflable de espuma': 10,
        'Colchón de látex con memoria': 5,
        'Colchón ortopédico de muelles': 5,
        'Colchón ecológico de espuma': 5
    }
}



    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    print("Si quiere entrar con permisos de empleado coloque (1)")

    print( )

    print("Si quiere entrar con permisos de administrador coloque (2)")

    print( )
    print( )
    print( )
    permisos = input("Elija :")
    """
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    while True:
        opciones = 11+1
        
        
        
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1]  Ver Matriz")
            print("[2]  Ver informacion sobre los colchones")
            print("[3]  Ver informacion sobre las sucursales")
            print("[4]  Añadir colchones al stock")
            print("[5]  Eliminar colchones del stock")
            print("[6]  Cambiar precio de los colchones")
            print("[7]  Eliminar modelo de colchon")
            print("[8]  Eliminar sucursal")
            print("[9]  Ver lista de precios")
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
            exit() 
        

        
       
            
    


        if opcion == "1":
            verMatriz(colchones,sucursales,stock)


        if opcion == "2":
            verInformacionSobreLosColchones(colchones,stock)


        if opcion == "3":
            verInformacionSobreLasSucursales(sucursales)
            

        if opcion == "4":   
            añadirColchonesAlStock(colchones, sucursales, stock)
        

        if opcion == "5":   
            eliminarColchonesDelStock(colchones, sucursales, stock)


        if opcion == "6":   
            cambiarPrecioColchon(colchones)


        if opcion == "7" :   
            eliminarModelosDeColchones(colchones)
        
            

        if opcion == "8" :   
            eliminarSucursales(sucursales)
        


        if opcion == "9":   
            preguntarPrecioColchones(colchones)


        if opcion == "10" :  
            añadirNuevosModelosDeColchones()
        


        if opcion == "11":  
            añadirNuevasSucursal(nombreSucursal,direccionSucursal,stockMaximoSucursal)
        #else:
            #print("Un usuario con permiso de empleado no puede usar esta funcion")


        input("\nPresione ENTER para volver al menú.")
        print("\n\n")



# Punto de entrada al programa
main()

