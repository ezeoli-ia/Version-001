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
Cuando pedis la informacion sobre los colchones NO aparece la cantidad de stock de cada sucursal
Se puede poner mas stock del maximo
No hay muchas verificaciones al ingresar los datos

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
from datetime import datetime
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# [1]
def verMatriz(colchones,sucursales,stock):
    matriz=[]
    
    for f in range(len(sucursales) + 1):
        if f != 0 and sucursales[str(f)]["Status"] == True:  # Verificamos que el Status de la sucursal sea True
            matriz.append([sucursales[str(f)]["Sucursal"]])
        else:
            matriz.append([""])
        
        for c in range(len(colchones)):
            if colchones[str(c + 1)]["Status"] == True:  # Verificamos que el Status del colchón sea True
                if f == 0 and colchones[str(c + 1)]["Modelo"]:  # Imprime el modelo de colchón en la primera fila
                    matriz[f].append(colchones[str(c + 1)]["Modelo"])
                elif f != 0:  # En otras filas imprimimos el stock de cada modelo en la sucursal
                    NO = colchones[str(c + 1)]["Modelo"]
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

        # Un for que imprime todas las opciones para pedir informacion
        for elem in colchones: 
            if colchones[str(elem)]["Status"] == True:
                print("[",elem,"]","Toda la informacion de los modelos de",colchones[elem]["Modelo"])
        print("---------------------------")
        print()
        
        opcion = input("Seleccione una opción: ")
        #Valida la entrada de dato
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            #Se pregunta si el dato es diferente a 0
            if opcion!="0":
                #Se pregunta si el modelo de colchon esta habilitado, despues lo imprime si lo esta
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
                # Si se coloca 0 empieza un for en el que imprime toda la informacion de los colchones de forma ordenada
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
    # variable para verificar el dato de la opcion ingresada
    opciones=len(sucursales)+1
    while True:
        print()
        print("---------------------------")
        print("MENÚ DE LAS SUCURSALES     ")
        print("---------------------------")
        print("[ 0 ] Toda la informacion de las sucursales")
        # Un bucle en el que coloca todas las opciones de sucursales habilitadas
        for elem in sucursales: 
            if sucursales[str(elem)]["Status"] == True:
                print("[",elem,"]","Toda la informacion de los modelos de",sucursales[elem]["Sucursal"])
        print("---------------------------")
        print()

        # Pregunta la opcion
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            # pregunta si es diferente a 0
            if opcion!="0":
                # Pregunta si la opcion eligida esta habilitada 
                if sucursales[str(opcion)]["Status"] == True: 
                    print( )
                    print("-------------------------------" )
                    print("Nombre de la sucursal: ",sucursales[opcion]["Sucursal"])
                    print("Direccion :",sucursales[opcion]["Direccion"])
                    print("Stock Maximo :",sucursales[opcion]["Stock Maximo"])
                    print("-------------------------------" )
                    print( )
                    break
                else:
                    print()
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            else:
                # si es 0 imprime la informacion de todas las sucursales
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
    # Variable para verificar el dato ingresado
    opciones=len(colchones)+1
    print()
    print()
    # Menu
    while True:
        print("---------------------------")
        print("Sucursales disponibles:")
        print("---------------------------")
        #Variable para sumar las vueltas
        aux=0
        #bucle para mostrar las opciones de sucursales
        for sucursal_id, sucursal_info in sucursales.items():
            aux=aux+1
            #Pregunta si las sucursales esta habilitada, si no ,no la imprime
            if sucursales[str(aux)]["Status"]==True:
                print("[ " + sucursal_id + " ] " + sucursal_info['Sucursal'])
        print("---------------------------")
        
        print()
        print( )
        #Variable par }a ingresar el dato
        sucursal_elegida = input("Seleccione el número de la sucursal donde desea agregar colchones: ")
        print()
        print()
        # IF para validar el dato
        if sucursal_elegida in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            #otro if para validar el dato
            if int(sucursal_elegida) <len(sucursales):
                # Un if para fijarse si la sucursal esta habilitada, si lo esta imprime
                if sucursales[str(sucursal_elegida)]["Status"] == True:
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
            else:
                print()
                print()
                print("Opción inválida. Por favor, elija un número de sucursal válido.")
                print()
                print()
                print()
                print()
        else:
            print()
            print()
            print("Opción inválida. Por favor, elija un número de sucursal válido.")
            print()
            print()
            print()
            print()

    while True:
        opciones=len(colchones)+1
        print("---------------------------")
        print("Modelos de colchones disponibles:")
        print("---------------------------")
        #Variable para sumar las vueltas
        aux=0
        #bucle para mostrar las opciones de colchones
        for colchon_id, colchon_info in colchones.items():
            aux=aux+1
            #Pregunta si las sucursales esta habilitada, si no ,no la imprime
            if colchones[str(aux)]["Status"]==True:
                print("[ " + colchon_id + " ] " + colchon_info['Modelo'])
        print("---------------------------")
        print()
        #Variable para ingresar la opcion
        colchon_elegido = input("Seleccione el número del colchón que desea agregar al stock: ")
        # Un if de verificaion de dato
        if colchon_elegido in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            # Un if de verificaion de dato
            if int(colchon_elegido) <len(colchones):
                # IF de verificar si el modelo de colchon esta disponible
                if colchones[str(colchon_elegido)]["Status"] == True:
                    print()
                    print("Ha seleccionado el modelo " + colchones[colchon_elegido]['Modelo'] + ".")
                    break  # Sale del bucle si el colchón es válido
                else:
                    print()
                    print()
                    print("Opción inválida. Por favor, elija un número de sucursal válido.")
                    print()
                    print()
                    print()
                    print()
            else:
                print()
                print()
                print("Opción inválida. Por favor, elija un número de sucursal válido.")
                print()
                print()
                print()
                print()
        else:
            print()
            print()
            print("Opción inválida. Por favor, elija un número de colchón válido.")
            print()
            print()
            
    while True:
        print()
        print()
        #Variable para colocar el numero de colchones a ingresar
        cantidad = input("¿Cuántos colchones desea agregar al stock? ")
        #Verifica si el dato ingresado son numeros
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
def eliminarColchonesDelStock(colchones, sucursales, stock, compra_venta):
    
    
    while True:
        opciones = len(sucursales) + 1
        print()
        print("---------------------------")
        print("MENÚ PARA ELIMINAR COLCHONES DEL STOCK")
        print("---------------------------")
        
        # Mostrar las sucursales
        aux = 0
        for sucursal in sucursales:
            aux += 1
            if sucursales[str(aux)]["Status"] == True:
                print(f"[{sucursal}] {sucursales[sucursal]['Sucursal']}")
        print("---------------------------")

        sucursal_opcion = input("Seleccione una sucursal: ")
        
        if sucursal_opcion in [str(i) for i in range(1, opciones)]:  # Ajuste: los índices de las sucursales empiezan desde 1
            if sucursales[sucursal_opcion]["Status"] == True:
                print()
                print(f"Sucursal seleccionada: {sucursales[sucursal_opcion]['Sucursal']}")
                print("---------------------------")
                
                # Mostrar los colchones disponibles en esa sucursal
                print("Colchones disponibles:")
                for colchon_id in colchones:
                    if colchones[colchon_id]["Status"] == True:
                        modelo = colchones[colchon_id]["Modelo"]
                        print(f"[{colchon_id}] {modelo} - Stock: {stock[sucursal_opcion][modelo]}")
                print("---------------------------")
                
                colchon_opcion = input("Seleccione un colchón para eliminar del stock: ")
                
                if colchon_opcion in colchones and colchones[colchon_opcion]["Status"] == True:
                    cantidad = int(input(f"¿Cuántos {colchones[colchon_opcion]['Modelo']} desea eliminar?: "))
                    print()
                    if cantidad <= stock[sucursal_opcion][colchon_opcion]:
                        # Restar la cantidad del stock
                        stock[sucursal_opcion][colchon_opcion] -= cantidad
                        print(f"Se han eliminado {cantidad} colchones de {colchones[colchon_opcion]['Modelo']} del stock de {sucursales[sucursal_opcion]['Sucursal']}.")

                        # Crear un nuevo ID de venta automáticamente
                        nuevo_item_id = f"venta{str(len(compra_venta) + 1).zfill(2)}"  # Incrementar el número de venta automáticamente
                        fecha_actual = datetime.now().strftime("%d/%m/%Y %H.%M")  # Obtener fecha y hora actuales

                        # Añadir el nuevo ítem al diccionario de compras
                        compra_venta[nuevo_item_id] = {
                            "id": colchon_opcion, 
                            "cantidad": cantidad, 
                            "fecha": fecha_actual
                        }    
                        print("Venta realizada con éxito")
                    else:
                        print("Error: No hay suficientes colchones en stock para eliminar esa cantidad.")
                else:
                    print("Opción inválida. Por favor, seleccione un colchón válido.")
            else:
                print("Opción inválida. Por favor, seleccione una sucursal válida.")
        else:
            print("Opción inválida. Por favor, seleccione una sucursal válida.")
    
# [6] 
def cambiarPrecioColchon(colchones):
    # Mostrar todos los colchones disponibles
    print()
    print("Colchones disponibles:")
    print("-----------------------")
    aux = 0
    for key, colchon in colchones.items():
        aux += 1
        if colchones[str(aux)]["Status"]:
            print(f"{key}. {colchon['Modelo']} - Precio: {colchon['Precio']}")
            print("            -            ")

    # Seleccionar el colchón que se desea modificar
    print()
    while True:
        colchon_id = input("Elige el número del colchón que deseas modificar: ")

        # Validar si el ID ingresado existe en el diccionario de colchones
        if colchon_id in colchones:
            # Mostrar el colchón seleccionado
            colchon_seleccionado = colchones[colchon_id]
            print(f"\nHas seleccionado: {colchon_seleccionado['Modelo']} - Precio actual: {colchon_seleccionado['Precio']}")
            print()
            
            # Pedir el nuevo precio con validación
            while True:
                nuevo_precio = input("Introduce el nuevo precio (no se aceptan decimales): $")

                # Comprobar si la entrada es un número entero positivo
                if nuevo_precio.isdigit() and int(nuevo_precio) > 0:
                    nuevo_precio_int = int(nuevo_precio)  # Convertir a int aquí
                    # Formatear el precio con puntos como separadores de miles
                    precio_formateado = "{:,}".format(nuevo_precio_int).replace(",", ".")
                    # Actualizar el precio en el diccionario
                    colchones[colchon_id]["Precio"] = f"${precio_formateado}"
                    print(f"\nEl precio del {colchon_seleccionado['Modelo']} ha sido actualizado a ${precio_formateado}.")
                    return  # Salir de la función ya que el cambio ha sido exitoso
                else:
                    print("Entrada inválida. Por favor, introduce un número entero positivo sin puntos.")
                    
        else:
            print("Opción inválida. El número del colchón no existe. Por favor, elige un número válido.")
            cambiarPrecioColchon(colchones)
    
# [7]
def eliminarModelosDeColchones(colchones):
    #Variable para validar el menu
    opciones=len(colchones)+1
    while True:
        print()
        print("---------------------------------------------")
        print("MENÚ PARA ELIMINAR UN MODELO DE COLCHON      ")
        print("---------------------------------------------")
        #Bucle en el que imprime las opciones que pasan la verificacion de estar habilitadas
        for elem in colchones:
            if colchones[str(elem)]["Status"] == True:
                print("[",elem,"]",colchones[elem]["Modelo"])
        print("---------------------------")
        print()
        #Variable para ingresar la opcion
        opcion = input("Seleccione una opción: ")
        #IF para verificar que la opcion este
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            print()
            print()
            # IF para verificar que el modelo de colchon este habilitado e imprimirlo
            if colchones[str(opcion)]["Status"] == True: 
                print("Se a eliminado el modelo",colchones[opcion]["Modelo"],"en todas las sucursales")
                # Cambia el valor de true por false
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
    #Variable para validar el menu
    opciones=len(sucursales)+1
    while True:
        print()
        print("---------------------------------------")
        print("MENÚ PARA ELIMINAR UN SUCURSAL         ")
        print("---------------------------------------")
        #Bucle en el que imprime las opciones que pasan la verificacion de estar habilitadas
        for elem in sucursales:
            if sucursales[str(elem)]["Status"] == True:
                print("[",elem,"]",sucursales[elem]["Sucursal"])
        print("---------------------------")
        print()
        #Variable para ingresar la opcion
        opcion = input("Seleccione una opción: ")
        #IF para verificar que la opcion este
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            print()
            print()
            # IF para verificar que el modelo de colchon este habilitado e imprimirlo
            if sucursales[str(opcion)]["Status"] == True: 
                print("Se a eliminado la",sucursales[opcion]["Sucursal"])
                # Cambia el valor de true por false
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
    """
    Esta funcion muestra una lista de los modelos de colchones con su precio
    usa un for de conteo y una verificacion de disponibilidad, para imprimir lo necesario
    """
    for i in range(1,len(colchones)+1):
        if colchones[str(i)]["Status"] == True:
            print("                     -")
            print("El precio del modelo ", colchones[str(i)]["Modelo"]," es de ",colchones[str(i)]["Precio"])
    print()

# [10] 
def añadirNuevosModelosDeColchones(colchones):
    aux = 1
    # bucble para reafirmar los datos ingresados
    while aux==1:
        print()
        print()
        modeloDeColchon=input("Nombre del nuevo modelo de colchon: ")
        print()
        precio=input("Cual es el precio del modelo :")
        print()
        medidas=input("Cuales son las medidas del colchon (Ej: 200x140 cm): ")
        print()
        print()
        print()
        print("Esta seguro de querer añadir un nuevo modelo de colchon con esta informacion?")
        print("Modelo de colchon :", modeloDeColchon)
        print("Precio : ", precio)
        print("Medidas : ", medidas)
        print()
        print()
        aux = int(input("Coloque [ 0 ] si esta seguro o [ 1 ] si desea volver a colocar los datos"))
    # Crea la clave y los valores y los mete en el diccionario
    colchones[str(len(colchones)+1)]= {
        "Status" : True,
        "Modelo": modeloDeColchon,
        "Precio": precio,
        "Medidas": medidas,
    }

# [11] 
def añadirNuevasSucursal(sucursales,stock,colchones):
    """
    
    """
    aux = 1
    # bucble para reafirmar los datos ingresados
    while aux==1:
        print()
        print()
        sucursal=input("Nombre de la nueva sucursal: ")
        print()
        direccion=input("Cual es la direccion de la sucursal: ")
        print()
        stockMaximo=input("Cual es el valor maximo de stock que puede tener la sucursal: ")
        print()
        print()
        print()
        print("Esta seguro de queres añadir una sucursal con esta informacion?")
        print("Sucursal :", sucursal)
        print("Direccion : ", direccion)
        print("Stock maximo : ", stockMaximo)
        print()
        print()
        aux = int(input("Coloque [ 0 ] si esta seguro o [ 1 ] si desea volver a colocar los datos"))
        
    # Crea la clave y los valores y los mete en el diccionario
    sucursales[str(len(sucursales)+1)]= {
        "Status" : True,
        "Sucursal": sucursal,
        "Direccion": direccion,
        "Stock Maximo": stockMaximo,
    }
    print()
    print()
    #Bucle para ingresar el stock en la nueva sucursal
    for i in range (1,len(colchones)+1):
        if colchones[str(i)]["Status"]==True:
            print()
            aux=str(colchones[str(i)])
            aux1=input("Cuanto stock de " + colchones[str(i)]["Modelo"] + " se tiene: ")
            stock[str(len(sucursales))] ={aux : aux1}





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


    compra_venta = {
    "venta01": {"id": 1, "cantidad": 10, "fecha": "01/01/2024 12.00"},
    "venta02": {"id": 2, "cantidad": 5, "fecha": "02/01/2024 13.30"},
    "venta03": {"id": 3, "cantidad": 8, "fecha": "03/01/2024 14.45"},
    "venta04": {"id": 4, "cantidad": 3, "fecha": "04/01/2024 15.15"},
    "venta05": {"id": 5, "cantidad": 12, "fecha": "05/01/2024 16.00"},
    "venta06": {"id": 6, "cantidad": 6, "fecha": "06/01/2024 17.20"},
    "venta07": {"id": 7, "cantidad": 4, "fecha": "07/01/2024 18.30"},
    "venta08": {"id": 8, "cantidad": 15, "fecha": "08/01/2024 19.40"},
    "venta09": {"id": 9, "cantidad": 7, "fecha": "09/01/2024 20.50"},
    "venta10": {"id": 10, "cantidad": 9, "fecha": "10/01/2024 21.00"},
    "venta11": {"id": 11, "cantidad": 11, "fecha": "11/01/2024 22.10"},
    "venta12": {"id": 12, "cantidad": 2, "fecha": "12/01/2024 23.15"},
    "venta13": {"id": 13, "cantidad": 1, "fecha": "13/01/2024 00.30"},
    "venta14": {"id": 14, "cantidad": 3, "fecha": "14/01/2024 01.45"},
    "venta15": {"id": 15, "cantidad": 5, "fecha": "15/01/2024 02.00"},
}

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Acceso a los permisos administrador o empleado
    print()
    print()
    print()
    print("Para entrar con permisos de administrador coloque [ 0 ], si quiere entrar con permisos de empleado coloque [ 1 ]")
    print()
    print()
    permisos=int(input("Elija: "))
    
    #Validacion de datos ingresados e reingreso en el caso de error
    while permisos != 0 and permisos != 1:
        permisos=int(input("Elija: "))
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #Menu del administrador
    if permisos == 0:
        while True:
            # numero de opciones + 1 para que no de error al poner la ultima opcion
            opciones = 11+1
            
            # Menu del administrador
            while True:
                print()
                print("---------------------------")
                print("MENÚ DEL SISTEMA           ")
                print("---------------------------")
                print("[1]  Ver Matriz")
                print("[2]  Ver información sobre los colchones")
                print("[3]  Ver información sobre las sucursales")
                print("[4]  Añadir colchones al stock")
                print("[5]  Eliminar colchones del stock")
                print("[6]  Cambiar precio de los colchones")
                print("[7]  Eliminar modelo de colchón")
                print("[8]  Eliminar sucursal")
                print("[9]  Ver lista de precios")
                print("[10] Añadir nuevo modelo de colchón")
                print("[11] Añadir nueva sucursal ")
                print("---------------------------")
                print("[0] Salir del sistema")
                print("---------------------------")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    print()
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
                eliminarColchonesDelStock(colchones, sucursales, stock,compra_venta)


            if opcion == "6":   
                cambiarPrecioColchon(colchones)


            if opcion == "7" :   
                eliminarModelosDeColchones(colchones)


            if opcion == "8" :   
                eliminarSucursales(sucursales)
            

            if opcion == "9":   
                preguntarPrecioColchones(colchones)


            if opcion == "10" :  
                añadirNuevosModelosDeColchones(colchones)
            

            if opcion == "11":  
                añadirNuevasSucursal(sucursales,stock,colchones)


            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


    #Menu del emplado
    if permisos == 1:
        while True:
            # numero de opciones + 1 para que no de error al poner la ultima opcion
            opciones = 7+1
            
            # Menu del empleado
            while True:
                print()
                print("---------------------------")
                print("MENÚ DEL SISTEMA           ")
                print("---------------------------")
                print("[1]  Ver Matriz")
                print("[2]  Ver información sobre los colchones")
                print("[3]  Ver información sobre las sucursales")
                print("[4]  Añadir colchones al stock")
                print("[5]  Eliminar colchones del stock")
                print("[6]  Cambiar precio de los colchones")
                print("[7]  Ver lista de precios")
                print("---------------------------")
                print("[0] Salir del sistema")
                print("---------------------------")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    print()
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
            

            if opcion == "7":   
                preguntarPrecioColchones(colchones)


            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()

