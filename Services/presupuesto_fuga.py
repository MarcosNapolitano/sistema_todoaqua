from Utils.search_client import search_client
from Services.Presupuesto import Presupuesto_Fuga_Piscinas

def presupuesto_fuga_piscinas(id_cliente = None):

	# si id_cliente es NONE entonces buscarlo en BBDD

	if not id_cliente:
		id_cliente = search_client()
		
	largo = input("\nIngrese largo: ")
	ancho = input("\nIngrese ancho: ")
	skimmer = input("\nIngrese skimmer: ")
	jacuzzi = input("\nIngrese jacuzzi: ")
	distancia = input("\nIngrese distancia: ")

	if skimmer == "Si" or skimmer == "si" or skimmer == "SI":
		skimmer = True
	else:
		skimmer = False

	if jacuzzi == "Si" or jacuzzi == "si" or jacuzzi == "SI":
		jacuzzi = True
	else:
		jacuzzi = False

	nuevo_presupuesto = Presupuesto_Fuga_Piscinas(distancia, largo, ancho, skimmer, jacuzzi, id_cliente)

	print(f"El presupuesto es de: {nuevo_presupuesto.tarifar()}")
	nuevo_presupuesto.id_cliente = id_cliente
	nuevo_presupuesto.save_presupuesto("fuga piscinas")

	del nuevo_presupuesto

	return True