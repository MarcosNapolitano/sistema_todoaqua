from BBDD.connect import get_all

def search_pres(tipo):

	res = None
	while not res:

		cliente = input("\nIngrese Nombre Presupuesto: ")
		query = "SELECT id_presupuesto, nombre, tipo, fecha, total FROM presupuestos RIGHT JOIN CLIENTES ON presupuestos.id_cliente = clientes.id_cliente WHERE nombre ILIKE %s AND tipo = %s;";

		data = (f"%{cliente}%", tipo, )

		res = get_all(query, data)

		if not res:
			print("\nCliente no encontrado pruebe otra búsqueda\n")

	count = 1

	if len(res) > 1:
		print("\nResultados Obtenidos\n")
		for i in res:
			print(f"{count} | {i[1]} - {i[2]} - {i[3]} - {i[4]}\n")
			count += 1

		id_pres = None

		while not id_pres:
			id_pres = int(input("\nPor favor ingrese número elegido: \n"))

		res = res[id_pres-1]
	else:
		print(f"\nPresupuesto {res[0][2]} de {res[0][1]}\n")
		res = res[0]

	return res