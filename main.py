import os
from conection import *

pet = conectar()
create_table(pet)

def main():
    os.system('cls')
    print('BIENVENIDO A SU AGENDA DE CONTACTOS'.center(50, '='))
    print('''
          \t 1. Crear contacto
          \t 2. Mostrar contactos
          \t 3. Buscar constacto
          \t 4. Modificar contacto
          \t 5. Eliminar contacto
          \t 6. Salir
          ''')
    
    input('> ')
    
main()