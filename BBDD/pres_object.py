from BBDD.connect import get_single
from Models.Presupuesto import (
    Presupuesto_Repa,
    Presupuesto_Fuga_Piscinas,
    Presupuesto_Todo_Fugas,
    Presupuesto_Lamina,
)


def pres_object_piscina(id_pres):

    query_str = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
    data = (id_pres,)

    query = get_single(query_str, data)

    presupuesto = Presupuesto_Fuga_Piscinas(
        query[9], query[10], query[11], query[12], query[13], query[1]
    )

    presupuesto.id_cliente = query[1]
    presupuesto.precio = query[6]
    presupuesto.total = query[7]
    presupuesto.fecha = query[2]

    return presupuesto


def pres_object_fuga(id_pres):

    query_str = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
    data = (id_pres,)

    query = get_single(query_str, data)

    presupuesto = Presupuesto_Todo_Fugas(query[9], query[14], query[15], query[1])

    presupuesto.id_cliente = query[1]
    presupuesto.precio = query[6]
    presupuesto.total = query[7]
    presupuesto.fecha = query[2]

    return presupuesto


def pres_object_repa(id_pres):

    query_str = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
    data = (id_pres,)

    query = get_single(query_str, data)

    query_c = "SELECT CONCEPTO FROM CONCEPTOS_PRESUPUESTO WHERE ID_PRESUPUESTO = %s;"

    concepto = get_single(query_c, data)[0].split(";")

    presupuesto = Presupuesto_Repa(query[1])

    for i in range(0, len(concepto), 2):
        if concepto[i] == "":
            break

        presupuesto.concepto.append((concepto[i], concepto[i + 1]))

    presupuesto.id_cliente = query[1]
    presupuesto.precio = query[6]
    presupuesto.total = query[7]
    presupuesto.fecha = query[2]

    return presupuesto


def pres_object_lamina(id_pres):

    query_str = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
    data = (id_pres,)

    query = get_single(query_str, data)

    query_c = "SELECT * FROM CONCEPTOS_PRESUPUESTO WHERE ID_PRESUPUESTO = %s;"

    concepto = get_single(query_c, data)

    presupuesto = Presupuesto_Lamina(concepto[2], concepto[21], concepto[22], query[1])

    presupuesto.id_cliente = query[1]
    presupuesto.precio = float(query[6])
    presupuesto.total = float(query[7])
    presupuesto.fecha = query[2]
    presupuesto.impulsion = concepto[3]
    presupuesto.impulsion_precio = concepto[4]
    presupuesto.barrefondo = concepto[5]
    presupuesto.barrefondo_precio = concepto[6]
    presupuesto.skimmers = concepto[7]
    presupuesto.skimmers_precio = concepto[8]
    presupuesto.sumidero = concepto[9]
    presupuesto.sumidero_precio = concepto[10]
    presupuesto.sumidero_grande = concepto[11]
    presupuesto.sumidero_grande_precio = concepto[12]
    presupuesto.nicho = concepto[13]
    presupuesto.nicho_precio = concepto[14]
    presupuesto.otros = concepto[15]
    presupuesto.otros_concepto = concepto[16]
    presupuesto.otros_precio = concepto[17]
    presupuesto.primera_partida = concepto[18]
    presupuesto.segunda_partida = concepto[19]
    presupuesto.tercera_partida = concepto[20]

    return presupuesto
