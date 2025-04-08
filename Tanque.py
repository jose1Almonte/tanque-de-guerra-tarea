import copy
import random
import time

class Tanque():
    def __init__(self, id, lista_de_tanques: list, vidas = 5, balas_cap = 1):
        self.id = id
        self.vidas = vidas
        self.balas_cap = balas_cap
        self.balas_cargadas = 0
        self.apuntando = False
        self.lista_de_tanques = lista_de_tanques
    
    def cargar(self):
        if self.balas_cargadas + 1 <= self.balas_cap:
            self.balas_cargadas += 1
            print(f"El tanque {self.id} ha cargado una bala. {self.balas_cargadas}/{self.balas_cap}")
            return True
        # puse variable balas_cargadas en vez de balas_cap, igualmente cualquier de las dos deberia de servir
        # aunque no creo que el problema radique aqui
        print(f"tanque {self.id} cargado al maximo ({self.balas_cargadas} balas cargadas)")
        return False
    
    def apuntar(self):
        print("Tanques que puedes apuntar:")
        tanques = self.mostrar_otros_tanques()
        tanque = int(input("Elige un tanque: "))
        tanque = tanques[tanque-1]
        self.apuntando = tanque.id
        return tanque

    def mostrar_otros_tanques(self):
        nueva_lista = []
        nueva_lista: list[Tanque]
        for i in range(len(self.lista_de_tanques)):
            tanque = self.lista_de_tanques[i]
            tanque: Tanque
            
            if tanque.id != self.id and tanque.vidas > 0: nueva_lista.append(tanque)
            
        for i in range(len(nueva_lista)):
            tanque = nueva_lista[i]
            tanque: Tanque

            print(i+1,tanque.id)
        
        return nueva_lista
    
    def preguntar_cantidad_disparos(self):
        while True:
            try:
                print("numero")
                balas_cargadas = copy.deepcopy(self.balas_cargadas)
                print("balas disponibles:",end=" ")
                print(balas_cargadas)
                numero = int(input("Por favor, ingrese la cantidad de balas que desea disparar: "))
                if numero <= self.balas_cargadas and numero >= 0:
                    return numero
                print("Numero erroneo de balas")
            except:
                print("dato invalido, el numero de balas tiene que ser un numero entero")

    def disparar(self):
        if self.balas_cargadas > 0:
            balas_a_disparar = self.preguntar_cantidad_disparos()

            probabilidad_acierto = random.randint(0,100)
            self.balas_cargadas -= balas_a_disparar
            if balas_a_disparar == 0:
                print("No se disparo ninguna bala, perdiste el turno")
                # TODO: mmm no me gusta que pierda el turno 🤔, luego veré que hacer
            elif self.apuntando: # Si el usuario eligió a quien apuntar
                # Aqui esta el error, esta dentro de una sola condicion de nuevo
                #solución: mover la variable afuera de las condiciones
                #igual que la anterior
                #solución: mover la variable afuera de las condiciones
                probabilidad_dos = random.randint(70,80)
                
                if probabilidad_acierto <= probabilidad_dos:
                    tanque_apuntado = self.encontrar_tanque()
                    if tanque_apuntado: 
                        tanque_apuntado.recibir_disparo(balas_a_disparar)
                else:
                    self.fallar_tiro(balas_a_disparar)
                self.apuntando = False # hacemos que después no apunte a nadie
            #Aqui me faltó quitar identación
            else: # si el usuario no eligió a quien apuntar
                #aqui hacemos que se elija un tanque al azar
                tanque_apuntado = self.elegir_otro_tanque_al_azar()
                if tanque_apuntado:
                    if probabilidad_acierto <= 40:
                        tanque_apuntado.recibir_disparo(balas_a_disparar)
                    else:
                        self.fallar_tiro(balas_a_disparar)
                else:
                    print("No hay tanque a quien apuntar")
            #Con esto ya no deberia faltar nada para lo del apuntado,
            # Veamos como podemos probar todo lo que hemos hecho
        else:
            print("No hay balas para disparar")

    def fallar_tiro(self,balas_a_disparar):
        print("Fallaste el tiro")
        self.balas_cargadas -= balas_a_disparar
    
    def elegir_otro_tanque_al_azar(self):
        while True:
            numero = random.randint(0, len(self.lista_de_tanques)-1)
            tanque = self.lista_de_tanques[numero]
            tanque: Tanque
            if tanque.id != self.id and tanque.vidas > 0 and self.hay_otro_tanque_no_abatido():
                return tanque
            
            if not self.hay_otro_tanque_no_abatido():
                return None
    
    def hay_otro_tanque_no_abatido(self):
        for tanque in self.lista_de_tanques:
            tanque: Tanque
            if tanque.id != self.id and tanque.vidas > 0:
                return True
        return False


    def soy_el_tanque(self, id):
        return self.id == id
    
    def encontrar_tanque(self):
        for i in range(len(self.lista_de_tanques)): 
            tanque = self.lista_de_tanques[i]
            tanque: Tanque
            if tanque.soy_el_tanque(self.apuntando):
                return tanque
        return False
    
    def recibir_disparo(self, balas_a_disparar: int):
        self.vidas -= balas_a_disparar
        print("ATAQUE RECIBIDO DE LLENO! QUEDAN",self.vidas,"VIDAS PARA",self.id)
        if (self.vidas <= 0):
            print(self.id, "Ha sido abatido") 
            #ahora bien, hagamos que el tanque no pueda apuntar
            # a otros tanques que ya han sido abatidos
            # para eso solo modificaremos un metodo que ya hicimos anteriormente
            # y ese metodo es...
    
    def tunear_tanque(self):
        if self.vidas < 5:
            self.vidas += 1
            print(f"recuperacion de vida de {self.id}: {self.vidas}/5!🍃")
        
        self.balas_cap += 1
        print(f"Capacidad maxima de balas aumentada a {self.balas_cap}. (cargadas actualmente: {self.balas_cargadas})")
        
        