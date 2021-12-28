from os import system
from time import sleep

def print_options():
    print("""Available options(use -h to a brief help):
preview [-d --date] [-s --show] | show [-w --what] 
change [-a --alunos] [--posto-code] [--scale]
quit | about 
Enter the comand:""")


def print_help(option):
    match option:
        case "preview":
            print("""HELP: preview [-d --date] [-s --show]
- date format: dd/mm/yyyy""")
            system("pause")

        case "show":
            print("""HELP: show [-w --what]
Options:
- alunos_list: return number and name of all students in section
- all_postos: return all postos(archived or not)
- using_postos: return only current postos""")
            system("pause")

        case "change":
            print("""HELP: change [-a --alunos]
- example: >>>change -a 21063 21424 120 red
""")
            system("pause")

        case _:
            print("There's no help file for this comand")
            system("pause")


def print_preview(preview):
    print("Preview:")
    for date in preview:
        print("#######################################################################################")
        print(preview[date]["title"])
        for posto_title in preview[date]["postos"]:
            print("--> ", posto_title)
            for name in preview[date]["postos"][posto_title]:
                print("\t", name)
    system("pause")


def print_alunos_list(num_names):
    for i in range(len(num_names)):
        if i % 3 == 0:
            print("")
        string = num_names[i][0]  + " ==> " + num_names[i][1]
        print(string.ljust(29), end = "")
    system("pause")


def print_postos(lista):
    for i in lista:
        print(i)
    system("pause")


def print_quit():
    print("Thanks for trusting us, we will be waiting for you.")
    sleep(1)
    system("cls")


def print_about():
    print("""An initiative of the vibrant XXV students:
-ALXPV --> ALEXANDRE PAIVA
-BRAGA --> BRAGA
-WOBETEC --> ESDRAS

Take a look at our repository:
https://github.com/wobetec/escala""")
    print("")
    system("pause")


def print_non_existing():
    print("Sorry this function is not defined.")
    system("pause")


def print_head():
    system("cls")
    print("""███████╗███████╗ ██████╗ █████╗ ██╗      █████╗     ██████╗  ██████╗  ██████╗  ██████╗ 
██╔════╝██╔════╝██╔════╝██╔══██╗██║     ██╔══██╗    ╚════██╗██╔═████╗██╔═████╗██╔═████╗
█████╗  ███████╗██║     ███████║██║     ███████║     █████╔╝██║██╔██║██║██╔██║██║██╔██║
██╔══╝  ╚════██║██║     ██╔══██║██║     ██╔══██║     ╚═══██╗████╔╝██║████╔╝██║████╔╝██║
███████╗███████║╚██████╗██║  ██║███████╗██║  ██║    ██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ 
                                                    Powered by: ALXPV, BRAGA and WOBETEC""")


if __name__ == "__main__":
    pass

