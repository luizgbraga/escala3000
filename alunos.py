import json


class Alunos:

    alunos_dir = "./Data/alunos/"

    def __init__(self, year):
        self.year = year
        direc = Alunos.alunos_dir + str(year) + "_ano/all.json"

        with open(direc, "r") as f:
            alunos_dic = json.loads(f.read())

        self.alunos = {}

        for number in alunos_dic:
            aluno = Alunos.Aluno(alunos_dic[str(number)])
            self.alunos[number] = aluno


    def list_alunos(self):
        for aluno in self.alunos:
            print(aluno + " --> " + self.alunos[aluno].get_name())


    def save(self):
        dic_alunos = {}
        for number in self.postos:
            dic_alunos[number] = self.postos[number].return_dict()
        
        direc = Alunos.alunos_dir + str(self.year) + "_ano/all.json"

        with open(direc, "w") as f:
            json.dump(dic_alunos, f)


    class Aluno:

        def __init__(self, args):
            self.name = args["name"]
            self.gender = args["gender"]
            self.dispensa = args["disp_lim"]
            self.tur_cmd = args["tur_cmd"]
            self.last_work = args["last_work"]
            self.scale_work_number = args["works_number"]
            self.changes_number = args["changes_number"]


        def get_name(self):
            name = self.name 
            return name


        def return_dict(self):
            dic = {
                "name": self.name,
                "gender": self.gender,
                "disp_lim": self.disp_lim,
                "tur_cmd": self.tur_cmd,
                "last_work": self.last_work,
                "works_number": self.works_number,
                "changes_number": self.changes_number
            }


if __name__ == "__main__":
    alunos = Alunos(1)
    alunos.list_alunos()
    pass
