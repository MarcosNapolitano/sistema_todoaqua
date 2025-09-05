from BBDD.connect import basic_exec, ultima_id

class Cliente:
	def __init__(self, telefono: str,
					   nombre: str, 
					   direccion: str,
				 	   localidad: str, 
				 	   provincia: str):

		self.telefono = telefono
		self.nombre = nombre
		self.contacto = None
		self.direccion = direccion
		self.localidad = localidad
		self.provincia = provincia
		self.nif = None
		self.cp = None
		self.correo = None
	
	def save_client(self):

		query = "INSERT INTO CLIENTES (telefono, nombre, direccion, localidad, provincia) VALUES (%s, %s, %s, %s, %s);"

		data = (self.telefono, self.nombre, self.direccion, self.localidad, self.provincia, )
		
		basic_exec(query, data)
		query = "SELECT * FROM CLIENTES ORDER BY ID_CLIENTE DESC LIMIT 1"
		# recuperar aca la ultima id generada y retornarla
		print("\nCliente registrado correctamente\n")
		return ultima_id(query)

class Llamada:
	def __init__(self, telefono: str, nombre: str, motivo: str):
		
		self.telefono = telefono
		self.nombre = nombre
		self.motivo = motivo

	def save_llamada(self):

		query = "INSERT INTO LLAMADAS (telefono, nombre, motivo) VALUES (%s, %s, %s);"

		data = (self.telefono, self.nombre, self.motivo, )

		basic_exec(query, data)

		return "\nLlamada registrada correctamente\n"
