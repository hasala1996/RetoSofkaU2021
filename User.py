import pandas as pd
class Player():                     #Clase Player con metodos
    def __init__(self,fullName):
        self.fullName=fullName
        self.score = 0
        self.book = None

    def dfRegister(self,level):   # metodo par registrar en archivo Excel el histórico de jugadores con nombre completo, puntajes y niveles.
        self.book = pd.read_excel('Base_Datos_Jugadoros_Historicos.xlsx', sheet_name= 'Sheet1', index_col=[0])
        newdata = {'Nombre':self.fullName[0],'Apellido':self.fullName[1],'Puntaje Obtenido':self.score,'Nivel alcanzado': level}
        self.book = self.book.append(newdata, ignore_index = True)
        self.book.to_excel("Base_Datos_Jugadoros_Historicos.xlsx","Sheet1")
        print(self.book)
    




