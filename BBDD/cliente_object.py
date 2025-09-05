from BBDD.connect import get_single
from BBDD.connect import update_single
from Models.Cliente import Cliente
import customtkinter as ct


def cliente_object(id_cliente):

    query = "SELECT * FROM CLIENTES WHERE id_cliente = %s"

    param = (id_cliente,)

    client = get_single(query, param)

    client_object = Cliente(
        client["telefono"],
        client["nombre"],
        client["direccion"],
        client["localidad"],
        client["provincia"],
    )

    if not client["nif"]:

        while not client_object.nif:

            dialog = ct.CTkInputDialog(
                text="Ingrese Nif Cliente:", title="Sistema de Gestión Todo Aqua"
            )
            nif = dialog.get_input()  # waits for input

            if nif:
                client_object.nif = int(nif)

        query = "UPDATE CLIENTES SET NIF = %s WHERE ID_CLIENTE = %s;"
        param = (
            client_object.nif,
            id_cliente,
        )

        update_single(query, param)

    else:
        client_object.nif = client["nif"]

    if not client["cp"]:

        while not client_object.cp:

            dialog = ct.CTkInputDialog(
                text="Ingrese CP Cliente:", title="Sistema de Gestión Todo Aqua"
            )
            cp = dialog.get_input()  # waits for input
            if cp:
                client_object.cp = int(cp)

        query = "UPDATE CLIENTES SET CP = %s WHERE ID_CLIENTE = %s;"
        param = (
            client_object.cp,
            id_cliente,
        )

        update_single(param, query)

    else:
        client_object.cp = client["cp"]

    if not client["correo"]:

        while not client_object.correo:

            dialog = ct.CTkInputDialog(
                text="Ingrese Correo Cliente:", title="Sistema de Gestión Todo Aqua"
            )
            correo = dialog.get_input()
            if correo:
                client_object.correo = correo

        query = "UPDATE CLIENTES SET CORREO = %s WHERE ID_CLIENTE = %s;"
        param = (client_object.correo, id_cliente)

        update_single(query, param)

    else:
        client_object.correo = client["correo"]

    return client_object
