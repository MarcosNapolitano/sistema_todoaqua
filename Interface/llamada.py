from Services.Cliente import Cliente
from Services.Cliente import Llamada
from Utils.presupuesto_fuga import presupuesto_fuga_piscinas
from Utils.presupuesto_todofugas import presupuesto_todo_fugas

def llamada(separator_string):

	wellcome_string = "Qué desea registrar?\n"
	main_options = "Elija una opción:\n\n01 - Cliente\n02 - Llamada General\n\n"

	def client_choice(separator_string):

		print("\n" + separator_string)
		print(wellcome_string) 
		print(separator_string)

		selection = input(main_options)

		match selection:

			case "1":

				telefono = input("\nIngrese teléfono: ")
				nombre = input("\nIngrese nombre: ")
				direccion = input("\nIngrese direccion: ")
				localidad = input("\nIngrese localidad: ")
				provincia = input("\nIngrese provincia: ")
				
				cliente = Cliente(telefono, nombre, direccion, localidad, provincia)

				id_cliente = cliente.save_client()

				tipo_presupuesto = input("\nQué tipo de fuga?\n\n1 - Piscina\n2 - Domicilio\n\n")

				"""
				implementar mejor esto, porque al ser 2 no es 1 y al ser 1 no es 2
				while tipo_presupuesto != "1" or tipo_presupuesto != "2":
					print("Por favor seleccione una opción válida\n")
					tipo_presupuesto = input("\nQué tipo de fuga?\n\n1 - Piscina\n2 - Domicilio\n\n")
				"""

				if tipo_presupuesto == "1":
					presupuesto_fuga_piscinas(id_cliente)
				else:
					presupuesto_todo_fugas(id_cliente)

				del cliente

				return True

			case "2":

				telefono = input("\nIngrese teléfono: ")
				nombre = input("\nIngrese nombre: ")
				motivo = input("\nIngrese motivo: ")

				llamada = Llamada(telefono, nombre, motivo)

				# guarda que esto retorne True siempre, 
				return llamada.save_llamada()

			case other:
				print("\nPor favor elija una opción válida\n") 
				return False


	selection = client_choice(separator_string)

	while not selection:
		selection = client_choice(separator_string)

	return False