import prints
from back import Section
from os import system
from time import sleep

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
        print("""Available options(use -h to a brief help):
preview [-d --date] [-s --show] | show [-w --what]
change [-a --alunos] [--posto-code] [--scale] | 
quit | about 
Enter the comand:""")

        opts = input(">>>").split("-")
        option = opts.pop(0).split()[0]

        self.main_head()

        if option == "preview":
            for i in range(len(opts)):
                if opts[i][0] == "d":
                    date = opts[i].split()[1]
                    self.section.update_preview(date)
                if opts[i][0] == "s":
                    self.show_preview()
                if opts[i][0] == "h":
                    print("""HELP: preview [-d --date] [-s --show]
- date format: dd/mm/yyyy
""")
                    system("pause")

        elif option == "show":
            for i in range(len(opts)):
                if opts[i][0] == "w":
                    what = opts[i].split()[1]
                    if what == "alunos_list":
                        self.show_alunos_list()
                if opts[i][0] == "h":
                    print("""HELP: show [-w --what]
Options:
- alunos_list: return number and name of all students in section
""")
                    system("pause")

        elif option == "change":
            for i in range(len(opts)):
                if opts[i][0] == "a":
                    lista = opts.split(" ")
                    alunos = (lista[1], lista[2])
                    posto_code = lista[3]
                    red = True if lista[4] == "red" else False

                    pass
                if opts[i][0] == "h":
                    print("""HELP: change [-a --alunos]
- example: >>>change -a 21063 21424 120 red
""")
                    system("pause")

        elif option == "about":
            self.about_mensage()
        elif option == "quit" or option == "q":
            self.exit_mensage()
            return False
        else:
            self.non_existing_option()
        
        return True


    def show_preview(self):
        preview = self.section.return_preview_text()
        prints.print_preview(preview)


    def show_alunos_list(self):
        num_names = self.section.alunos.get_list_alunos()
        prints.print_alunos_list(num_names)


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

