from psycopg2 import Date
from Interface.llamada import presupuesto_todo_fugas
from Interface.presupuesto import presupuesto
from Models.Tarifas import tarifas_fuga_piscinas
from Models.Tarifas import tarifas_todo_fugas
from Models.Tarifas import tarifas_elementos_lamina
from BBDD.connect import basic_exec, ultima_id, get_single
from math import floor


class Presupuesto:

    def __init__(self, id_cliente: int):
        self.id_cliente = id_cliente
        self.fecha = Date
        self.precio = 0.0
        self.total = 0.0


class Presupuesto_Fuga_Piscinas(Presupuesto):

    def __init__(
        self,
        distancia: str,
        largo: int,
        ancho: int,
        skimmer: bool,
        jacuzzi: bool,
        id_cliente: int,
    ):
        super().__init__(id_cliente)
        self.distancia = int(distancia)
        self.largo = int(largo)
        self.ancho = int(ancho)
        self.skimmer = skimmer
        self.jacuzzi = jacuzzi

    def tarifar(self):

        for i in tarifas_fuga_piscinas.keys():

            if self.distancia <= i:

                sup = self.largo * self.ancho

                for j in tarifas_fuga_piscinas[i]:
                    if sup <= j[0]:
                        self.precio = j[1]
                        if self.jacuzzi:
                            self.precio += 250
                        self.total = self.precio * 1.21
                        break
                break

        if not self.precio:
            # to do: precio is not str
            self.precio = "Consultar"

        return self.total

    def save_presupuesto(self, tipo):

        query = "INSERT INTO PRESUPUESTOS (id_cliente, precio, total, tipo, distancia, largo, ancho, skimmer, jacuzzi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

        param = (
            self.id_cliente,
            self.precio,
            self.total,
            tipo,
            self.distancia,
            self.largo,
            self.ancho,
            self.skimmer,
            self.jacuzzi,
        )

        basic_exec(query, param)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True

    def object_presupuesto_piscina(self, id_pres):

        query_str = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
        data = (id_pres,)

        query = get_single(query_str, data)

        presupuesto = Presupuesto_Fuga_Piscinas(
            query["distancia"],
            query["largo"],
            query["ancho"],
            query["skimmer"],
            query["jacuzzi"],
            query["id_cliente"],
        )

        presupuesto.precio = query["precio"]
        presupuesto.total = query["total"]
        presupuesto.fecha = query["fecha"]

        return presupuesto


class Presupuesto_Todo_Fugas(Presupuesto):

    def __init__(
        self, distancia: int, tipo_tuberia: int, id_cliente: int, superficie=90
    ):
        super().__init__(id_cliente)
        self.distancia = int(distancia)
        self.superficie = int(superficie)
        self.tipo_tuberia = tipo_tuberia

    def tarifar(self):

        for i in tarifas_todo_fugas.keys():

            if self.distancia <= i:
                if self.superficie <= 120:
                    self.precio = tarifas_todo_fugas[i]
                    self.total = self.precio * 1.21
                break

        if not self.precio:
            self.precio = "Consultar"

        return self.total

    def save_presupuesto(self, tipo):

        query = "INSERT INTO PRESUPUESTOS (id_cliente, precio, total, tipo, skimmer, superficie, tipo_tuberia, distancia) VALUES (%s, %s, %s, %s, %s, %s, %s);"

        data = (
            self.id_cliente,
            self.precio,
            self.total,
            tipo,
            False,
            self.superficie,
            self.tipo_tuberia,
            self.distancia,
        )

        basic_exec(query, data)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True

    def object_presupuesto_fuga(self, id_pres):

        query_str = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
        data = (id_pres,)

        query = get_single(query_str, data)

        presupuesto = Presupuesto_Todo_Fugas(
            query["distancia"],
            query["tipo_tuberia"],
            query["id_cliente"],
            query["superficie"],
        )

        presupuesto.precio = query["precio"]
        presupuesto.total = query["total"]
        presupuesto.fecha = query["fecha"]

        return presupuesto


class Presupuesto_Lamina(Presupuesto):

    def __init__(self, metros: float, id_cliente: int, modelo="A Definir", tarifa=75):
        super().__init__(id_cliente)
        self.metros = float(metros)
        self.impulsion = 0
        self.impulsion_precio = tarifas_elementos_lamina["impulsor"]
        self.barrefondo = 0
        self.barrefondo_precio = tarifas_elementos_lamina["barrefondo"]
        self.skimmers = 0
        self.skimmers_precio = tarifas_elementos_lamina["skimmer"]
        self.sumidero = 0
        self.sumidero_precio = tarifas_elementos_lamina["sumidero"]
        self.sumidero_grande = 0
        self.sumidero_grande_precio = tarifas_elementos_lamina["sumidero_grande"]
        self.nicho = 0
        self.nicho_precio = tarifas_elementos_lamina["nicho"]
        self.otros = 0
        self.otros_precio = 0.0
        self.otros_concepto = ""
        self.primera_partida = 0.0
        self.segunda_partida = 0.0
        self.tercera_partida = 0.0
        self.modelo = modelo
        self.tarifa = float(tarifa)

    def tarifar(self):

        self.primera_partida = floor(self.metros * self.tarifa * 100) / 100.0

        if self.impulsion:
            self.segunda_partida += int(self.impulsion) * self.impulsion_precio
        if self.barrefondo:
            self.segunda_partida += int(self.barrefondo) * self.barrefondo_precio
        if self.skimmers:
            self.segunda_partida += int(self.skimmers) * self.skimmers_precio
        if self.sumidero:
            self.segunda_partida += int(self.sumidero) * self.sumidero_precio
        if self.sumidero_grande:
            self.segunda_partida += (
                int(self.sumidero_grande) * self.sumidero_grande_precio
            )
        if self.nicho:
            self.segunda_partida += int(self.nicho) * self.nicho_precio

        if self.otros:
            self.tercera_partida = int(self.otros) * float(self.otros_precio)

        self.precio = self.primera_partida + self.segunda_partida + self.tercera_partida
        self.total = self.precio * 1.21

        # si necesito redondear!
        # segunda_partida += math.floor(p.metros * p.tarifa * 100)/100.0

        return self.total

    def save_presupuesto(self, tipo):

        query = "INSERT INTO PRESUPUESTOS (id_cliente, precio, total, tipo) VALUES (%s, %s, %s, %s);"

        param = (
            self.id_cliente,
            self.precio,
            self.total,
            tipo,
        )

        basic_exec(query, param)

        query = "SELECT * FROM PRESUPUESTOS ORDER BY ID_PRESUPUESTO DESC LIMIT 1"

        presupuesto_id = ultima_id(query)

        query = "INSERT INTO CONCEPTOS_PRESUPUESTO (id_presupuesto, tipo, metros, impulsion, impulsion_precio, barrefondo, barrefondo_precio, skimmers, skimmers_precio, sumidero, sumidero_precio, sumidero_grande, sumidero_grande_precio, nicho, nicho_precio, otros, otros_precio, otros_concepto, primera_partida, segunda_partida, tercera_partida, modelo, tarifa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        param = (
            presupuesto_id,
            tipo,
            self.metros,
            self.impulsion,
            self.impulsion_precio,
            self.barrefondo,
            self.barrefondo_precio,
            self.skimmers,
            self.skimmers_precio,
            self.sumidero,
            self.sumidero_precio,
            self.sumidero_grande,
            self.sumidero_grande_precio,
            self.nicho,
            self.nicho_precio,
            self.otros,
            self.otros_precio,
            self.otros_concepto,
            self.primera_partida,
            self.segunda_partida,
            self.tercera_partida,
            self.modelo,
            self.tarifa,
        )

        basic_exec(query, param)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True

    def object_presupuesto_lamina(self, id_pres):

        query = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
        param = (id_pres,)

        presupuesto = get_single(query, param)

        query = "SELECT * FROM CONCEPTOS_PRESUPUESTO WHERE ID_PRESUPUESTO = %s;"

        concepto = get_single(query, param)

        presupuesto_object = Presupuesto_Lamina(
            concepto["metros"],
            presupuesto["id_cliente"],
            concepto["modelo"],
            concepto["tarifa"],
        )

        presupuesto_object.precio = float(presupuesto["precio"])
        presupuesto_object.total = float(presupuesto["total"])
        presupuesto_object.fecha = presupuesto["fecha"]
        presupuesto_object.impulsion = concepto["impulsion"]
        presupuesto_object.impulsion_precio = concepto["impulsion_precio"]
        presupuesto_object.barrefondo = concepto["barrefondo"]
        presupuesto_object.barrefondo_precio = concepto["barrefondo_precio"]
        presupuesto_object.skimmers = concepto["skimmer"]
        presupuesto_object.skimmers_precio = concepto["skimmers_precio"]
        presupuesto_object.sumidero = concepto["sumidero"]
        presupuesto_object.sumidero_precio = concepto["sumidero_precio"]
        presupuesto_object.sumidero_grande = concepto["sumidero_grande"]
        presupuesto_object.sumidero_grande_precio = concepto["sumidero_grande_precio"]
        presupuesto_object.nicho = concepto["nicho"]
        presupuesto_object.nicho_precio = concepto["nicho_precio"]
        presupuesto_object.otros = concepto["otros"]
        presupuesto_object.otros_concepto = concepto["otros_concepto"]
        presupuesto_object.otros_precio = concepto["otros_precio"]
        presupuesto_object.primera_partida = concepto["primera_partida"]
        presupuesto_object.segunda_partida = concepto["segunda_partida"]
        presupuesto_object.tercera_partida = concepto["tercera_partida"]

        return presupuesto


class Presupuesto_Repa(Presupuesto):

    def __init__(self, id_cliente: int):
        super().__init__(id_cliente)

        # tuples array ("concepto", precio)
        self.concepto = []

    def tarifar(self):
        if self.concepto:
            for i in self.concepto:
                self.precio += i[1]

            self.total = self.precio * 1.21

        return self.total

    def save_presupuesto(self, tipo):

        query = "INSERT INTO PRESUPUESTOS (id_cliente, precio, total, tipo) VALUES (%s, %s, %s, %s);"

        param = (
            self.id_cliente,
            self.precio,
            self.total,
            tipo,
        )

        basic_exec(query, param)

        query = "SELECT * FROM PRESUPUESTOS ORDER BY ID_PRESUPUESTO DESC LIMIT 1"

        presupuesto_id = ultima_id(query)

        concepto = ""

        for i in self.concepto:
            concepto += f"{i[0]};{i[1]};"

        query = "INSERT INTO CONCEPTOS_PRESUPUESTO (id_presupuesto, tipo, concepto) VALUES (%s, %s, %s);"

        param = (
            presupuesto_id,
            "reparación",
            concepto,
        )

        basic_exec(query, param)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True

    def pres_object_repa(self, id_pres):

        query = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
        param = (id_pres,)

        presupuesto  = get_single(query, param)

        query = "SELECT CONCEPTO FROM CONCEPTOS_PRESUPUESTO WHERE ID_PRESUPUESTO = %s;"

        concepto = get_single(query, param)[0].split(";")

        presupuesto_object = Presupuesto_Repa(presupuesto["id_cliente"])

        for i in range(0, len(concepto), 2):
            if concepto[i] == "":
                break

            presupuesto_object.concepto.append((concepto[i], concepto[i + 1]))

        presupuesto_object.id_cliente = presupuesto["id_cliente"]
        presupuesto_object.precio = presupuesto["precio"]
        presupuesto_object.total = presupuesto["total"]
        presupuesto_object.fecha = presupuesto["fecha"]

        return presupuesto_object
