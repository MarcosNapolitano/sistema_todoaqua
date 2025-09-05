from Utils.presupuesto_fuga import presupuesto_fuga_piscinas
from Utils.presupuesto_todofugas import presupuesto_todo_fugas
from Utils.presupuesto_lamina import presupuesto_lamina
from Utils.presupuesto_repa import presupuesto_repa


def crear_presupuesto(separator_string):

	wellcome_string = "Qué Presupuesto Desea Crear?\n"
	main_options = "Elija una opción:\n\n01 - Fuga Piscinas\n02 - Todo Fugas\n03 - Midas Piscinas - Lámina Armada\n04 - Midas Piscinas - Reparación\n\n"

	def first_choice(separator_string):

		print("\n" + separator_string)
		print(wellcome_string) 
		print(separator_string)

		selection = input(main_options)

		match selection:

			case "1":
				return presupuesto_fuga_piscinas()

			case "2":
				return presupuesto_todo_fugas()

			case "3":
				return presupuesto_lamina()

			case "4":
				return presupuesto_repa()

			case other:
				print("\nPor favor elija una opción válida\n") 
				return False


	selection = first_choice(separator_string)

	while not selection:
		selection = first_choice(separator_string)

	return False
