import pandas as pd

class Alunos:

    alunos_dir = "./Data/alunos/"

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

    def list_alunos(self):
        for aluno in self.alunos:
            print(self.alunos[aluno].get_name())

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

            self.name = args["Name"]
            self.number = args["Number"]
            self.gender = args["Gender"]
            self.dispensa = args["Disp_lim"]
            self.tur_cmd = args["Tur_cmd"]
            self.last_work = args["Last_work"]
            self.scale_work_number = args["Works_number"]
            self.changes_number = args["Changes_number"]

        def get_name(self):
            name = str(int(self.number)) + " " + self.name 
            return name


if __name__ == "__main__":

    pass
