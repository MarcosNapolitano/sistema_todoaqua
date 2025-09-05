from Services.Presupuesto import Presupuesto_Todo_Fugas
from Utils.search_client import search_client

def presupuesto_todo_fugas(id_cliente = None):

	#si id = None hacer query en BBDD

	if not id_cliente:
		id_cliente = search_client()

	superficie = input("\nIngrese superficie aprox en m2\n(El valor por defecto es el de un adosado de 90m2): ")
	distancia = input("\nIngrese distancia: ")
	tipo = input("\nEs tubería Doméstica, Urbanización o Comercial?: ")

	if not superficie:
		superficie = 90

	nuevo_presupuesto = Presupuesto_Todo_Fugas(distancia, tipo, superficie, id_cliente)

	print(f"El presupuesto es de: {nuevo_presupuesto.tarifar()}")

	nuevo_presupuesto.id_cliente = id_cliente

	nuevo_presupuesto.save_presupuesto("todo fugas")

	del nuevo_presupuesto

	return True