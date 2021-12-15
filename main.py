import pandas as pd



class App:

    def __init__(self):
        pass

class Escalas:

    def __init__(self, posto, sequence_black, sequence_red):
        self.posto = posto
        self.sequence_black = sequence_black
        self.sequence_red = sequence_red
        self.posto = posto


class Aluno:

    def __init__(self, **args):
        """
        args = {
            "Name": ,
            "Number": ,
            "Disp_bool": ,
            "Disp_lim" ,
            "Tur_cmd": ,
            "Last_work": ,
            "Scale_work_number": ,
            "Changes_number": ,
        }
        """

        self.war_name = args["Name"]
        self.number = args["Number"]
        self.dispensa = (args["Disp_bool"], args["Disp_lim"])
        self.tur_cmd = args["Tur_cmd"]
        self.last_work = args["Last_work"]
        self.scale_work_number = args["Scale_work_number"]#dict
        self.changes_number = args["Changes_number"]


class Posto:

    types = {0:"Permanência", 1:"Sentinela", 2:"Plantão", 3:"Cb de dia", 4:"Sgt de dia"}
    
    def __init__(self, tipo, where, people, gender, year):
        self.type = Posto.types[tipo]
        self.where = where
        self.people = int(people)
        self.gender = gender
        self.year = year






