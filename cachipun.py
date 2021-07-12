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
    pygame.mixer.init()
    #cancion =playsound('Boss-Fight.mp3')

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

    def presentacion(self):
        os.system('cls')
        print("*********Bienvenido al juego Cachipun Maquina Vs Humano*********")
        print("Opciones: ")

        print("1.-tijera = ", self.tijera)
        print("2.-piedra = ", self.piedra)
        print("3.-papel = ", self.papel)
        

    def humano(self):
        time.sleep(2)
        self.opcionH = int(input("\nIngrese su opcion: (1={},2={},3={})".format(
            self.tijera, self.piedra, self.papel)))

        if self.opcionH == 1:
            return 'tijera'
        if self.opcionH == 2:
            return 'piedra'
        if self.opcionH == 3:
            return 'papel'

    def jugar(self):
        
        repeticiones = 0
        self.puntosH = 0
        self.puntosM = 0

        # 0 reps es menor a 3? si es asi entrar en ciclo
        while repeticiones < 3:
            
            # guardar en una variable la opcion humana ingresada
            # ejecutamos la funcion humano la cual pedira ingresar por teclado una opcion
            resultadoHumano = self.humano()

            # guardar en una variable el resultado aleatorio de la maquina
            # se ejecuta la opcion maquina y esta aleatoriamente generara su opcion
            resultadoMaquina = self.maquina()

            print("Humano: {}".format(resultadoHumano))
            print("Maquina:{}".format(resultadoMaquina))

            # *****************buscar ganador****************************
            # Piedra:
            # Empate humano
            if resultadoHumano == 'piedra' and resultadoMaquina == 'piedra':
                self.puntosH += 1
                self.puntosM += 1
                print("Piedra vs Piedra Empate!")
            # Pierde humano
            elif resultadoHumano == 'piedra' and resultadoMaquina == 'papel':
                self.puntosH += 0
                self.puntosM += 1
                print("Piedra vs Papel Gana Papel")
            # Gana humano
            elif resultadoHumano == 'piedra' and resultadoMaquina == 'tijera':
                self.puntosH += 1
                self.puntosM += 0
                print("Piedra vs Tijera Gana Piedra!")

            # Papel:
            # Gana humano
            if resultadoHumano == 'papel' and resultadoMaquina == 'piedra':
                self.puntosH += 1
                self.puntosM += 0
                print("Papel vs Piedra gana Papel!")
            # Empate humano
            elif resultadoHumano == 'papel' and resultadoMaquina == 'papel':
                self.puntosH += 1
                self.puntosM += 1
                print("Papel vs Papel Empate!")
            # Gana maquina
            elif resultadoHumano == 'papel' and resultadoMaquina == 'tijera':
                self.puntosH += 0
                self.puntosM += 1
                print("Papel vs tijera gana Tijera!")
            # Tijera:
            # Pierde humano
            if resultadoHumano == 'tijera' and resultadoMaquina == 'piedra':
                self.puntosH += 0
                self.puntosM += 1
                print("Tijera vs Piedra gana Piedra!")
            # Gana humano
            elif resultadoHumano == 'tijera' and resultadoMaquina == 'papel':
                self.puntosH += 1
                self.puntosM += 0
                print("Tijera vs papel gana Tijera!")
            # Empate maquina
            elif resultadoHumano == 'tijera' and resultadoMaquina == 'tijera':
                self.puntosH += 1
                self.puntosM += 1
                print("Tijera vs tijera Empate!")

            repeticiones += 1

            time.sleep(2)
            print("\nResultado puntos: ")
            print("******************************")
            print("Humano: {}".format(self.puntosH))
            print("Maquina: {}".format(self.puntosM))

    def ganador(self):
        if self.puntosH > self.puntosM:
            print("Enhorabuena Humano haz ganado!")
        elif self.puntosH < self.puntosM:
            print("Maquina a ganado, Jajaja >:)")
        else:
            print("Han Empatado!")
            
        
# =========Crear objeto de la clase cachipun=========
maquina = Cachipun('Boss-Fight.mp3')
maquina.presentacion()
maquina.jugar()
maquina.ganador()

print("Fin")



