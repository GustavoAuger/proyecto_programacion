import numpy as np

def mostrar_asientos():
    a=0
    b=0
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
    print(lista_vueloL)
    #print(asientos_ocupados)
    if op=="1":
        mostrar_opciones() #solo lo muestra cuando la opción es 1 en el menu mostrar_opciones; si es op==2 (Compra de asientos), tambien visualiza los asientos, pero no vuelve a mostrar las opciones, sino que continua con la compra de asientos.

def ingreso(): #función registrar datos del pasajero:
    nombre= input("\nFavor ingrese su nombre: ")
    rut=0    
    celular=0
    banco=0
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            rut= int(input("ingrese su rut, sin punto ni guión: "))
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
                banco= input("Si pertenece al banco 'bancoDuoc'('15%' de descuento), presione 'B', de lo contrario ingrese su banco: ").upper()
                global descuento
                if banco=="B":
                    descuento=0.15
                else:
                    descuento=0
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")    
    print("\nDatos ingresados correctamente\n\n")
    global cliente
    cliente={"Nombre":nombre,"Rut":rut,"Celular":celular,"Banco":banco} #completados los datos correctamente, guardamos los datos del cliente en un diccionario.

#función comprar asientos:

def comprar_asiento():
    global asientos_ocupados
    ingreso()
    retorno="R"
    while retorno=="R":
        conf="" #creamos la variable conf (de confirmación) para cuando se utilice en el ciclo while para confirmar asiento o cambiarlo
        retorno=""
        mostrar_asientos()
        print("Los asientos marcados con una X, no se encuentran disponibles.\nDesde el asiento 31 al 42 son para pasajeros VIP.\n\nLos precios son:\n\n - Asiento normal: $ 78.900\n - Asiento VIP: $ 240.000\n")
        eleccion=int(input("Favor, Seleccione un asiento: "))
        while eleccion in asientos_ocupados:
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
                    lista_vueloL.append(cliente.copy())
                    asientos_ocupados=[] #vacio de la lista, de asientos ocupados y la actualizo según la lista de vuelo, asi no se generan datos repetitivos.
                    print(asientos_ocupados)
                    for asiento in lista_vueloL: #De acuerdo a la lista de vuelo, toma el valor de la clave Asiento 
                        asientos_ocupados.append(asiento["Asiento"])
                    np.save('file.npy', lista_vuelo) #actualizamos la lista de vuelo en nuestro archivo donde registramos los pasajeros con sus datos y asientos.
                    print(asientos_ocupados)
                    print("Asiento asignado, sus datos son los siguientes:\n")
                    for datos in cliente:
                        print(datos,":",cliente[datos])
                    print("\nDisfrute su vuelo, gracias por preferir Vuelos-Duoc.\n")
                    mostrar_opciones()
                elif conf=="C":
                    cliente.popitem()
                    eleccion=0
                    retorno="R"
def modificar():
    index=0
    asiento_mod=0000000
    op_chance="0" # opción inicializada de cambio.
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            rut_mod= int(input("ingrese su rut, sin punto ni guión: "))
            rut_test1= rut_mod     #Se crea una variable alterna para no tocar el rut ingresado que debe tener 8 a 9 digitos (sin considerar puntos ni guion).
            cont=0
            while rut_test1>0:
                cont=cont+1              #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera, mientras sea mayor a 0.
                rut_test1= rut_test1//10
            if cont<8 or cont>9:
                print("Rut inválido")
            else:
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")
    for test in lista_vueloL:
        index=index+1
        if rut_mod==test["Rut"]:
            asiento_mod= test["Asiento"]
            print(index)
            print(asiento_mod)
    while(True): #validamos que la entrada sea del tipo entero, división sobre 0 
        try:
            asiento_cambio= int(input("indique su asiento: "))
        except:
            print("Error de ingreso") 
        if(asiento_cambio==asiento_mod):
            while(op_chance != "1" and op_chance != "2"):
                op_chance= input("Ingrese una opcion:\n \n1. Cambiar nombre \n2. Modificar teléfono \n\nOpcion: ")
            else:
                if op_chance=="1":
                    cliente_chance=(lista_vueloL[index-1]) # usamos el index obtenido anteriormente -1, pues el indice comienza desde 0.
                    cliente_chance["Nombre"]= input("\nFavor ingrese nombre a cambiar: ")
                    lista_vueloL[index-1]=cliente_chance
                    print("\nDatos modificados correctamente:\n")
                    for datos in cliente:
                        print(datos,":",cliente_chance[datos])
                elif op_chance=="2":
                    while(True):
                        try:
                            celular_new= int(input("Ingrese su número de celular sin anteponer el 9: "))
                            celular_test= celular_new  #Se crea una variable alterna para no tocar el número de telefono que 8 digitos exactos (sin considerar el 9 o +569).
                            cont=0
                            while celular_test>0:
                                cont=cont+1                #cuenta la cantidad de digitos al repetirse el siglo de la divion parte entera , mientras sea mayor a 0.
                                celular_test= celular_test//10 
                            if cont!=8:
                                print("Telefono inválido")
                            else:
                                cliente_chance_cel=(lista_vueloL[index-1]) # usamos el index obtenido anteriormente -1, pues el indice comienza desde 0.
                                cliente_chance_cel["Celular"]= celular_new
                                lista_vueloL[index-1]=cliente_chance_cel
                                print("\nDatos modificados correctamente:\n")
                                for datos in cliente:
                                    print(datos,":",cliente_chance_cel[datos])
                                break
                        except:
                            print("Error de ingreso, favor vuelva a intentar")  
                break 
        else:
            print("\nCombinación rut-asiento errónea\n")
    print("\n")
    mostrar_opciones()

def anular_vuelo():
    cantidad_pasajeros_actual=len(lista_vueloL) 
    if cantidad_pasajeros_inicial<cantidad_pasajeros_actual: #nos aseguramos que no pueda eliminar otros pasajeros de anteriores compras.
        cliente={}
        print(cliente)
        lista_vueloL.pop()
        print("\n*** Compra anulada ***\n.")
        mostrar_opciones()
    else:
        print("\nOpción inválida, usuario no tiene compra asociada.\n")
        mostrar_opciones()

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

asientos= np.zeros((7,6)) # inicio del programa creamos la matriz de los asientos y damos la bienvenida
i=1
for c in range(7):
    for f in range(6):
        asientos[c][f]=i
        i=i+1
print("¡ Bienvenido a Vuelos-Duoc !\n")
#intenta abrir un registro de reservas de un archivo npy (simulando una bd), si es que existe. Sino crea un un archivo npy:
try:
    asientos_ocupados=[] # creamos la lista asientos ocupados
    cliente = {} #Se define como diccionario la variable cliente, guarda sus datos + su asiento.
    lista_vuelo = np.load('file.npy', allow_pickle='TRUE') #array
    for asiento in lista_vuelo: #De acuerdo a la lista de vuelo, toma el valor de la clave Asiento 
        asientos_ocupados.append(asiento["Asiento"])
    lista_vueloL=lista_vuelo.tolist() #Utilizamos el array como lista para poder acceder al metodo tradicional de append (insertar nuevos clientes) 
    cantidad_pasajeros_inicial=len(lista_vueloL) #para tener el control de la cantidad de pasajeros inicial, a la hora de eliminar el último asiento
    #print(lista_vuelo)
    mostrar_opciones() 
    
except FileNotFoundError: 
    asientos_ocupados=[] # creamos la lista Asientos ocupados
    lista_vuelo=[{"Nombre":"none","Rut":0,"Celular":0,"Banco":"none","Asiento":0}]  #Al no existir una lista de pasajeros anterior, creamos la variable lista_vuelo, con un cliente ficticio para que el valor de la clave asiento exista
    np.save('file.npy', lista_vuelo)
    lista_vuelo = np.load('file.npy', allow_pickle='TRUE')
    lista_vueloL=lista_vuelo.tolist()
    cantidad_pasajeros_inicial=len(lista_vueloL) #para tener el control de la cantidad de pasajeros inicial, a la hora de eliminar el último asiento
    mostrar_opciones()