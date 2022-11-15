import sqlite3

def conectar():
    try: 
        conexion = sqlite3.connect('contacts.db')
        print('Se ha logrado conectar correctamente con SQLite3')
        return conexion
    except sqlite3.Error as err:
        print('Ocurrio un problema al momento de conectar con la base de datos ', err)
        
def create_table(conexion):
    cursor = conexion.cursor()
    query = ''' CREATE TABLE IF NOT EXIST contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        enterprise TEXT NOT NULL,
        adress TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL
        ) '''
        
    cursor.execute(query)
    conexion.commit()