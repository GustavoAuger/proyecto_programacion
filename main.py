
asientos_ocupados=[] #asientos ocupados

import numpy as np
from funciones import *

def mostrar_opciones():
    global cliente
    global op
    op=""
    while(op != "1" and op != "2" and op != "3" and op != "4" and op != "5"):
        op= input("Ingrese una opcion:\n \n1. Ver asientos disponibles \n2. Comprar asiento \n3. Anular vuelo \n4. Modificar datos de pasajero \n5. Salir\n\nOpcion: ")
    else:
        if op=="1":
            mostrar_asientos()
        elif op=="2":
            comprar_asiento()
        elif op=="3": #anula el último vuelto que se compro en el momento, y deja el asiento disponible. (no especifica que sea un vuelo anterior)
            anular_vuelo()
        elif op=="4":
            modificar()
        elif op=="5":
            np.save('file.npy', lista_vueloL) #Cierra el programa, y guarda los cambios sobreescribiendo el archivo npy, donde almacenamos nuestra lista de pasajeros con su respectivo asiento
            print("\n¡ Hasta pronto !\n")
