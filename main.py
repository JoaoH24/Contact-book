import os
from conection import *
from query import *
from tabulate import tabulate

pet = conectar()
create_table(pet)

def main():
    os.system('cls')
    def menu():
        print(' BIENVENIDO A SU AGENDA DE CONTACTOS '.center(50, '='))
        print('''
          \t 1. Crear contacto
          \t 2. Mostrar contactos
          \t 3. Buscar constacto
          \t 4. Modificar contacto
          \t 5. Eliminar contacto
          \t 6. Salir
          ''')
    menu()
    user = input('> ')
    flag = True
    while flag:

        if user == '1':
            crear()
            menu()
            user = input('> ')

        elif user == '2':
            mostrar()

            datos = mostrar()
            HEADER = ('ID', 'NAME', 'ENTERPRISE', 'ADRESS', 'PHONE', 'EMAIL')
            table = tabulate(datos, HEADER, tablefmt='fancy_grid')
            print(table)
            menu()
            user = input('> ')

        elif user == '3':
            #buscar()

            datos = buscar()
            HEADER = ('ID', 'NAME', 'ENTERPRISE', 'ADRESS', 'PHONE', 'EMAIL')
            table = tabulate(datos, HEADER, tablefmt='fancy_grid')
            print(table)
            menu()
            user = input('> ')

        elif user == '4':
            modificar()
            menu()
            user = input('> ')
        
        elif user == '5':
            eliminar()
            menu()
            user = input('> ')
        
        else:
            flag = False
    
main()