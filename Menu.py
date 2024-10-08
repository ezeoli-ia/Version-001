#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    ...


    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 4
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Opción 1")
            print("[2] Opción 2")
            print("[3] Opción 3")
            print("[4] Opción 4")
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

        elif opcion == "1":   # Opción 1
            ...
        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            ...
        elif opcion == "4":   # Opción 4
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()