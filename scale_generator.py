import pandas as pd
import table_control


class Search:

    def __init__(self, table):
        self.table = table


    def run_scale(self, begin, scale_name):
        lenth = len(self.table)

        name = self.table.loc[self.table[scale_name]==begin]
        pass
        for i in range(begin, lenth+1):
            self.table.loc[self.table[scale_name]==i, scale_name] -= 1

        self.table.loc[self.table["name"]==list(name["name"])[0], scale_name] = lenth


    def get_people(self, scale):

        priority = self.table.loc[self.table[scale[1]]==1]
        
        if len(priority) != 0:
            order = min(list(priority[scale[0]]))
            person = priority.loc[self.table[scale[0]]==order]
            self.table.loc[self.table["name"]== list(person["name"])[0], scale[1]] = 0
            scale_begin = list(person[scale[0]])[0]

        else:
            person = self.table.loc[self.table[scale[0]]==1]
            scale_begin = 1

        self.run_scale(scale_begin, scale[0])
        return list(person["name"])[0]


class Postos:

    def __init__(self, n, name):
        self.counter = n
        self.pessoas = ["" for i in range(n)]
        self.name = name


    def get_posto(self, scale):
        table = table_control.DataBase().get_data()
        escala = Search(table)
        lista = []
        for i in range(self.counter):
            lista.append(escala.get_people(scale))
        table_control.DataBase().save_data(escala.table)
        return lista
    
    
    
    def set_day(self):



if __name__ == "__main__":
    pan = Postos(3, "plantao ala norte")
    perm = Postos(1, "permanencia 3o piso")
    postos = [pan, perm]

    dia = {}
    for i in postos:
        dia.update({i.name:i.get_posto(("scale_black", "priority_black"))})
    
    for i in dia:
        print(i, end=': ')
        print(dia[i], end='\n')
    





