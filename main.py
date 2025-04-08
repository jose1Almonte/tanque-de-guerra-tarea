from Tanque import Tanque

# lista = []
# #faltó pasarle la lista al constructor
# tanque = Tanque("terminator",lista)
# tanque2 = Tanque("maquina de guerra", lista)
# tanque3 = Tanque("tanque de agua", lista)

# lista.append(tanque)
# lista.append(tanque2)
# lista.append(tanque3) #recuerda que python ahorra memoria, es decir,
# # Al yo modificar la lista en la linea 3, las instancias son conscientes
# # de los cambios que yo le haga a dicha lista, no importa cuando

# tanque.apuntar()
# tanque.cargar() #me faltó cargar balas jajaj
# # lo bueno de esto es que me di cuenta que falta un mensaje que avise cuando no tenga balas
# tanque.disparar()

# # Ok, ya habiendo probado eso, antes de hacer el menú, hagamos
# # el metodo encargado de tunear el tanque
# # listo el tuneo, podemos probarlo
# tanque.cargar()
# tanque.tunear_tanque()
# #por ultimo, probemos el disparo sin apuntar
# tanque.cargar() 
# tanque.disparar()
# #probemos de una vez a ver si disparó dos balas, al cargar 1, deberia de haber una bala
# tanque.cargar() 
# # ahora si funciona. Recomiendo que, al hacer un proyecto, siempre trabajen
# # en un repositorio, asi tendran "checkpoints" por si en algun momento
# # su codigo no funciona y no encuentran el error
# #Ahora si podremos comenzar con el menu encargado de crear mas tanques
# #para luego, cuando inicie la guerra, podramos rotar el turno de los tanques uno
# #por uno. En resumen, tendremos dos menus (mientras lo hacemos veremos si
# # necesitaremos mas)
#Lo dejaré todo comentado para empezar aqui mismo.

def main():
    # Creamos una lista vacia para almacenar los tanques
    lista_tanques = []
    # Creamos un bucle para que el usuario pueda crear tantos tanques como desee
    # o comenzar el juego

    while True:
        #No hay error, pero quiero mejorar la estetica
        print("\nBienvenido al juego de tanques 💣. que deseas hacer?")
        print("1. Crear un tanque")
        print("2. Comenzar el juego")
        print("3. Salir")
        # Pedimos al usuario que ingrese su opción
        opcion = int(input("Ingrese su opción: "))
        # Si el usuario elige la opción 1, creamos un tanque
        if opcion == 1:
            crear_tanque(lista_tanques) # llamaremos a una funcion para que se encargue de crear el tanque
        # Si el usuario elige la opción 2, comenzamos el juego
        elif opcion == 2:
            juego(lista_tanques) # Aqui iria el juego, usaremos otra funcion para ello
        # Si el usuario elige la opción 3, salimos del juego
        elif opcion == 3:
            print("Hasta luego")
            break

def crear_id_tanque(lista_tanques):
    while True:
        repetir_ciclo = False
        id_tanque = input("Por favor, ingrese el nombre de su tanque: ")
        for tanque in lista_tanques:
            tanque: Tanque
            #nota, al id de la clase tanque no le salen opciones porque python cree
            # que puede ser cualquier cosa
            # esto es mas estetica, pero lo podemos solucionar facil
            # con eso ya le indicamos a python que el id siempre será str
            if tanque.id.lower() == id_tanque.lower():
                print("El nombre de tanque ya existe, por favor ingrese otro nombre")
                repetir_ciclo = True
        
        if repetir_ciclo: continue
        return id_tanque

def crear_tanque(lista_tanques: list):
    id_tanque = crear_id_tanque(lista_tanques)
    tanque = Tanque(id_tanque,lista_tanques)
    lista_tanques.append(tanque) # no siempre deberia yo de añadirlo
    # sin modificar esta parte 

def juego(lista_tanques: list):
    while(not queda_un_tanque_en_pie(lista_tanques)):
        pasar_una_ronda(lista_tanques)

#El juego no acabará hasta que quede solo 1 tanque en pie

def queda_un_tanque_en_pie(lista_tanques: list):
    tanques_en_pie = []

    for tanque in lista_tanques:
        tanque: Tanque
        if tanque.vidas > 0: 
            tanques_en_pie.append(tanque)
    nro_tanques_en_pie = len(tanques_en_pie)
    print(nro_tanques_en_pie)
    if nro_tanques_en_pie == 1: 
        print("Queda solo un tanque en pie!")
        print(f"FELICIDADES {tanques_en_pie[0].id}")
        return True
    
    return False

def pasar_una_ronda(lista_tanques: list):
    for tanque in lista_tanques:
        tanque: Tanque
        if tanque.vidas > 0:
            menu_opciones_tanque(tanque)

def menu_opciones_tanque(tanque: Tanque):
    # Pongamos primero la informacion del tanque
    print(f"\nTanque {tanque.id} 💣")
    print(f"Vidas: {tanque.vidas}")
    print(f"Balas: {tanque.balas_cargadas}/{tanque.balas_cap}")
    print("Que deseas hacer en el turno de este tanque?")
    print(f"1. Apuntar (apuntando a: {tanque.apuntando})") #simplemente para ayudar al usuario a saber
    print("2. Disparar")
    print(f"3. Cargar bala ({tanque.balas_cargadas}/{tanque.balas_cap})") #en singular, porque solo carga una 
    print("4. Tunear")
    # print("3. Moverse") # Buena idea de la ia, me lo puedo guardar para un futuro
    opcion = int(input("> "))
    
    match (opcion):
        case 1:
            tanque.apuntar()
        case 2:
            tanque.disparar()
        case 3:
            tanque.cargar()
        case 4:
            tanque.tunear_tanque()

# excelente, probemos lo que llevamos llamando a main
main()

#A, bueno veamos que faltó en la seccion de crear un tanque

#Parece que funciona muy bien, solo falta detalles para hacerlo mas entendible

# Ya luego podremos hacer que el jugador no pierda turnos luego de ingresar un dato erroneo

# Eso fue todo, si quieren que le agregue algo mas o tienen alguna idea
# La pueden dejar en los comentarios
# Tendran acceso a este proyecto a traves del link al github que dejaré en la 
#descripcion de este video

#Ahora parece que está todo bien, deja tu like... :)