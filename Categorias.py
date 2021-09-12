import random
import time

class Category():
    
    def __init__(self,ctgria):                                   #constructor de la clase Category
        self.nume=ctgria
        self.answer= None   

    def obtenerdoc(self):                                       # metodo para obtener del documento,toda la info 
        listaPregunta = list(open("categoria%s.txt"%self.nume))
        self.obtenerPregResp(listaPregunta)    
        
    def obtenerPregResp(self,listaPregunta):                    # metodo para obtener del documento,la lista de pregutas y respuesta

        data = listaPregunta.pop(random.randint(0,len(listaPregunta) - 1))
        items = data.split('[')
        global question
        question = items[0]
        #print(question)
        global answers
        answers = items[1].strip("\n").split(',')
        
        print('Pregunta número:', self.nume, "por", self.nume*100, "dolares")
        time.sleep(1)
        print(question)
        time.sleep(1)
        print('A: ' + answers[0])
        time.sleep(1)
        print('B: ' + answers[1])
        time.sleep(1)
        print('C: ' + answers[2])
        time.sleep(1)
        print('D: ' + answers[3])
        time.sleep(1)

        
        global listaR 
        listaR = {
        'A' : answers[0],
        'B' : answers[1],
        'C' : answers[2],
        'D' : answers[3],
        }
    
    def validarRespuesta(self,respuesta):       # metodo para validar respuestas ingresadas 

        if respuesta in listaR:
            if listaR[respuesta] == answers[4]:
                time.sleep(1)
                print('\n' + 'Muy bien, la respuesta es correcta.' + "\n")
                return True
            else:
                print("Haz fallado, la respuesta correcta es:", str(answers[4]) + "!")
                return False
        else: 
            print('Tu respuesta no se reconoce como válida, tu juego a finalizado')
            return False