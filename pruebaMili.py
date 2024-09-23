DiccSucursales = {
        "Sucursal1": {
           "Nombre": "Devoto",
           "Direccion": "libertad 330",
           "Stock Maximo": "300"
        }
}

def crearSucursal(DiccSucursales,nombreSucursal,direccionSucursal,stockMaximoSucursal):
    # Esta funcion recibira numero de sucursal, nombre, direccion y stock maximo. Agregara a el diccionario 
    # "sucursales" los datos.
    # Crear un diccionario interno con la información de la sucursal
    sucursalInfo={
        "nombre":nombreSucursal,
        "direccion":direccionSucursal,
        "stockMaximo":stockMaximoSucursal,
        
    }
    numeroSucursal = len(DiccSucursales) + 1
    # Agregar el diccionario interno al diccionario externo
    DiccSucursales["Sucursal"+numeroSucursal] = sucursalInfo
    return

def main():
    #Llamado a la funcion crearSucursal
    nombreSucursal=input("Ingrese el nombre de la sucursal nueva: ")
    direccionSucursal=input("Ingrese la dirección de la nueva sucursal: ")
    stockMaximoSucursal=int(input("Ingese el stock maximo de la sucursal nueva: "))
    crearSucursal(DiccSucursales,nombreSucursal,direccionSucursal,stockMaximoSucursal)

# Punto de entrada al programa
main()