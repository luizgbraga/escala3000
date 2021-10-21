import pandas as pd

class DataBase:
    def __init__(self):
        pass

    def get_data(self):
        f = pd.read_excel("./escala.xlsx")
        f.fillna(0, inplace=True)
        return f.copy()
    
    def save_data(self, df):
        writer = pd.ExcelWriter("./escala.xlsx", engine="openpyxl")
        df.to_excel(writer, index=False)
        writer.save()

if __name__ == "__main__":
    pass