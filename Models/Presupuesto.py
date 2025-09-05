from tkinter import messagebox
from Models.Cliente import Cliente
from Models.Tarifas import tarifas_fuga_piscinas
from Models.Tarifas import tarifas_todo_fugas
from Models.Tarifas import tarifas_elementos_lamina
from BBDD.connect import basic_exec, ultima_id, get_single
from math import floor


class Presupuesto:

    def __init__(self):
        self.id_cliente: int = 0
        self.fecha: str = ""
        self.precio: float = 0.0
        self.total: float = 0.0


class Presupuesto_Fuga_Piscinas(Presupuesto):

    def __init__(self):
        super().__init__()
        self.distancia: int = 0
        self.largo: int = 0
        self.ancho: int = 0
        self.skimmer: bool = False
        self.jacuzzi: bool = False

    def create_presupuesto(
        self,
        distancia: int,
        largo: int,
        ancho: int,
        skimmer: bool,
        jacuzzi: bool,
        id_cliente: int,
    ):
        self.distancia = distancia
        self.largo = largo
        self.ancho = ancho
        self.skimmer = skimmer
        self.jacuzzi = jacuzzi
        self.id_cliente = id_cliente

        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{self.__tarifar()}",
        )

        try:
            self.__save_presupuesto("fuga piscinas")

            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )

        except:
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )

    def __tarifar(self):

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
            self.precio = 999999.99
            return "Consultar"

        return self.total

    def __save_presupuesto(self, tipo):

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

        query = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
        param = (id_pres,)

        presupuesto = get_single(query, param)

        presupuesto_object = Presupuesto_Fuga_Piscinas()

        presupuesto_object.id_cliente = int(presupuesto["id_cliente"])
        presupuesto_object.distancia = int(presupuesto["distancia"])
        presupuesto_object.largo = int(presupuesto["largo"])
        presupuesto_object.ancho = int(presupuesto["ancho"])
        presupuesto_object.skimmer = bool(presupuesto["skimmer"])
        presupuesto_object.jacuzzi = bool(presupuesto["jacuzzi"])
        presupuesto_object.precio = float(presupuesto["precio"])
        presupuesto_object.total = float(presupuesto["total"])
        presupuesto_object.fecha = presupuesto["fecha"]

        return presupuesto_object

    def generar_archivo_presupuesto(
        self, cliente: "Cliente", presupuesto: "Presupuesto_Fuga_Piscinas"
    ):
        pass


class Presupuesto_Todo_Fugas(Presupuesto):

    def __init__(self):
        super().__init__()
        self.distancia: int = 0
        self.superficie: int = 90
        self.tipo_tuberia: str = ""

    def create_presupuesto(
        self, cliente: int, superficie: int, distancia: int, tipo_tuberia: str
    ):

        self.id_cliente = cliente
        self.superficie = superficie
        self.distancia = distancia
        self.tipo_tuberia = tipo_tuberia

        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{self.__tarifar()}",
        )

        try:
            self.__save_presupuesto("todo fugas")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )

        except:
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )

    def __tarifar(self):

        for i in tarifas_todo_fugas.keys():

            if self.distancia <= i:
                if self.superficie <= 120:
                    self.precio = tarifas_todo_fugas[i]
                    self.total = self.precio * 1.21
                break

        if not self.precio:
            self.precio = 999999.99
            return "Consultar"

        return self.total

    def __save_presupuesto(self, tipo):

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

        presupuesto = get_single(query_str, data)

        presupuesto_object = Presupuesto_Todo_Fugas()

        presupuesto_object.id_cliente = int(presupuesto["id_cliente"])
        presupuesto_object.distancia = int(presupuesto["distancia"])
        presupuesto_object.tipo_tuberia = presupuesto["tipo_tuberia"]
        presupuesto_object.superficie = int(presupuesto["superficie"])
        presupuesto_object.precio = float(presupuesto["precio"])
        presupuesto_object.total = float(presupuesto["total"])
        presupuesto_object.fecha = presupuesto["fecha"]

        return presupuesto_object

    def generar_archivo_presupuesto(
        self, cliente: "Cliente", presupuesto: "Presupuesto_Todo_Fugas"
    ):
        pass


class Presupuesto_Lamina(Presupuesto):

    def __init__(self):
        super().__init__()
        self.metros: float = 0.0
        self.impulsion: int = 0
        self.impulsion_precio: float = tarifas_elementos_lamina["impulsor"]
        self.barrefondo: int = 0
        self.barrefondo_precio: float = tarifas_elementos_lamina["barrefondo"]
        self.skimmers: int = 0
        self.skimmers_precio: float = tarifas_elementos_lamina["skimmer"]
        self.sumidero: int = 0
        self.sumidero_precio: float = tarifas_elementos_lamina["sumidero"]
        self.sumidero_grande: int = 0
        self.sumidero_grande_precio: float = tarifas_elementos_lamina["sumidero_grande"]
        self.nicho: int = 0
        self.nicho_precio: float = tarifas_elementos_lamina["nicho"]
        self.otros: int = 0
        self.otros_precio: float = 0.0
        self.otros_concepto: str = ""
        self.primera_partida: float = 0.0
        self.segunda_partida: float = 0.0
        self.tercera_partida: float = 0.0
        self.modelo: str = "A Definir"
        self.tarifa: float = 75.0

    def create_presupuesto(
        self, metros: float, modelo: str, tarifa: float, id_cliente: int
    ):
        self.metros = metros
        self.modelo = modelo
        self.tarifa = tarifa
        self.id_cliente = id_cliente

        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{self.__tarifar()}",
        )

        try:
            self.__save_presupuesto("lamina armada")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )

        except Exception as error:
            print(error)
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )

    def __tarifar(self):

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

    def __save_presupuesto(self, tipo):

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

        presupuesto_object = Presupuesto_Lamina()

        presupuesto_object.id_cliente = int(presupuesto["id_cliente"])
        presupuesto_object.metros = int(concepto["metros"])
        presupuesto_object.modelo = concepto["modelo"]
        presupuesto_object.tarifa = float(concepto["tarifa"])
        presupuesto_object.total = float(presupuesto["total"])
        presupuesto_object.fecha = presupuesto["fecha"]
        presupuesto_object.impulsion = int(concepto["impulsion"])
        presupuesto_object.impulsion_precio = float(concepto["impulsion_precio"])
        presupuesto_object.barrefondo = int(concepto["barrefondo"])
        presupuesto_object.barrefondo_precio = float(concepto["barrefondo_precio"])
        presupuesto_object.skimmers = int(concepto["skimmer"])
        presupuesto_object.skimmers_precio = float(concepto["skimmers_precio"])
        presupuesto_object.sumidero = int(concepto["sumidero"])
        presupuesto_object.sumidero_precio = float(concepto["sumidero_precio"])
        presupuesto_object.sumidero_grande = int(concepto["sumidero_grande"])
        presupuesto_object.sumidero_grande_precio = float(
            concepto["sumidero_grande_precio"]
        )
        presupuesto_object.nicho = int(concepto["nicho"])
        presupuesto_object.nicho_precio = float(concepto["nicho_precio"])
        presupuesto_object.otros = int(concepto["otros"])
        presupuesto_object.otros_concepto = concepto["otros_concepto"]
        presupuesto_object.otros_precio = float(concepto["otros_precio"])
        presupuesto_object.primera_partida = float(concepto["primera_partida"])
        presupuesto_object.segunda_partida = float(concepto["segunda_partida"])
        presupuesto_object.tercera_partida = float(concepto["tercera_partida"])

        return presupuesto_object

    def generar_archivo_presupuesto(
        self, cliente: "Cliente", presupuesto: "Presupuesto_Lamina"
    ):
        pass


class Presupuesto_Repa(Presupuesto):

    def __init__(self):
        super().__init__()

        # tuples array ("concepto", precio)
        self.concepto: list = []

    def create_presupuesto(self, id_cliente: int, conceptos: list):

        self.id_cliente = id_cliente

        for concepto in conceptos:
            if concepto[0] and concepto[1]:
                self.concepto.append(concepto)

        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{self.__tarifar()}",
        )

        try:
            self.__save_presupuesto("reparación")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )
        except:
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )

    def __tarifar(self):
        if self.concepto:
            for i in self.concepto:
                self.precio += i[1]

            self.total = self.precio * 1.21

        return self.total

    def __save_presupuesto(self, tipo):

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

    def object_presupuesto_repa(self, id_pres):

        query = "SELECT * FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s"
        param = (id_pres,)

        presupuesto = get_single(query, param)

        query = "SELECT CONCEPTO FROM CONCEPTOS_PRESUPUESTO WHERE ID_PRESUPUESTO = %s;"

        concepto = get_single(query, param)[0].split(";")

        presupuesto_object = Presupuesto_Repa()

        presupuesto_object.id_cliente = int(presupuesto["id_cliente"])

        for i in range(0, len(concepto), 2):
            if concepto[i] == "":
                break

            presupuesto_object.concepto.append((concepto[i], concepto[i + 1]))

        presupuesto_object.precio = float(presupuesto["precio"])
        presupuesto_object.total = float(presupuesto["total"])
        presupuesto_object.fecha = presupuesto["fecha"]

        return presupuesto_object

    def generar_archivo_presupuesto(
        self, cliente: "Cliente", presupuesto: "Presupuesto_Repa"
    ):
        pass
