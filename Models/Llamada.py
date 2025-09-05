from BBDD.connect import basic_exec


class Llamada:
    def __init__(self, telefono: str, nombre: str, motivo: str):

        self.telefono = telefono
        self.nombre = nombre
        self.motivo = motivo

    def save_llamada(self):

        query = "INSERT INTO LLAMADAS (telefono, nombre, motivo) VALUES (%s, %s, %s);"

        param = (
            self.telefono,
            self.nombre,
            self.motivo,
        )

        basic_exec(query, param)

        return "\nLlamada registrada correctamente\n"
