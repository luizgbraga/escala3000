from os import system
from time import sleep

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
        print(num_names[i].ljust(29), end = "")
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

