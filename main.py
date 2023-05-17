import os
from conection import *
from query_inter import *
from tabulate import tabulate
from interface import *

peticion = conectar()
create_table(peticion)


def main():
    os.system("cls")

    mainWindow()


main()
