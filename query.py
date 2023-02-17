from tabulate import tabulate
import sqlite3

def crear():
    # conectando con la bd y creando el cursor
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    
    # datos a rellenar
    name = input('Nombre: ')
    enterprise = input('Empresa: ')
    adress = input('Dirección: ')
    phone = input('Número de celular: ')
    email = input('Correo electronico: ')
    
    # creación y ejecución del query
    q2 = f"INSERT INTO contacts (name, enterprise, adress, phone, email) VALUES ('{name}', '{enterprise}', '{adress}', '{phone}', '{email}');"
    cursor.execute(q2)
    
    # commit y cierre de la conexión
    print(' Se ingresaron correctamente los datos '.center(50,"*"))
    con.commit()
    con.close()


def mostrar():
    # conectando con la bd y creando el cursor
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    df = []

    # creación y ejecución del query
    q3 = f'''SELECT * FROM contacts;'''
    cursor.execute(q3)
    df = cursor.fetchall()
    
    # commit y cierre de la conexión
    con.commit()
    con.close()
    return df


def buscar():
    # conectando con la bd y creando el cursor
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    df = []

    # datos a rellenar
    name = input('Ingrese el nombre del contacto: ')

    # creación y ejecución del query
    q4 = f'''SELECT * FROM contacts WHERE name = "{name}";'''
    cursor.execute(q4)
    df = cursor.fetchall()
    
    # commit y cierre de la conexión
    print(' Busqueda finalizada '.center(50, "#"))
    con.commit()
    con.close()
    return df


def modificar():
    # conectando con la bd y creando el cursor
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()

    # datos a rellenar
    mostrar()

    id = int(input('Ingrese el id del contacto que desea modificar: '))
    print('''
        1. Modificar el nombre
        2. Modificar la empresa
        3. Modificar la dirección
        4. Modificar el numero telefonico
        5. Modicifar el correo electronico
        6. Modificar todo
    ''')

    election = input('Ingrese opcion: ')
    if election == '1':
        name = input('Ingrese el nuevo nombre: ')
        q5 = f'UPDATE contacts SET name = "{name}" WHERE id = {id}'
        cursor.execute(q5)
    
    elif election == '2':
        enterprise = input('Ingrese la nueva empres: ')
        q5 = f'UPDATE contacts SET enterprise = "{enterprise}" WHERE id = {id}'
        cursor.execute(q5)
    
    elif election == '3':
        adress = input('Ingrese la nueva dirección: ')
        q5 = f'UPDATE contacts SET adress = "{adress}" WHERE id = {id}'
        cursor.execute(q5)
    
    elif election == '4':
        phone = input('Ingrese el nuevo nuevo celular: ')
        q5 = f'UPDATE contacts SET phone = "{phone}" WHERE id = {id}'
        cursor.execute(q5)
    
    elif election == '5':
        email = input('Ingrese el nuevo correo: ')
        q5 = f'UPDATE contacts SET email = "{email}" WHERE id = {id}'
        cursor.execute(q5)

    
    elif election == '6':
        name = input('Ingrese el nuevo nombre: ')
        q5 = f'UPDATE contacts SET name = "{name}" WHERE id = {id}'
        cursor.execute(q5)
        
        enterprise = input('Ingrese la nueva empresa: ')
        q5 = f'UPDATE contacts SET enterprise = "{enterprise}" WHERE id = {id}'
        cursor.execute(q5)
        
        adress = input('Ingrese la nueva dirección: ')
        q5 = f'UPDATE contacts SET adress = "{adress}" WHERE id = {id}'
        cursor.execute(q5)

        phone = input('Ingrese el nuevo nuevo celular: ')
        q5 = f'UPDATE contacts SET phone = "{phone}" WHERE id = {id}'
        cursor.execute(q5)

        email = input('Ingrese el nuevo correo:')
        q5 = f'UPDATE contacts SET email = "{email}" WHERE id = {id}'
        cursor.execute(q5)
    
    # creación y ejecución del query
    mostrar()

    # commit y cierre de la conexión
    print(' Actualizado correctamente '.center(50, "/"))
    con.commit()
    con.close()

def eliminar():
    # conectando con la bd y creando el cursor
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    
    # datos a rellenar
    id = int(input('Ingrese el id del contacto que desea eliminar: '))
    
    # creación y ejecución del query
    q6 = f"DELETE FROM contacts WHERE id = {id};"
    cursor.execute(q6)
    
    # commit y cierre de la conexión
    print(' Eliminado correctamente '.center(50,"*"))
    con.commit()
    con.close()

def show_table(m):

    datos = m()
    HEADER = ('ID', 'NAME', 'ENTERPRISE', 'ADRESS', 'PHONE', 'EMAIL')
    table = tabulate(datos, HEADER)
    print(table)