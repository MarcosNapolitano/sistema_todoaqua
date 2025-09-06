from BBDD.connect import get_all
import customtkinter as ct
from tkinter import messagebox


def search_client(name):

    query = "SELECT ID_CLIENTE, NOMBRE, LOCALIDAD, PROVINCIA FROM CLIENTES WHERE NOMBRE ILIKE %s LIMIT 5"

    param = (f"%{name}%",)

    clientes = get_all(query, param)

    if not clientes:
        messagebox.showerror(
            title="Sistema de Gestión Todo Aqua", message="Cliente inexistente."
        )
        return False

    count = 1

    if len(clientes) > 1:

        text = "Varios clientes coinciden en nombre:\n"

        for cliente in clientes:
            text += f"{count} | {cliente[1]} - {cliente[2]} - {cliente[3]}\n"
            count += 1

        text += "Por favor elija el número del usuario."

        id_cliente = 0

        while not id_cliente:
            try:
                dialog = ct.CTkInputDialog(text=text, title="Elija usuario")
                id = int(dialog.get_input() or 0)  # waits for input

                if id:
                    id_cliente = id
            except:
                messagebox.showerror(
                    title="Sistema de Gestión Todo Aqua",
                    message="Por favor ingrese un número",
                )

        id_cliente = clientes[id_cliente - 1][0]
    else:

        id_cliente = clientes[0][0]

    return id_cliente
