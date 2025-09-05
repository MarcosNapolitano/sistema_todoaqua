from Interface.llamada import llamada
from Interface.presupuesto import presupuesto

def action_choice(separator_string):

	action_options = "Acciones Disponibles\n"
	main_actions = "Elija una opción:\n\n01 - Alta Cliente\n02 - Presupuesto\n03 - Actuación\n04 - Volver al menú anterior\n\n"
		
	print("\n" + separator_string)
	print(action_options)
	print(separator_string)

	selection = input(main_actions)

	match selection:

		case "1":
			return llamada(separator_string)

		case "2":
			return presupuesto(separator_string)

		case "3":
			print("\nestas dando actuaciones")
			return False

		case "4":
			return True

		case other:
			print("\nPor favor elija una opción válida\n") 
			return False