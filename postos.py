import json


class Postos:

    dir_postos = "./data/postos/postos.json"
    dir_postos_tmp = "./tmp/postos/postos.json"


    def __init__(self):
        with open(Postos.dir_postos, "r") as f:
            postos_dic = json.loads(f.read())

        self.postos = {}
        
        for key in postos_dic:
            posto = Postos.Posto(postos_dic[key])
            self.postos[key] = posto


    def new_posto(self, type, where, people, gender, year, code):
        dic = {
            "type": type,
            "where": where,
            "people": people,
            "gender": gender,
            "year": year,
            "black": [],
            "red": []
        }
        posto = Postos.Posto(dic)
        posto.new_escale()
        self.postos[str(code)] = posto


    def delete(self, code):
        removed = self.postos.pop(str(code))


    def list_postos(self, details = False, using = False):
        if using:
            codes = [str(x) for x in self.get_using()]
        else:
            codes = list(self.postos.keys())

        lista = []
        if details:
            for key in codes:
                lista.append(key + " " + self.postos[key].get_name_details())
        else:
            for key in codes:
                lista.append(key + " " + self.postos[key].get_name())

        return lista


    def get_using(self):
        options_dir = "./var/system_variables.json"
        with open(options_dir, "r") as f:
            options_dic = json.loads(f.read())
            using = options_dic["using_postos"]
        return using


    def save(self):
        dic_postos = {}
        for key in self.postos:
            dic_postos[key] = self.postos[key].return_dict()

        with open(Postos.dir_postos, "w") as f:
            json.dump(dic_postos, f)


    def save(self):
        dic_postos = {}
        for key in self.postos:
            dic_postos[key] = self.postos[key].return_dict()

        with open(Postos.dir_postos_tmp, "w") as f:
            json.dump(dic_postos, f)


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

        def __init__(self, dic):
            self.type = dic["type"]
            self.where = dic["where"]
            self.people = dic["people"]
            self.gender = dic["gender"]
            self.year = dic["year"]
            self.black = dic["black"]
            self.red = dic["red"]


        def return_dict(self):
            dic = {
                "type": self.type,
                "where": self.where,
                "people": self.people,
                "gender": self.gender,
                "year": self.year,
                "black": self.black,
                "red": self.red
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
        

        def request_preview(self, red):
            """
            scale - numbers sequence
            people - how many people are selected
            title
            """

            pack = {}
            pack["scale"] = red
            pack["people"] = self.people
            pack["title"] = Postos.Posto.types[self.type] + " " + self.where
            return pack


if __name__ == "__main__":
    pass