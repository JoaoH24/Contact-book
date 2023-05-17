from tkinter import *
from query_inter import *

# StringVars
# name_entry = StringVar()
# enterprise_entry = StringVar()
# adress_entry = StringVar()
# phone_entry = StringVar()
# email_entry = StringVar()


def mainWindow():
    # Creación de la ventana principal
    root = Tk()
    root.geometry("800x400")
    root.title("Agenda de contactos")
    root.config(bg="gray")
    root.resizable(0, 0)

    create = Button(root, text="Crear contacto", command=addContact).place(x=20, y=300)
    show = Button(root, text="Mostrar contacto", command=showContact).place(
        x=180, y=300
    )
    search = Button(root, text="Buscar contacto", command=searchContact).place(
        x=340, y=300
    )
    modify = Button(root, text="Modificar contacto", command=modifyContact).place(
        x=500, y=300
    )
    delete = Button(root, text="Eliminar contacto", command=deleteContact).place(
        x=660, y=300
    )

    root.mainloop()


def addContact():
    # Ventana para agrgar nuevo contacto
    create = Tk()
    create.geometry("400x250")
    create.title("Agregar contacto")
    create.config(bg="gray")
    create.resizable(0, 0)

    # Creacion de las etiquetas de texto con los datos esenciales de contacto
    label_name = Label(
        create, text="Nombre", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=40)
    label_enterprise = Label(
        create, text="Empresa", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=80)
    label_adress = Label(
        create, text="Dirección", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=120)
    label_phone = Label(
        create, text="Teléfono", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=160)
    label_email = Label(
        create, text="E-mail", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=200)

    name = Entry(create).place(x=100, y=40)
    enterprise = Entry(create).place(x=100, y=80)
    adress = Entry(create).place(x=100, y=120)
    phone = Entry(create).place(x=100, y=160)
    email = Entry(create).place(x=100, y=200)

    create.mainloop()


def showContact():
    # Vemtama para mostrar contacto
    show = Tk()
    show.geometry("400x250")
    show.title("Mostrar contacto")
    show.config(bg="gray")
    show.resizable(0, 0)

    show.mainloop()


def searchContact():
    # Ventana para buscar contacto
    search = Tk()
    search.geometry("400x250")
    search.title("Buscar Contacto")
    search.config(bg="gray")
    search.resizable(0, 0)

    label_name = Label(
        search, text="Nombre: ", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=150)

    name = Entry(search).place(x=100, y=150)

    search.mainloop()


def modifyContact():
    # Ventana para modificar contacto
    modify = Tk()
    modify.geometry("400x250")
    modify.title("Modificar contacto")
    modify.config(bg="gray")
    modify.resizable(0, 0)

    label_id = Label(
        modify, text="Id: ", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=150)

    id = Entry(modify).place(x=100, y=150)

    modify.mainloop()


def deleteContact():
    # Ventana para eliminar contacto
    delete = Tk()
    delete.geometry("400x250")
    delete.title("Eliminar contacto")
    delete.config(bg="gray")
    delete.resizable(0, 0)

    label_id = Label(
        delete, text="Id: ", font="montserrat 10", bg="gray", fg="white"
    ).place(x=20, y=150)

    id = Entry(delete).place(x=100, y=150)

    delete.mainloop()
