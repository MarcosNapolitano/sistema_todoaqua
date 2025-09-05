from BBDD.connect import basic_exec, ultima_id, get_single, update_single
import customtkinter as ct


class Cliente:

    def __init__(
        self, telefono: str, nombre: str, direccion: str, localidad: str, provincia: str
    ):

        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia
        self.nif = 0
        self.contacto = ""
        self.cp = 0
        self.correo = ""

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def save_client(self):

        query = "INSERT INTO CLIENTES (telefono, nombre, direccion, localidad, provincia) VALUES (%s, %s, %s, %s, %s);"

        data = (
            self.telefono,
            self.nombre,
            self.direccion,
            self.localidad,
            self.provincia,
        )

        basic_exec(query, data)
        query = "SELECT * FROM CLIENTES ORDER BY ID_CLIENTE DESC LIMIT 1"

        # recuperar aca la ultima id generada y retornarla
        print("\nCliente registrado correctamente\n")
        return ultima_id(query)

    def cliente_object(self, id_cliente):

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

            self.__check_update_property(client_object, client, "nif")

        else:
            client_object.nif = client["nif"]

        if not client["cp"]:
            self.__check_update_property(client_object, client, "cp")

        else:
            client_object.cp = client["cp"]

        if not client["correo"]:

            self.__check_update_property(client_object, client, "correo")

        else:
            client_object.correo = client["correo"]

        return client_object

    def __check_update_property(
        self, client_object: "Cliente", client: dict, property: str
    ):

        while not client[property]:

            dialog = ct.CTkInputDialog(
                text=f"Ingrese {property.title()} Cliente:",
                title="Sistema de Gestión Todo Aqua",
            )
            new_property = dialog.get_input()
            if new_property:
                client_object[property] = property

        query = f"UPDATE CLIENTES SET {property.upper()} = %s WHERE ID_CLIENTE = %s;"
        param = (property, client["id_cliente"])

        update_single(query, param)
