from BBDD.connect import get_all
import customtkinter as ct
from tkinter import messagebox


def search_client(name):

	query = "SELECT ID_CLIENTE, NOMBRE, LOCALIDAD, PROVINCIA FROM CLIENTES WHERE NOMBRE ILIKE %s LIMIT 5";

	data = (f"%{name}%", )

	res = get_all(query, data)

	if not res:
		messagebox.showerror(title="Sistema de Gestión Todo Aqua", message="Cliente inexistente.")
		return False

	count = 1

	if len(res) > 1:

		text = "Varios clientes coinciden en nombre:\n"

		for i in res:
			text += f"{count} | {i[1]} - {i[2]} - {i[3]}\n"
			count += 1

		text += "Por favor elija el número del usuario."

		id_cliente = None

		while id_cliente is None:
			try:
				dialog = ct.CTkInputDialog(text=text, title="Elija usuario")
				id_cliente = int(dialog.get_input()) # waits for input
			except:
				messagebox.showerror(title="Sistema de Gestión Todo Aqua", message="Por favor ingrese un número")


		id_cliente = res[id_cliente-1][0]
	else:

		id_cliente = res[0][0]

	return id_cliente