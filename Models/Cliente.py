from BBDD.connect import basic_exec, ultima_id


class Cliente:

    nif = ""
    contacto = ""
    nif = ""
    cp = ""
    correo = ""

    def __init__(
        self, telefono: str, nombre: str, direccion: str, localidad: str, provincia: str
    ):

        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia

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
