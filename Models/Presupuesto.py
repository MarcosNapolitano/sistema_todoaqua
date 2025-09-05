from Services.Tarifas import tarifas_fuga_piscinas
from Services.Tarifas import tarifas_todo_fugas
from BBDD.connect import basic_exec, ultima_id
from math import floor


class Presupuesto:

    def __init__(self, id_cliente=None):
        self.id_cliente = id_cliente
        self.fecha = None
        self.precio = 0.0
        self.total = 0.0

        # los parametros opcionales habría que borrarlos a futuro
        # los dejo aca como guia para armar la tabla luego
        # pero no hacen al funcionamiento del sistema
        # sería mejor implementar metodos que modifquen directamente
        # la tabla SQL


class Presupuesto_Fuga_Piscinas(Presupuesto):

    def __init__(self, distancia, largo, ancho, skimmer, jacuzzi, id_cliente=None):
        super().__init__(id_cliente=None)
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
            self.precio = "Consultar"

        return self.total

    def save_presupuesto(self, tipo):

        query = "INSERT INTO PRESUPUESTOS (id_cliente, precio, total, tipo, distancia, largo, ancho, skimmer, jacuzzi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

        data = (
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

        basic_exec(query, data)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True


class Presupuesto_Todo_Fugas(Presupuesto):

    def __init__(self, distancia, tipo_tuberia, superficie=90, id_cliente=None):
        super().__init__(id_cliente=None)
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


class Presupuesto_Lamina(Presupuesto):

    def __init__(self, metros, modelo="A Definir", tarifa=75, id_cliente=None):
        super().__init__(id_cliente=None)
        self.metros = float(metros)
        self.impulsion = None
        self.impulsion_precio = 95.0
        self.barrefondo = None
        self.barrefondo_precio = 95.0
        self.skimmers = None
        self.skimmers_precio = 350.0
        self.sumidero = None
        self.sumidero_precio = 250.0
        self.sumidero_grande = None
        self.sumidero_grande_precio = 450.0
        self.nicho = None
        self.nicho_precio = 425.0
        self.otros = None
        self.otros_precio = 0.0
        self.otros_concepto = None
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

        data = (
            self.id_cliente,
            self.precio,
            self.total,
            tipo,
        )

        basic_exec(query, data)

        query = "SELECT * FROM PRESUPUESTOS ORDER BY ID_PRESUPUESTO DESC LIMIT 1"

        p_id = ultima_id(query)

        query = "INSERT INTO CONCEPTOS_PRESUPUESTO (id_presupuesto, tipo, metros, impulsion, impulsion_precio, barrefondo, barrefondo_precio, skimmers, skimmers_precio, sumidero, sumidero_precio, sumidero_grande, sumidero_grande_precio, nicho, nicho_precio, otros, otros_precio, otros_concepto, primera_partida, segunda_partida, tercera_partida, modelo, tarifa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        data = (
            p_id,
            "lamina armada",
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

        print(data)

        basic_exec(query, data)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True


class Presupuesto_Repa(Presupuesto):

    def __init__(self, id_cliente=None):
        super().__init__(id_cliente=None)

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

        data = (
            self.id_cliente,
            self.precio,
            self.total,
            tipo,
        )

        basic_exec(query, data)

        query = "SELECT * FROM PRESUPUESTOS ORDER BY ID_PRESUPUESTO DESC LIMIT 1"

        p_id = ultima_id(query)

        concepto = ""

        for i in self.concepto:
            concepto += f"{i[0]};{i[1]};"

        query = "INSERT INTO CONCEPTOS_PRESUPUESTO (id_presupuesto, tipo, concepto) VALUES (%s, %s, %s);"

        data = (
            p_id,
            "reparación",
            concepto,
        )

        basic_exec(query, data)

        print(f"\nGuardaste tu presupuesto {tipo} en la base de datos\n")

        return True
