import numpy as np
from itertools import cycle
def matriz(): # inicio del programa creamos la matriz de los asientos 
    global asientos
    asientos= np.zeros((7,6)) 
    i=1
    for c in range(7):
        for f in range(6):
            asientos[c][f]=i
            i=i+1

def creacion():
    global cliente
    global lista_vuelo
    global cantidad_pasajeros_inicial
    global asientos_ocupados
    asientos_ocupados=[] # creamos la lista asientos ocupados "el asiento 0"
    #intenta abrir un registro de reservas de un archivo npy (simulando una bd), si es que existe. Sino crea un un archivo npy:
    try:
        cliente = {} #Se define como diccionario la variable cliente, guarda sus datos + su asiento.
        lista_vuelo = np.load('file.npy', allow_pickle='TRUE') 
    except FileNotFoundError:
        lista_vuelo=[{"Nombre":"none","Rut":0,"Celular":0,"Banco":"none","Asiento":0}]  #Al no existir una "lista" de vuelo anterior, creamos la variable lista_vuelo del tipo array, con un cliente ficticio para que el valor de la clave asiento en el diccionario exista"
        np.save('file.npy', lista_vuelo)
        lista_vuelo = np.load('file.npy', allow_pickle='TRUE')
    lista_vuelo=lista_vuelo.tolist()
    for asiento in lista_vuelo: #De acuerdo a la lista de vuelo, toma el valor de la clave Asiento 
        asientos_ocupados.append(asiento["Asiento"]) #se le asirgna valor 0 que viene del diccionario dentro de la lista_vuelo, el cual no existe el asiento el valor 0 (no afecta para el uso del programa), pero nos sirve para ir comparando con el array inicial, de esta forma cuando se ocupe un asiento lo reemplaza por la varible X cuando este pintando los valores de la matriz
    cantidad_pasajeros_inicial=len(lista_vuelo) #para tener el control de la cantidad de pasajeros inicial, a la hora de eliminar el último asiento
 #   print(asientos_ocupados) #de control para ver cual(es), son los asientos ocupados
#    print(lista_vuelo)
#función mostrar los asientos disponibles // printea los números del array los ordena y reemplaza por X cuando coincide los asientos ocupados con el del array original
def mostrar_asientos():
    a=0
    b=0
    global asientos
    print("Asientos del vuelo:\n")
    for b in range (5):
        print("|",end="  ")
        for a in range(3):
            if(asientos[b][a] in asientos_ocupados): #asientos[b][a] son cordenadas del array creado al inicio y comprueba si ese asiento en particular se encuentra en los asientos ocupados
                asiento= "X "
            elif(asientos[b][a]<10):
                asiento= str(round(asientos[b][a]))+" "
            else:
                asiento=round(asientos[b][a])
            print(asiento,end=" ")
        print(end="    ")
        for a in range (3):
            if(asientos[b][3+a] in asientos_ocupados):
                asiento= "X "
            elif(asientos[b][3+a]<10):
                asiento= str(round(asientos[b][3+a]))+" "
            else:
                asiento=round(asientos[b][3+a])
            print(asiento,end=" ")
        print(" |")
    print(" __________","    ""__________")
    print(" __________","    ""__________")
    for b in range(5,7):
        print("|",end="  ")
        for a in range(3):
            if(asientos[b][a] in asientos_ocupados):
                asiento= "X "
            else:  
                asiento=round(asientos[b][a])    
            print(asiento,end=" ")
        print(end="    ")
        for a in range (3):
            if(asientos[b][3+a] in asientos_ocupados):
                asiento= "X "
            else:
                asiento=round(asientos[b][3+a])
            print(asiento,end=" ")
        print(" |")
    print("\n")
    #print(lista_vuelo) lista de los pasajeros con sus datos
    #print(asientos_ocupados) lista de los asientos que se encuentran ocupados
    if op=="1":
        mostrar_opciones() #solo lo muestra cuando la opción es 1 en el menu mostrar_opciones; si es op==2 (Compra de asientos), tambien visualiza los asientos, pero no vuelve a mostrar las opciones, sino que continua con la compra de asientos.

def ingreso(): #función registrar datos del pasajero: 
    global cliente
    nombre= input("\nIngrese su nombre: ")
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            rut= int(input("Ingrese su rut, sin punto ni guión, ni dígito veriicador: "))
            rut_test= rut     #Se crea una variable alterna para no tocar el rut ingresado que debe tener 8 a 9 digitos (sin considerar puntos ni guion).
            cont=0
            while rut_test>0:
                cont=cont+1              #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera, mientras sea mayor a 0.
                rut_test= rut_test//10
            if cont<7 or cont>8:
                print("rut inválido")
            else:
                rut= str(rut)+"-"+digito_verificador(rut)
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")      
            
    while(True):
        try:
            celular= int(input("Ingrese su número de celular sin anteponer el 9: "))
            celular_test= celular  #Se crea una variable alterna para no tocar el número de telefono que 8 digitos exactos (sin considerar el 9 o +569).
            cont=0
            while celular_test>0:
                cont=cont+1                #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera , mientras sea mayor a 0.
                celular_test= celular_test//10 
            if cont!=8: #si la cantidad ingresada no es 8 exacta no deja continuar hasta qu sea la cantidad de 8 números exactos.
                print("Telefono inválido")
            else:
                celular="+569 "+str(celular)
                banco= input("Si pertenece al banco 'bancoDuoc'('15%' de descuento), presione 'B', de lo contrario ingrese su banco: ").upper()
                global descuento
                if banco=="B":
                    descuento=0.15
                    banco="bancoDuoc" 
                else:
                    descuento=0
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")    
    print("\nDatos ingresados correctamente\n\n")
    cliente={"Nombre":nombre,"Rut":rut,"Celular":celular,"Banco":banco} #completados los datos correctamente, guardamos los datos del cliente en un diccionario.
    
def comprar_asiento(): #función comprar asientos, llama a la funcion ingreso, para registrar al usuario, y luego llama a la funcion mostrar asientos (para indicar cuales se encuentran disponibles)
    global asientos_ocupados
    global cliente
    ingreso()
    retorno="R"
    while retorno=="R": 
        try:  
            conf="" #creamos la variable conf (de confirmación) para cuando se utilice en el ciclo while para confirmar asiento o cambiarlo
            mostrar_asientos()
            print("Los asientos marcados con una X, no se encuentran disponibles.\nDesde el asiento 31 al 42 son para pasajeros VIP.\n\nLos precios son:\n\n - Asiento normal: $ 78.900\n - Asiento VIP: $ 240.000\n")
            eleccion=int(input("Favor, Seleccione un asiento: "))
            while eleccion in asientos_ocupados or eleccion<=0 or eleccion>42:
                eleccion=int(input("Ese asiento no esta disponible, favor seleccione otro asiento: "))
            else:
                asiento_escogido={"Asiento":eleccion}
                cliente.update(asiento_escogido)
                if 0<eleccion and eleccion<31:
                    precio=78900
                elif 31<=eleccion and eleccion<43:
                    precio=240000
                precio= round(precio-precio*descuento)
                print(f"El precio a pagar es de: $ {precio}.") 
                if(descuento==0.15):
                    print("Descuento aplicado por perternecer a 'bancoDuoc': 15%")
                while(conf != "S" and conf != "C" and conf != "M"):
                    conf=input("\n  - Para confirmar asiento, presione S.\n  - Para cambiar asiento presione C.\n\nOpcion: ").upper()
                else:
                    if conf=="S":
                        print(lista_vuelo)
                        lista_vuelo.append(cliente.copy())
                        asientos_ocupados=[] #vacio de la lista, de asientos ocupados y la actualizo según la lista de vuelo, asi no se generan datos repetitivos.
                        print(asientos_ocupados)
                        print(lista_vuelo)
                        for asiento in lista_vuelo: #De acuerdo a la lista de vuelo, toma el valor de la clave Asiento - en ciclo se usa "asiento"  para hacerlo más representativo
                            asientos_ocupados.append(asiento["Asiento"])
                        np.save('file.npy', lista_vuelo) #actualizamos la lista de vuelo en nuestro archivo donde registramos los pasajeros con sus datos y asientos.
                        print(asientos_ocupados)
                        print("Asiento asignado, sus datos son los siguientes:\n")
                        for datos in cliente:
                            print(datos,":",cliente[datos])
                        print("\nDisfrute su vuelo, gracias por preferir Vuelos-Duoc.\n")
                        break
                    elif conf=="C":
                        cliente.popitem() #elimina solo el asiento del diccionario cliente
                        eleccion=0
                        retorno="R"
        except: 
            print("Error de ingreso, favor vuelva a intentar")  
    mostrar_opciones()  
    
def modificar(): #modifica los datos del usuario solicitando la comparacionde rut & número de asiento deontre del registro de compras de asientos.
    index=0
    asiento_mod=0000000
    op_chance="0" # opción inicializada de cambio.
    print("Para realizar esta opción, necesitamos válidar sus datos.")
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            rut_mod= int(input("Ingrese su rut, sin punto ni guión, ni dígito veriicador: "))
            rut_test= rut_mod    #Se crea una variable alterna para no tocar el rut ingresado que debe tener 8 a 9 digitos (sin considerar puntos ni guion).
            cont=0
            while rut_test>0:
                cont=cont+1              #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera, mientras sea mayor a 0.
                rut_test= rut_test//10
            if cont<7 or cont>8:
                print("rut inválido")
            else:
                rut_mod= str(rut_mod)+"-"+digito_verificador(rut_mod)
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")   
    for test in lista_vuelo:
        index=index+1
        if rut_mod==test["Rut"]: #compara el rut ingresado, con los rut de la lista base de rut de pasajeros
            asiento_mod= test["Asiento"] #obtengo el asiento asociado al rut en cuestión
            #print(index)    # prueba el indique que nos encontramos
            #print(asiento_mod)    # muestra el asiento asociado al rut correcto. (solo para ir comprobando) 
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            asiento_cambio= int(input("indique su asiento: ")) 
        except:
            print("Error de ingreso") 
        if(asiento_cambio==asiento_mod): #comparo el asiento ingresado con el que ya tengo asociado al rut, si se cumple, se visualiza el submanu de acontinuación, y sino vuelve al menu principal
            while(op_chance != "1" and op_chance != "2"):
                op_chance= input("Ingrese una opcion:\n \n1. Cambiar nombre \n2. Modificar teléfono \n\nOpcion: ")
            else:
                if op_chance=="1":
                    cliente_chance=(lista_vuelo[index-1]) # usamos el index obtenido anteriormente -1, pues el indice comienza desde 0.
                    cliente_chance["Nombre"]= input("\nIngrese nuevo nombre: ")
                    lista_vuelo[index-1]=cliente_chance
                    print("\nDatos modificados correctamente:\n")
                    for datos in cliente_chance:
                        print(datos,":",cliente_chance[datos])
                    print("") #salto     
                elif op_chance=="2":
                    while(True):
                        try:
                            celular_new= int(input("Ingrese su nuevo número de celular, sin anteponer el 9: "))
                            celular_test= celular_new  #Se crea una variable alterna para no tocar el número de telefono que 8 digitos exactos (sin considerar el 9 o +569).
                            cont=0
                            while celular_test>0:
                                cont=cont+1                #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera , mientras sea mayor a 0.
                                celular_test= celular_test//10 
                            if cont!=8:
                                print("Telefono inválido")
                            else:
                                celular_new="+569 "+str(celular_new)
                                cliente_chance_cel=(lista_vuelo[index-1]) # usamos el index obtenido anteriormente -1, pues el indice comienza desde 0. accedemos al diccionario correspondiente a su index
                                cliente_chance_cel["Celular"]= celular_new #modificamos el celular 
                                lista_vuelo[index-1]=cliente_chance_cel
                                print("\nDatos modificados correctamente:\n")
                                for datos in cliente_chance_cel:
                                    print(datos,":",cliente_chance_cel[datos])
                                print("") #salto     
                                break
                        except:
                            print("Error de ingreso, favor vuelva a intentar")  
                break 
        else:
            print("\nCombinación rut-asiento errónea\n")
            break
    np.save('file.npy', lista_vuelo) #actualizamos la lista de vuelo
    mostrar_opciones()

def anular_vuelo():
    global cliente
    respuesta=""
    cantidad_pasajeros_actual=len(lista_vuelo) 
    if cantidad_pasajeros_inicial<cantidad_pasajeros_actual: #nos aseguramos que no pueda eliminar otros pasajeros de anteriores compras.
        while (respuesta!="S" and respuesta!="N"):
            print("¿Esta seguro que desea eliminar su compra asociada a los siguientes datos? (S/N):\n")
            for datos in cliente:
                print(datos,":",cliente[datos])
            respuesta= input("\nRespuesta: ").upper()
        else:
            if respuesta=="S":
                cliente={}
                lista_vuelo.pop()
                asientos_ocupados.pop() #eliminamos el asiento en nuestra lista de asientos ocupados.
                print("\n*** Compra anulada ***\n")
            elif respuesta=="N":
                print("\n***Su compra no ha sido anulada*** \n")
            else:
                print("Opción, inválida, ingrese nuevamente.")
    else:
        print("\nOpción inválida, usuario no tiene compra asociada.\n")
    np.save('file.npy', lista_vuelo) #actualizamos la lista de vuelo
    mostrar_opciones()

def mostrar_opciones(): #creacion de menu principal
    global op
    op=""
    while(op != "1" and op != "2" and op != "3" and op != "4" and op != "5"):
        op= input("Ingrese una opcion:\n \n1. Ver asientos disponibles \n2. Comprar asiento \n3. Anular vuelo \n4. Modificar datos de pasajero \n5. Salir\n\nOpcion: ")
        print("") #salto
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
            np.save('file.npy', lista_vuelo) #Cierra el programa, y guarda los cambios sobreescribiendo el archivo npy, donde almacenamos nuestra lista de pasajeros con su respectivo asiento
            print("\n¡ Hasta pronto !\n")

#funcion para calcular digito verificador: (funcion extra, como bunus)
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11==10:
        return "k"
    else:
        return str((-s) % 11)
