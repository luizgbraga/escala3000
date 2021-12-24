from alunos import Alunos
from postos import Postos
from tools import Date


class Section:

    def __init__(self):
        self.alunos = Alunos(1)
        self.postos = Postos()
        self.preview = {}

    
    def get_preview(self, date_range):
        p = self.postos.get_using()
        for date in date_range:
            self.preview[date] = Section.Preview(date, p)


    class Preview:
        
        def __init__(self, date1, posto_codes, forced_red=False):
            self.title = Date.generate_title(date1)

            if Date.get_weekday(date1)>4 or forced_red:
                self.red = True
            else:
                self.red = False

            self.postos = {}
            for code in posto_codes:
                pass


        def alunos_request(self):
            pass





if __name__ == "__main__":

    pass
