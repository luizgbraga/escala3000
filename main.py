import pandas as pd


class Shell:

    def __init__(self):
        pass


class AppBone:

    def __init__(self):
        pass


class Escalas:

    def __init__(self, posto, sequence_black, sequence_red):
        self.posto = posto
        self.sequence_black = sequence_black
        self.sequence_red = sequence_red
        self.posto = posto


class Alunos:

    alunos_dir = ".Data/alunos/"

    def __init__(self, year):
        direc = Alunos.alunos_dir + str(year) + "_ano/all.json"
        alunos_df = pd.read_json(direc, orient="index")

        self.alunos = {}

        for index, key in alunos_df.iterrows():
            args = {
                "Name": key["name"],
                "Number": key["number"],
                "Gender": key["gender"],
                "Disp_lim": key["disp_lim"],
                "Tur_cmd": key["tur_cmd"],
                "Last_work": key["last_work"],
                "Works_number": key["works_number"],
                "Changes_number": key["changes_number"]
            }

            aluno = Alunos.Aluno(args)

            self.alunos[key["number"]] = aluno


    class Aluno:

        def __init__(self, args):
            """
            args = {
                "Name": ,
                "Number": ,
                "Gender": ,
                "Disp_lim": ,
                "Tur_cmd": ,
                "Last_work": ,
                "Works_number": ,
                "Changes_number": ,
            }
            """

            self.war_name = args["Name"]
            self.number = args["Number"]
            self.gender = args["Gender"]
            self.dispensa = args["Disp_lim"]
            self.tur_cmd = args["Tur_cmd"]
            self.last_work = args["Last_work"]
            self.scale_work_number = args["Works_number"]
            self.changes_number = args["Changes_number"]


class Postos:

    postos_dir = "./Data/postos/postos.json"

    def __init__(self):
        postos_df = pd.read_json(Postos.postos_dir, orient="index")
        self.postos = []
        
        for index, key in postos_df.iterrows():
            posto = Postos.Posto(key["type"], key["where"], key["people"], key["gender"], key["year"])
            self.postos.append(posto)


    def new_posto(self, type, where, people, gender, year):
        posto = Postos.Posto(type, where, people, gender, year)
        posto_dic = posto.return_dict()
        

        postos_df = pd.read_json(Postos.postos_dir, orient="index")
        postos_df = postos_df.append(posto_dic, ignore_index = True)

        postos_df.to_json(Postos.postos_dir, orient="index")

        self.postos.append(posto)


    def list_postos(self, details = False):
        if details:
            for i in range(len(self.postos)):
                print(i, " ", self.postos[i].get_name_details())
        else:
            for i in range(len(self.postos)):
                print(i, " ", self.postos[i].get_name())

    def delete(self, index):
        postos_df = pd.read_json(Postos.postos_dir, orient="index")

        postos_df = postos_df.drop(index)
        self.postos.remove(self.postos[index])

        postos_df = postos_df.reset_index(drop=True)

        postos_df.to_json(Postos.postos_dir, orient="index")


    class Posto:

        types = {0:"Permanencia", 1:"Sentinela", 2:"Plantao", 3:"Cb de dia", 4:"Sgt de dia"}
        genders = {0:"masc", 1:"fem"}
        
        def __init__(self, type, where, people, gender, year):
            self.type = type
            self.where = where
            self.people = people
            self.gender = gender
            self.year = year


        def return_dict(self):
            dic = {
                "type": self.type,
                "where": self.where,
                "people": self.people,
                "gender": self.gender,
                "year": self.year,
            }
            return dic
        
        
        def get_info(self):
            print("type = ", self.type)
            print("where = ", self.where)
            print("people = ", self.people)
            print("gender = ", self.gender)
            print("year = ", self.year)
            pass

        def get_name(self):
            name = self.types[self.type] + " " + self.where
            return name
        
        def get_name_details(self):
            name = self.types[self.type] + " " + self.where
            others = f"|people: {self.people} |gender: {self.genders[self.gender]} |year: {self.year} |"

            info = name.ljust(25, " ") + others

            return info
        

if __name__ == "__main__":

    pass






