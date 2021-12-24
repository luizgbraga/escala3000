from datetime import date

class Date:
    
    """
    ddmmyyyy
    """

    def split_date(d1):
        d = int(d1[0:2])
        m = int(d1[2:4])
        y = int(d1[4:])
        da = date(y, m, d)
        return da

    def check_dif(date1, date2):
        d1 = Date.split_date(date1)
        d2 = Date.split_date(date2)
        delta = d2 - d1
        return delta.days
    
    def get_weekday(date1):

        d1 = Date.split_date(date1)
        week = d1.weekday()

        return week
    
    def generate_title(date1):
        d1 = Date.split_date(date1)
        week_days=["SEGUNDA-FEIRA","TERÇA-FEIRA","QUARTA-FEIRA","QUINTA-FEIRA","SEXTA-FEIRA","SÁBADO","DOMINGO"]
        months = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
        d = str(d1.day).rjust(2, "0")
        m = months[d1.month-1]
        y = d1.year
        week = week_days[d1.weekday()]
        title = f"ESCALA DE SERVIÇO PARA O DIA {d} DE {m} {y} - {week}"

        return title


if __name__ == "__main__":
    print(Date.generate_title("01012021"))
    pass