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
def CrearMatrizPrincipal(filas,columnas,sucursales,matriz):
    # Aca ira la matriz en donde estaran todos los datos
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            if c==0 :
                relleno = f
                if 0<f<10:
                    relleno = sucursales[f-1]  
                    matriz[f].append(relleno)
                else:
                    matriz[f].append(relleno)
            if f==0:
                matriz[f].append(" Modelo")
            else:
                relleno = str(random.randint(10,99))
                matriz[f].append(str("   " + relleno + "  "))
    return matriz


def colchones():
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
    return diccColchones


def sucursales():
    DiccSucursales = {
        "Sucursal1": {
           "Nombre": "Devoto",
           "Direccion": "libertad 330",
           "Stock Maximo": "300"
           }
    }
    return DiccSucursales
def crearNuevoColchon():
    #Mili y Juli
    # Esta funcion recibira el modelo y los datos del colchon que se quiere añadir al diccionario.

    return

def crearSucursal(nombreSucursal,direccionSucursal,stockMaximoSucursal):
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
    return

def eliminarMarcaOColchon():
    #Esta funcion recibira los datos que se quieran eleminar de la matriz.
    
    
    return

def verificarStock():
    #Esta funcion permite controlar y consultar sobre el stock total y por sucursal
    # Esto no seria solamente , hacerle un print a la matriz
    return

def detalleColchon():
    #Facu
    #Esta funcion permite obtener detalles especificos de cada modelo de colchon 
    
    return


def precioColchones():
    #Sofi 
    #Esta funcion permite ver el precio de cada modelo de colchon
    
    return

def añadirStockALaMatriz():
    #Esta funcion permite sumar un numero en una fila(sucursal) y columna(modelo) en la matriz que hace referencia al stock.

    return

def infoSucursal():
    #Esta funcion brinda informacion sobre la sucursal elegida

    return
def cambiarPrecioColchon():
    #Esta funcion hace posible cambiar el precio a cualquier modelo de colchon

    return
def añadirNuevasMarcasDeColchones():
    #

    return
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    filas = 8
    columnas = 10
    matriz = []
    sucursales = ['Sucursal Central','Sucursal Norte','Sucursal Sur','Sucursal Este','Sucursal Oeste','Sucursal Plaza','Sucursal Mercado',]

    Matriz= CrearMatrizPrincipal(filas,columnas,sucursales,matriz)


    for fila in matriz:
        print(fila)


    
    nombreSucursal=input("Ingrese el nombre de la sucursal nueva: ")
    direccionSucursal=input("Ingrese la dirección de la nueva sucursal: ")
    stockMaximoSucursal=int(input("Ingese el stock maximo de la sucursal nueva: "))
    


    crearSucursal(nombreSucursal,direccionSucursal,stockMaximoSucursal)

# Punto de entrada al programa
main()

"""
    Crear
    Añadir nuevos colchones al stock con su marca y modelo.(Realizado)
    Registrar nuevos modelos en sucursales específicas de la matriz.(Realizado)
    Agregar nuevas sucursales. (Realizado)
    
    Leer:
    Verificar el stock total y por sucursal. (Realizado)
    Obtener detalles de colchones específicos. (Realizado)
    Consultar precios de colchones. (Realizado)
    Buscar información sobre las sucursales. (Realidazo)
    
    Actualizar:
    Modificar precios de modelos de colchones.(Realizado)
    
    Remover colchones del stock:
    Eliminar marcas o modelos específicos en una sucursal.(Realizado)
"""