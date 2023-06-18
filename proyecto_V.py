import numpy as np


asientos_ocupados=[22,2,3,4,31,27] #asientos ocupados

#función mostrar los asientos disponibles // printea los números del array los ordena y reemplaza por X cuando coincide los asientos ocupados con el del array original
def mostrar_asientos():
    a=0
    b=0
    print("Asientos del vuelo:\n")
    for b in range (5):
        print("|",end="  ")
        for a in range(3):
            if(asientos_2[b][a] in asientos_ocupados):
                asiento= "X "
            elif(asientos_2[b][a]<10):
                asiento= str(round(asientos_2[b][a]))+" "
            else:
                asiento=round(asientos_2[b][a])
            print(asiento,end=" ")
        print(end="    ")
        for a in range (3):
            if(asientos_2[b][3+a] in asientos_ocupados):
                asiento= "X "
            elif(asientos_2[b][3+a]<10):
                asiento= str(round(asientos_2[b][3+a]))+" "
            else:
                asiento=round(asientos_2[b][3+a])
            print(asiento,end=" ")
        print(" |")
    print(" __________","    ""__________")
    print(" __________","    ""__________")
    for b in range(5,7):
        print("|",end="  ")
        for a in range(3):
            if(asientos_2[b][a] in asientos_ocupados):
                asiento= "X "
            else:  
                asiento=round(asientos_2[b][a])    
            print(asiento,end=" ")
        print(end="    ")
        for a in range (3):
            if(asientos_2[b][3+a] in asientos_ocupados):
                asiento= "X "
            else:
                asiento=round(asientos_2[b][3+a])
            print(asiento,end=" ")
        print(" |")
    print("\n")
    if op=="1":
        mostrar_opciones() #solo lo muestra cuando la opción es 1 en el menu mostrar_opciones; si es op==2 (Compra de asientos), tambien visualiza los asientos, pero no vuelve a mostrar las opciones, sino que continua con la compra de asientos.
     
#función registrar datos del pasajero:

def ingreso():
    nombre= (input("\nFavor ingrese su nombre: "))
    rut=0    
    celular=0
    banco=0
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            rut= int(input("ingrese su rut: sin punto ni guión: "))
            rut_test= rut     #Se crea una variable alterna para no tocar el rut ingresado que debe tener 8 a 9 digitos (sin considerar puntos ni guion).
            cont=0
            while rut_test>0:
                cont=cont+1              #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera, mientras sea mayor a 0.
                rut_test= rut_test//10
            if cont<8 or cont>9:
                print("rut inválido")
            else:
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")      
    while(True):
        try:
            celular= int(input("Ingrese su número de celular sin ante sin anteponer el 9: "))
            celular_test= celular  #Se crea una variable alterna para no tocar el número de telefono que 8 digitos exactos (sin considerar el 9 o +569).
            cont=0
            while celular_test>0:
                cont=cont+1                #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera , mientras sea mayor a 0.
                celular_test= celular_test//10 
            if cont!=8:
                print("Telefono inválido")
            else:
                banco= (input("ingrese su banco: ")) 
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")    
    print("\nDatos ingresados correctamente\n\n")
    global cliente
    cliente={"Nombre":nombre,"Rut":rut,"Celular":celular,"Banco":banco} #completados los datos correctamente, guardamos los datos del cliente en un diccionario.

#función comprar asientos:

def comprar_asiento():
    ingreso()
    retorno="R"
    while retorno=="R":
        conf=""
        retorno=""
        mostrar_asientos()
        print("Los asientos marcados con una X, no se encuentran disponibles.\nDesde el asiento 31 al 42 son para pasajeros VIP.\n\nLos precios son:\n\n - Asiento normal: $ 78.900\n - Asiento VIP: $ 240.000\n")
        eleccion=int(input("Favor, Seleccione un asiento: "))
        eleccion={"Asiento":eleccion}
        cliente.append(eleccion)
        if 0<eleccion and eleccion<31:
            precio=78900
        elif 31<=eleccion and eleccion<43:
            precio=240000
        print("\nEl precio a pagar es de: $",precio)
        while(conf != "S" and conf != "C" and conf != "M"):
            conf=input("\nPara confirmar asiento, presione S.\nPara cambiar asiento presione C.\nPara anular elección y volver al menu pricipal presione M\n\n Opcion: ").upper()
        else:
            if conf=="S":
                for datos in cliente:
                    print(datos,":",cliente[datos])
            elif conf=="C":
                retorno="R"
            elif conf=="M":
                eleccion=""
                mostrar_opciones()

def mostrar_opciones():
    global op
    op=""
    while(op != "1" and op != "2" and op != "3" and op != "4" and op != "5"):
        op= input("Ingrese una opcion:\n \n1. Ver asientos disponibles \n2. Comprar asiento \n3. Anular vuelo \n4. Modificar datos de pasajero \n5. Salir\n\nOpcion: ")
    else:
        if op=="1":
            mostrar_asientos()
        elif op=="2":
            comprar_asiento()
        elif op=="3":
            print("algo")
        elif op=="4":
            print("algo")
        elif op=="5":
            print("hasta pronto")
    
#inicio del programa: comprueba si existe registro de asientos en archivo"asientos.txt", sino crea un arreglo y lo guarda en un archivo txt: "asientos.txt"

try:         # comprueba que existe registro de asientos tomados anteriormente
    file = open('asientos.txt')
    print("work") # 
    asientos_2 = np.loadtxt('asientos.txt', dtype=int)
    print("¡ Bienvenido a Vuelos-Duoc favor !\n")
    mostrar_opciones()
except FileNotFoundError: # sino existe crea una matriz de 7x6 y rellena del 1 a 42 asientos, luego lo guarda en un archivo .txt
    asientos= np.zeros((7,6))
    i=1
    for c in range(7):
        for f in range(6):
            asientos[c][f]=i
            i=i+1
    np.savetxt('asientos.txt', asientos, fmt='%d')
    asientos_2 = np.loadtxt('asientos.txt', dtype=int)
    print(asientos_2)
    mostrar_opciones()
   