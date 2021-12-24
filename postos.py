import pandas as pd
import hashes

class Postos:

    postos_dir = "./Data/postos/postos.json"
    local_code = {}

    def __init__(self):
        postos_df = pd.read_json(Postos.postos_dir, orient="index")
        self.postos = {}
        
        for index, key in postos_df.iterrows():
            posto = Postos.Posto(key["type"], key["where"], key["people"], key["gender"], key["year"], key["code"], key["black"], key["red"])
            self.postos[posto.code] = posto


    def new_posto(self, type, where, people, gender, year, code):
        posto = Postos.Posto(type, where, people, gender, year, code, [], [])
        posto.new_escale()
        posto_dic = posto.return_dict()

        postos_df = pd.read_json(Postos.postos_dir, orient="index")
        postos_df = postos_df.append(posto_dic, ignore_index = True)
        self.postos[posto.code] = posto

        postos_df.to_json(Postos.postos_dir, orient="index")


    def delete(self, code):
        postos_df = pd.read_json(Postos.postos_dir, orient="index")

        postos_df = postos_df.drop(postos_df.index[postos_df["code"] == code])
        temp = self.postos.pop(code)

        #postos_df = postos_df.reset_index(drop=True)

        postos_df.to_json(Postos.postos_dir, orient="index")


    def list_postos(self, details = False):
        if details:
            for key in self.postos:
                print(self.postos[key].code, " ", self.postos[key].get_name_details())
        else:
            for key in self.postos:
                print(self.postos[key].code, " ", self.postos[key].get_name())


    def get_using(self):
        using_dir = "./Data/postos/using.txt"
        using = []
        with open(using_dir) as f:
            for line in f.readlines():
                using.append(int(line))
        return using

    def save(self):
        
        pass

    def close(self):
        pass


    class Posto:

        types = {0:"Permanencia", 1:"Sentinela", 2:"Plantao", 3:"Cb de dia", 4:"Sgt de dia"}
        genders = {0:"masc", 1:"fem"}

        """
        Code: 1_a_b
        a = type
        b = local
            0-específico
            1-Ala N
            2-Ala S
            3-3o piso
            4-4o piso
        """

        def __init__(self, type, where, people, gender, year, code, black, red):
            self.type = type
            self.where = where
            self.people = people
            self.gender = gender
            self.year = year
            self.code = code
            self.black = black
            self.red = red


        def return_dict(self):
            dic = {
                "type": self.type,
                "where": self.where,
                "people": self.people,
                "gender": self.gender,
                "year": self.year,
                "code": self.code,
                "black": self.black,
                "black": self.red
            }
            return dic


        def get_name(self):
            name = self.types[self.type] + " " + self.where
            return name


        def get_name_details(self):
            name = self.get_name()
            others = f"|people: {self.people} |gender: {self.genders[self.gender]} |year: {self.year} |"

            info = name.ljust(25, " ") + others

            return info


        def new_escale(self):
            seg_fem = [21005, 21011, 21013, 21021, 21030, 21031, 21042, 21048, 21068, 21401, 21405]

            seg_masc = [20070, 20418, 21001, 21002, 21004, 21006, 21007, 21008, 21009, 21010, 21012, 21014, 21015, 21016, 21017, 21018, 21019, 21022, 21023, 21024, 21026, 21027, 21028, 21029, 21032, 21034, 21035, 21036, 21037, 21038, 21039, 21040, 21041, 21043, 21044, 21045, 21046, 21047, 21049, 21050, 21051, 21052, 21053, 21054, 21055, 21056, 21057, 21058, 21060, 21061, 21062, 21063, 21064, 21065, 21066, 21069, 21070, 21402, 21403, 21404, 21406, 21408, 21409, 21410, 21411, 21413, 21414, 21415, 21416, 21417, 21418, 21419, 21420, 21421, 21422, 21423, 21424, 21425, 21426, 21427, 21428]

            if self.gender:
                self.black = seg_fem.copy()
                self.red = seg_fem[::-1]
            else:
                self.black = seg_masc.copy()
                self.red = seg_masc[::-1]


if __name__ == "__main__":
    postos = Postos()
    print(postos.get_usings())
    pass