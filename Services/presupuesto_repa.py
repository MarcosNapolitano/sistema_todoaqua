from Utils.search_client import search_client
from Services.Presupuesto import Presupuesto_Repa

def presupuesto_repa():
	
	id_cliente = search_client()

	while not id_cliente:
		id_cliente = search_client()

	p = Presupuesto_Repa(id_cliente)

	while True:
		concepto = input("\nIngrese concepto: ")
		precio = input("\nIngrese precio: ")

		if concepto and precio:
			p.concepto.append((concepto,float(precio)))

		exit = input("\nDesea agregar más conceptos?\n0 - No\n1 - Si\n")

		if exit == "0":
			break

	p.tarifar()
	p.id_cliente = id_cliente
	p.save_presupuesto("reparación")

	return True