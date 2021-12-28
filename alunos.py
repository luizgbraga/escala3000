import json
from scripts.tools import Date

class Alunos:

    dir_alunos = "./data/alunos/"
    dir_alunos_tmp = "./tmp/alunos/"

    def __init__(self, year):
        self.year = year
        direc = Alunos.dir_alunos + str(year) + "_ano/all.json"

        with open(direc, "r") as f:
            alunos_dic = json.loads(f.read())

        self.alunos = {}

        for number in alunos_dic:
            aluno = Alunos.Aluno(alunos_dic[str(number)])
            self.alunos[number] = aluno


    def save(self):
        dic_alunos = {}
        for number in self.postos:
            dic_alunos[number] = self.postos[number].return_dict()

        direc = Alunos.dir_alunos + str(self.year) + "_ano/all.json"

        with open(direc, "w") as f:
            json.dump(dic_alunos, f)


    def save_preview(self):
        dic_alunos = {}
        for number in self.postos:
            dic_alunos[number] = self.postos[number].return_dict()

        direc = Alunos.dir_alunos_tmp + str(self.year) + "_ano/all.json"

        with open(direc, "w") as f:
            json.dump(dic_alunos, f)


    def save_tmp(self):
        pass


    def get_list_alunos(self):
        lista = []
        for key in self.alunos:
            lista.append((str(key), str(self.alunos[key].get_name())))
        return lista


    class Aluno:

        def __init__(self, args):
            self.name = args["name"]
            self.gender = args["gender"]
            self.dispensa = Date.get_date(args["disp_lim"])
            self.tur_cmd = args["tur_cmd"]
            self.last_work = Date.get_date(args["last_work"])
            self.works_number = args["works_number"]
            self.changes_number = args["changes_number"]


        def get_name(self):
            name = self.name 
            return name


        def return_dict(self):
            dic = {
                "name": self.name,
                "gender": self.gender,
                "disp_lim": Date.get_string(self.disp_lim),
                "tur_cmd": self.tur_cmd,
                "last_work": Date.get_string(self.last_work),
                "works_number": self.works_number,
                "changes_number": self.changes_number
            }


        def request_preview(self, date):
            """
            Conditions:
                - disp_limp
                - tur_cmd
                - last_work
            """
            #disp lim
            dif = Date.check_dif(date, self.dispensa)
            bool_disp_lim = dif < 0 
            bool_tur_cmd = int(self.tur_cmd) == 0
            bool_last_work = Date.check_dif(self.last_work, date) > 2

            if bool_disp_lim and bool_tur_cmd and bool_last_work:
                self.last_work = date
                self.works_number += 1
                return True, self.name
            else:
                return False, None


if __name__ == "__main__":
    alunos = Alunos(1)
    alunos.list_alunos()
    pass
