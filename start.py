#import sys
import random
import time

global nombre #una variable globlal donde se guardará el nombre del jugador
def intro():
   fullname = input("Hola, bienvenido al reto sofka, ingresa tu nombre y apellido por favor \n").split() #separa el nombre y apellido por posiciones
   time.sleep(1)
   print("Hola " + fullname[0] + " el juego es el siguiente: Vas a responder preguntas de selección multiple con única respuesta, podrás escoger entre A,B,C,D. ")
   time.sleep(1)
   print("Si respondes bien, avanzarás a la siguiente ronda y ganarás dinero,pero si pierdes, lo perderás todo." + 
         " \n Cada vez que avances, las preguntas serán más difíciles, ánimo!")
   return fullname




