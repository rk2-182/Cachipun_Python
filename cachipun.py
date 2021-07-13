"""https://pypi.org/project/playsound/"""

import random
import time
import os
#from playsound import playsound
import pygame

class Cachipun:

    tijera = chr(9996)
    papel = chr(9995)
    piedra = chr(9994)
    puntosH = 0
    puntosM = 0
    repeticiones = 0
    pygame.mixer.init()

    #Constructor con parametros recibe la cancion a tocar.
    def __init__(self,cancion):
        
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play(loops=-1) #loop infinito con -1
    
    # Metodos
    def maquina(self):
        # generar 'jugada' aleatoria
        self.__jugada = random.randrange(0, 3)  # atributo privado
        if self.__jugada == 0:
            return 'piedra'
        if self.__jugada == 1:
            return 'papel'
        if self.__jugada == 2:
            return 'tijera'

    def presentacion(self,cantidad):
        os.system('cls')
        print("*********Bienvenido al juego Cachipun Maquina Vs Humano a {} jugada(s)*********".format(cantidad))
        print("Opciones: ")

        print("1.-tijera = ", self.tijera)
        print("2.-piedra = ", self.piedra)
        print("3.-papel = ", self.papel)
        

    def humano(self):
        time.sleep(1)
        self.opcionH = int(input("Ingrese su opcion: (1={},2={},3={})".format(
            self.tijera, self.piedra, self.papel)))

        if self.opcionH == 1:
            return 'tijera'
        if self.opcionH == 2:
            return 'piedra'
        if self.opcionH == 3:
            return 'papel'

    def jugar(self,jugadas):
        
        self.repeticiones = 1
        #self.puntosH = 0
        #self.puntosM = 0

        # 0 reps es menor a 3? si es asi entrar en ciclo
        while self.repeticiones <=jugadas:
            print("\nRonda numero #{}".format(self.repeticiones))
            # guardar en una variable la opcion humana ingresada
            # ejecutamos la funcion humano la cual pedira ingresar por teclado una opcion
            resultadoHumano = self.humano()

            # guardar en una variable el resultado aleatorio de la maquina
            # se ejecuta la opcion maquina y esta aleatoriamente generara su opcion
            resultadoMaquina = self.maquina()
          
            print("Humano a jugado: {}".format(resultadoHumano))
          
            print("Maquina a jugado:{}".format(resultadoMaquina))

            # *****************buscar ganador****************************

            # Piedra:
            # Empate humano
            if resultadoHumano == 'piedra' and resultadoMaquina == 'piedra':
                self.puntosH += 0
                self.puntosM += 0
                time.sleep(0.5)
                print("Piedra vs Piedra Empate!")
            # Pierde humano
            elif resultadoHumano == 'piedra' and resultadoMaquina == 'papel':
                self.puntosH += 0
                self.puntosM += 1
                time.sleep(0.5)
                print("Piedra vs Papel Gana Papel")
            # Gana humano
            elif resultadoHumano == 'piedra' and resultadoMaquina == 'tijera':
                self.puntosH += 1
                self.puntosM += 0
                time.sleep(0.5)
                print("Piedra vs Tijera Gana Piedra!")

            # Papel:
            # Gana humano
            if resultadoHumano == 'papel' and resultadoMaquina == 'piedra':
                self.puntosH += 1
                self.puntosM += 0
                time.sleep(0.5)
                print("Papel vs Piedra gana Papel!")
            # Empate humano
            elif resultadoHumano == 'papel' and resultadoMaquina == 'papel':
                self.puntosH += 0
                self.puntosM += 0
                time.sleep(0.5)
                print("Papel vs Papel Empate!")
            # Gana maquina
            elif resultadoHumano == 'papel' and resultadoMaquina == 'tijera':
                self.puntosH += 0
                self.puntosM += 1
                time.sleep(0.5)
                print("Papel vs tijera gana Tijera!")

            # Tijera:
            # Pierde humano
            if resultadoHumano == 'tijera' and resultadoMaquina == 'piedra':
                self.puntosH += 0
                self.puntosM += 1
                time.sleep(0.5)
                print("Tijera vs Piedra gana Piedra!")
            # Gana humano
            elif resultadoHumano == 'tijera' and resultadoMaquina == 'papel':
                self.puntosH += 1
                self.puntosM += 0
                time.sleep(0.5)
                print("Tijera vs papel gana Tijera!")
            # Empate maquina
            elif resultadoHumano == 'tijera' and resultadoMaquina == 'tijera':
                self.puntosH += 0
                self.puntosM += 0
                time.sleep(0.5)
                print("Tijera vs tijera Empate!")

            self.repeticiones += 1

            time.sleep(2)
            print("\nResultado puntos: ")
            print("==============================")
            print("Humano: {}".format(self.puntosH))
            print("Maquina: {}".format(self.puntosM))


            #Evaludar si algun jugador ya va 2 a 0 terminando el bucle por reglas del juego.
            if self.puntosM >=2 and self.puntosH == 0:
                #self.ganador()
                break
            if self.puntosH >=2 and self.puntosM == 0:
                #self.ganador()
                break
        
        return jugadas
           


    def ganador(self):
        if self.puntosH > self.puntosM:
            print("Enhorabuena Humano haz ganado!")
        elif self.puntosH < self.puntosM:
            print("Maquina a ganado, Jajaja >:)")
        else:
            print("Han Empatado!")

        if self.puntosH == self.puntosM:
            print("*****Desempate a muerte!*****")
            self.jugar(1)
            self.ganador()

            
        
# =========Crear objeto de la clase cachipun=========
maquina = Cachipun('Boss-Fight.mp3')
os.system('cls')
jugadas = int(input("A la primera o tercera? (1 o 3): "))

maquina.presentacion(jugadas)
cantidad_jugadas = maquina.jugar(jugadas)
#maquina.jugar(3)
maquina.ganador()

print("**********************************************************************************")
input("PRESIONE ENTER PARA SALIR")
print("Fin")
exit()



