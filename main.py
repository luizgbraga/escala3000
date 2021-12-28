from os import system
import scripts.prints as prints
from back import Section


class Shell:

    def __init__(self):
        self.section = Section()
        pass


    def run_shell(self):
        OK = True
        while OK:
            self.main_head()
            OK = self.get_comand()
        pass


    def get_comand(self):
        prints.print_options()

        opt = input(">>>").split("-")
        option = opt.pop(0).split()[0]
        opts = {}

        for i in opt:
            lista = i.split()
            if len(lista) > 1:
                opts[lista[0]] = lista[1:]
            else:
                opts[lista[0]] = "_"

        self.main_head()

        match option:
            case "preview":
                for flag in opts:
                    match flag:
                        case "d":
                            date = opts[flag][0]
                            self.section.update_preview(date)
                        case "s":
                            self.show_preview()
                        case "h":
                            prints.print_help(option)

            case "show":
                for flag in opts:
                    match flag:
                        case "w":
                            what = opts[flag][0]
                            match what:
                                case "alunos_list": 
                                    self.show_alunos_list()
                                case "all_postos":
                                    self.show_all_postos()
                                case "using_postos":
                                    self.show_using_postos()
                                case _:
                                    prints.print_non_existing()
                        case "h":
                            prints.print_help(option)

            case "change":
                for flag in opts:
                    match flag:
                        case "a":
                            alunos = (opts[flag][0], opts[flag][1])
                            posto_code = opts[flag][2]
                            red = True if opts[flag][3] == "red" else False
                            self.section.change(alunos, posto_code, red)
                        case "h":
                            prints.print_help(option)

            case "about":
                self.about_mensage()

            case "quit":
                self.exit_mensage()
                return False

            case _:
                self.non_existing_option()
        
        return True


    def show_preview(self):
        preview = self.section.return_preview_text()
        prints.print_preview(preview)


    def show_alunos_list(self):
        num_names = self.section.alunos.get_list_alunos()
        prints.print_alunos_list(num_names)


    def show_all_postos(self):
        postos = self.section.postos.list_postos(details = True)
        prints.print_postos(postos)


    def show_using_postos(self):
        postos = self.section.postos.list_postos(details = True, using = True)
        prints.print_postos(postos)
        pass


    def exit_mensage(self):
        prints.print_quit()


    def about_mensage(self):
        prints.print_about()


    def non_existing_option(self):
        prints.print_non_existing()


    def main_head(self):
        prints.print_head()


if __name__ == "__main__":
    s = Shell()
    s.run_shell()
    pass

