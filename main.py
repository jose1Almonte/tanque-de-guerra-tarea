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

# Tomemonos un descanso... Vuelvo en unos minutos

