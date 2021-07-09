import random

class Cachipun:
      
    #Metodo
    def maquina(self):
        #generar 'jugada' aleatoria
        self.__jugada = random.randrange(0,3) #atributo privado
        if self.__jugada == 0:
            return 'piedra'
        if self.__jugada == 1:
            return 'papel'
        if self.__jugada == 2:
            return 'tijera'

    def humano(self):
     
        self.opcionH = int(input("Ingrese su opcion: (1=tijera,2=piedra,3=papel)"))

        if self.opcionH == 1:
            return 'tijera'
        if self.opcionH == 2:
            return 'piedra'
        if self.opcionH == 3:
            return 'papel'

    def jugar(self):
        repeticiones = 0
        puntosH = 0
        puntosM = 0

        #0 reps es menor a 3? si es asi entrar en ciclo
        while repeticiones < 3:
            #guardar en una variable la opcion humana ingresada
            resultadoHumano = self.humano()

            #guardar en una variable el resultado aleatorio de la maquina
            resultadoMaquina=self.maquina()

            print("Maquina:{}".format(resultadoMaquina))
            print("Humano: {}".format(resultadoHumano))
            #*****************buscar ganador****************************
            #Piedra:
            #Empate humano
            if resultadoHumano == 'piedra' and resultadoMaquina == 'piedra':
                puntosH +=1
                puntosM +=1
            #Pierde humano
            elif resultadoHumano == 'piedra' and resultadoMaquina == 'papel':
                puntosH+=0
                puntosM+=1
            #Gana humano
            elif resultadoHumano == 'piedra' and resultadoMaquina == 'tijera':
                puntosH+=1
                puntosM+=0
            
            #Papel:
            #Gana humano
            if resultadoHumano == 'papel' and resultadoMaquina == 'piedra':
                puntosH +=1
                puntosM +=0
            #Empate humano
            elif resultadoHumano == 'papel' and resultadoMaquina == 'papel':
                puntosH+=1
                puntosM+=1
            #Gana maquina
            elif resultadoHumano == 'papel' and resultadoMaquina == 'tijera':
                puntosH+=0
                puntosM+=1
            
            #Tijera:
            #Pierde humano
            if resultadoHumano == 'tijera' and resultadoMaquina == 'piedra':
                puntosH +=0
                puntosM +=1
            #Gana humano
            elif resultadoHumano == 'tijera' and resultadoMaquina == 'papel':
                puntosH+=1
                puntosM+=0
            #Empate maquina
            elif resultadoHumano == 'tijera' and resultadoMaquina == 'tijera':
                puntosH+=1
                puntosM+=1
            

            repeticiones+=1

            print("\nResultado puntos: ")
            print("******************************")
            print("Maquina: {}".format(puntosM))
            print("Humano: {}".format(puntosH))

        
#=========Crear objeto de la clase cachipun=========
maquina = Cachipun()

maquina.jugar()

print("Fin")



