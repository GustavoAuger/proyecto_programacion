import numpy as np
from funciones import *
print("¡ Bienvenido a Vuelos-Duoc !\n")
matriz() # inicio del programa creamos la matriz de los asientos 
creacion() #intenta abrir un registro de reservas de un archivo npy (simulando una bd), si es que existe. Sino crea un un archivo npy. y transforma a datos que podamos utilizar.
mostrar_opciones() #llama al menu principal - la cual esta interconectadas con las otras funciones como mostrar_asientos(); comprar_asiento(); anular_vuelo(); modificar(); y a su vez, éstas al terminar, llaman al menu principal.

