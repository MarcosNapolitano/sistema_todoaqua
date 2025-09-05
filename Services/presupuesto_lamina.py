from Utils.search_client import search_client
from Services.Presupuesto import Presupuesto_Lamina

def presupuesto_lamina():

	id_client = search_client()

	while not id_client:
		id_client = search_client()

	def primera_partida(id_cliente):

		print("\n\n -- Primera Partida --\n")

		metros = input("\nIngrese metros cuadrados totales: ")

		while not metros:
			metros = input("\nIngrese metros cuadrados totales: ")

		tarifa = input("\nIngrese tarifa (75€ defecto): ") or 75.0
		modelo = input("\nIngrese Modelo (a definir por defecto): ") or "A definir"

		p = Presupuesto_Lamina(metros, modelo, tarifa, id_client)
		p.id_cliente = id_client

		return p

	def segunda_partida(p):

		print("\n\n -- Segunda Partida --\n")

		p.impulsion = input("\nIngrese cantidad de boquillas de impulsión: ") or None
		p.barrefondo = input("\nIngrese cantidad de boquillas de barrefondo: ")or None
		p.skimmers = input("\nIngrese cantidad de skimmers: ") or None
		p.sumidero = input("\nIngrese cantidad de sumideros de fondo: ") or None
		p.sumidero_grande = input("\nIngrese cantidad de sumideros de fondo grandes: ") or None
		p.nicho = input("\nIngrese cantidad de foco y nicho: ") or None

		return p

	def tercera_partida(p):

		print("\n\n -- Tercera Partida --\n")
		p.otros_concepto = input("\nIngrese Concepto: ") or None
		p.otros = input("\nIngrese Cantidad: ") or None
		p.otros_precio = input("\nIngrese Precio: ") or None

		return p

	p = tercera_partida(segunda_partida(primera_partida(id_client)))
	p.tarifar()
	p.save_presupuesto("lamina armada")

	return p.total






