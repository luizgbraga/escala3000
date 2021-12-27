from datetime import date, datetime, timedelta
import json

class Date:
    
    """
    ddmmyyyy
    """

    def get_date(d1):
        date1 = datetime.strptime(d1, "%d/%m/%Y")
        return date1
    
    def get_string(d1):
        date1 = datetime.strftime(d1, "%d/%m/%Y")
        return date1

    def check_dif(d1, d2):
        """d2 - d1"""
        delta = d2 - d1
        return delta.days
    
    def get_next_day(d1):
        return d1 + timedelta(days=1)
    
    def generate_title(d1):
        week_days=["SEGUNDA-FEIRA","TERÇA-FEIRA","QUARTA-FEIRA","QUINTA-FEIRA","SEXTA-FEIRA","SÁBADO","DOMINGO"]
        months = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]

        d = str(d1.day).rjust(2, "0")
        m = months[d1.month-1]
        y = d1.year
        week = week_days[d1.weekday()]
        title = f"ESCALA DE SERVIÇO PARA O DIA {d} DE {m} {y} - {week}"

        return title
    
    def get_last_day():
        options_dir = "./Data/options.json"
        with open(options_dir, "r") as f:
            options_dic = json.loads(f.read())
            last = options_dic["last_scale"]
        return Date.get_date(last)

    def get_weekday(d1):
        return d1.weekday()


if __name__ == "__main__":
    pass