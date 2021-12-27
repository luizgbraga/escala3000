from alunos import Alunos
from postos import Postos
from tools import Date
from copy import deepcopy

class Section:

    def __init__(self):
        self.alunos = Alunos(1)
        self.postos = Postos()
        self.preview_generator = None
        self.set_preview_generator()
        self.preview = {}
        self.var = {}
    
    
    def set_preview_generator(self):
        self.preview_generator = (deepcopy(self.alunos), deepcopy(self.postos))


    def undo_all(self):
        self.set_preview_generator()


    def update_preview(self, until):
        self.preview = {}
        end = Date.get_date(until)
        p = self.postos.get_using()
        last = Date.get_last_day()

        while Date.check_dif(last, end) >= 0:
            self.preview[Date.get_string(last)] = Section.Preview(last, p, self.preview_generator)

            last = Date.get_next_day(last)


    def return_preview_text(self):
        preview_text = {}
        for key in self.preview:
            preview_text[key] = self.preview[key].get_text()
        return preview_text


    def change(self, alunos, code, red):
        #implementar bool para ver se eles realmente estão nesses dias
        #implementar bool para ver se cada um pode tirar no outro dia
        if red:
            lista = self.preview_generator[1].postos[str(code)].red
            aluno1 = lista.index(int(alunos[0]))
            aluno2 = lista.index(int(alunos[1]))
            self.preview_generator[1].postos[str(code)].red[aluno1], self.preview_generator[1].postos[str(code)].red[aluno2] = lista[aluno2], lista[aluno1]
        else:
            lista = self.preview_generator[1].postos[str(code)].black
            aluno1 = lista.index(int(alunos[0]))
            aluno2 = lista.index(int(alunos[1]))
            self.preview_generator[1].postos[str(code)].black[aluno1], self.preview_generator[1].postos[str(code)].black[aluno2] = lista[aluno2], lista[aluno1]

        self.preview_generator[0].alunos[alunos[0]].changes_number += 1
        self.preview_generator[0].alunos[alunos[1]].changes_number += 1




    class Preview:
        """
        - title
        - red
        - postos_title = {code:title}
        - postos = {code:{number:name}}
        """
        
        def __init__(self, date1, posto_codes, generator, forced_red=False):
            self.title = Date.generate_title(date1)
            self.postos_title = {}
            self.postos = {}

            if Date.get_weekday(date1)>4 or forced_red:
                self.red = True
            else:
                self.red = False

            temp_postos = {}
            for code in posto_codes:
                pack = generator[1].postos[str(code)].request_preview(self.red)
                temp_postos[str(code)] = pack
                self.postos_title[str(code)] = pack["title"]
            
            for code in posto_codes:
                n = 0
                last  = 0
                pack = temp_postos[str(code)]
                dic = {}
                while n < pack["people"]:
                    if pack["scale"]:
                        number = str(generator[1].postos[str(code)].red[last])
                        available = generator[0].alunos[number].request_preview(date1)
                        if available[0]:
                            number = generator[1].postos[str(code)].red.pop(last)
                            generator[1].postos[str(code)].red.append(number)
                            n += 1
                            dic[number] = available[1]
                        else:
                            last += 1
                    else:
                        number = str(generator[1].postos[str(code)].black[last])
                        available = generator[0].alunos[number].request_preview(date1)
                        if available[0]:
                            number = generator[1].postos[str(code)].black.pop(last)
                            generator[1].postos[str(code)].black.append(number)
                            n += 1
                            dic[number] = available[1]
                        else:
                            last += 1

                self.postos[str(code)] = dic


        def get_text(self):
            dic = {}
            dic["title"] = self.title
            dic["postos"] = {}
            for key in self.postos_title:
                lista = [str(x) + " ==> " + str(y) for x, y in list(self.postos[key].items())]
                dic["postos"][self.postos_title[key]] = lista
            return dic


if __name__ == "__main__":
    pass
