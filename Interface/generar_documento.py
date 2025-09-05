from Utils.generar_presupuesto_fuga_piscinas import generar_presupuesto_fuga_piscinas
from Utils.generar_presupuesto_todo_fugas import generar_presupuesto_todo_fugas
from Utils.generar_presupuesto_lamina import generar_presupuesto_lamina
from Utils.generar_presupuesto_repa import generar_presupuesto_repa
from BBDD.pres_object import pres_object_fuga, pres_object_lamina, pres_object_piscina, pres_object_repa
from BBDD.cliente_object import cliente_object


def generate(separator_string):

	wellcome_string = "Qué Presupuesto Desea Generar?\n"
	main_options = "Elija una opción:\n\n01 - Fuga Piscinas\n02 - Todo Fugas\n03 - Midas Piscinas - Lámina Armada\n04 - Midas Piscinas - Reparación\n\n"

	def first_choice(separator_string):

		print("\n" + separator_string)
		print(wellcome_string) 
		print(separator_string)

		selection = input(main_options)

		match selection:

			case "1":

				presupuesto = pres_object_piscina("fuga piscinas")
				cliente = cliente_object(presupuesto.id_cliente)
				
				print("\nPresupuesto generado!\n")
				return generar_presupuesto_fuga_piscinas(cliente, presupuesto)

			case "2":

				presupuesto = pres_object_fuga("todo fugas")
				cliente = cliente_object(presupuesto.id_cliente)

				print("\nPresupuesto generado!\n")
				return generar_presupuesto_todo_fugas(cliente, presupuesto)

			case "3":

				presupuesto = pres_object_lamina("lamina armada")
				cliente = cliente_object(presupuesto.id_cliente)

				print("\nPresupuesto generado!\n")
				return generar_presupuesto_lamina(cliente, presupuesto)

			case "4":

				presupuesto = pres_object_repa("reparación")
				cliente = cliente_object(presupuesto.id_cliente)

				print("\nPresupuesto generado!\n")
				return generar_presupuesto_repa(cliente, presupuesto)

			case other:
				print("\nPor favor elija una opción válida\n") 
				return False


	selection = first_choice(separator_string)

	while not selection:
		selection = first_choice(separator_string)

	return False