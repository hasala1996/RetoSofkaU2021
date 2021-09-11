import pandas as pd
class Player():
    def __init__(self,fullName):
        self.fullName=fullName
        self.score = 0
        self.book = None

    def obtainscore(self):
        return self.score

    def dfRegister(self,level):
        self.book = pd.read_excel('Base_Datos_Jugadoros_Historicos.xlsx', sheet_name= 'Sheet1', index_col=[0])
        newdata = {'Nombre':self.fullName[0],'Puntaje Obtenido':self.score,'Nivel alcanzado': level}
        self.book = self.book.append(newdata, ignore_index = True)
        self.book.to_excel("Base_Datos_Jugadoros_Historicos.xlsx","Sheet1")
        print(self.book)
    




