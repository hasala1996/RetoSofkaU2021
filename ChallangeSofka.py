import random
import time
import usuario
import Categorias
import User


fullname = usuario.intro()  #llamo al metodo intro que se encuentra en usuario para iniciar juego.
user = User.Player(fullname)

global cat
cat = 1
acumulado=0

while  cat <= 5:

    docQuestion = Categorias.Category(cat)
    docQuestion.obtenerdoc()

    respuesta= input("Por favor digite su respuesta \n")
    respuesta = respuesta.upper()

    val = docQuestion.validarRespuesta(respuesta)
    if val == False:
        user.score = 0
        print("Ha perdido todo su puntaje, lo sentimos")
        break
    #print(val)
    acumulado += 100
    user.score = acumulado
    print("Su acumulado hasta el momento es: ", acumulado)
    nextRound = input("Presione cualquier tecla para retirarse con su acumalado de : %i  dólares o S si quiere continuar: " %user.score).upper()
    if nextRound != 'S' :
        print('Ha decidido retiarse con su dinero, felicides, te llevas %i  dolares, hasta pronto: ' %user.score)
        user.score
        break


    cat += 1





    
   




