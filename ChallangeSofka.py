# se importan las librerias y archivos necesarios
import random
import time
import start
import Categorias
import User
import test

# se captura el nombre del jugador y se usa el metodo intro del archivo start.
fullname = start.intro()  
user = User.Player(fullname) # se instancia la clase Player 

# variables de categoría y premio acumulado
global cat
cat = 1
acumulado=0

# se ejecuta un while que valida las rondas del juego dependieno la catagoria
while  cat <= 5:

    docQuestion = Categorias.Category(cat) # se instancia la clase Category para hacer uso de sus metodos
    docQuestion.obtenerdoc()

    respuesta= input("Por favor digite su respuesta \n")
    respuesta = respuesta.upper()

    ##uso del metodo validar respuesta de la clase Category
    val = docQuestion.validarRespuesta(respuesta) 
    if val == False:
        user.score = 0
        print("Ha perdido todo su puntaje, lo sentimos")
        user.dfRegister(cat)
        break
    #print(val)
    acumulado += 100
    user.score = acumulado
    print("Su acumulado hasta el momento es: ", acumulado)
    
    if cat==5:
        print('Felicidades, haz completado todos los niveles del juego, tu premio es de %i dolares'%user.score)
        user.dfRegister(cat)# metodo dfRegister 
    else:
        nextRound = input("Presione cualquier tecla para retirarse con su acumalado de : %i  dólares o S si quiere continuar: " %user.score).upper()
        if nextRound != 'S' :
            print('Ha decidido retirarse con su dinero, felicides, te llevas %i  dolares, hasta pronto: ' %user.score)
            user.dfRegister(cat)
        #user.score
            break


    cat += 1





    
   




