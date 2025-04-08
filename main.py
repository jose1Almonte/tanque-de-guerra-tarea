from Tanque import Tanque

lista = []
#faltó pasarle la lista al constructor
tanque = Tanque("terminator",lista)
tanque2 = Tanque("maquina de guerra", lista)
tanque3 = Tanque("tanque de agua", lista)

lista.append(tanque)
lista.append(tanque2)
lista.append(tanque3) #recuerda que python ahorra memoria, es decir,
# Al yo modificar la lista en la linea 3, las instancias son conscientes
# de los cambios que yo le haga a dicha lista, no importa cuando

tanque.apuntar()
tanque.cargar() #me faltó cargar balas jajaj
# lo bueno de esto es que me di cuenta que falta un mensaje que avise cuando no tenga balas
tanque.disparar()

# Ok, ya habiendo probado eso, antes de hacer el menú, hagamos
# el metodo encargado de tunear el tanque
# listo el tuneo, podemos probarlo
tanque.cargar()
tanque.tunear_tanque()
#por ultimo, probemos el disparo sin apuntar
tanque.cargar() 
tanque.disparar()
#probemos de una vez a ver si disparó dos balas, al cargar 1, deberia de haber una bala
tanque.cargar() 
# ahora si funciona



