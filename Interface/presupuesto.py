from Interface.generar_documento import generate
from Interface.crear_presupuesto import crear_presupuesto

def presupuesto(separator_string):

	wellcome_string = "Qué desea hacer?\n"
	main_options = "Elija una opción:\n\n01 - Crear Presupuesto\n02 - Generar Documento\n03 - Volver al menú anterior\n\n"

	def first_choice(separator_string):

		print("\n" + separator_string)
		print(wellcome_string) 
		print(separator_string)

		selection = input(main_options)

		match selection:

			case "1":

				return crear_presupuesto(separator_string)

			case "2":

				return generate(separator_string) 
				
			case "3":

				return True

			case other:
				
				print("\nPor favor elija una opción válida\n") 
				return False


	selection = first_choice(separator_string)

	while not selection:
		selection = first_choice(separator_string)

	return False