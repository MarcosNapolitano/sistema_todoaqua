import customtkinter as ct
from BBDD.connect import get_all
from BBDD.connect import get_single
from Services.generar_presupuesto import generar_presupuesto

class Cons_Frame:

    def __init__(self, App, images):

        self.images = images
        # create consultas frame
        self.consultas_frame = ct.CTkFrame(App, corner_radius=0, fg_color="transparent")

        # main image
        self.consultas_frame_large_image_label = ct.CTkLabel(
            self.consultas_frame,
            text="Consultas",
            font=ct.CTkFont(size=30, weight="bold"),
            image=self.images.large_test_image,
        )
        self.consultas_frame_large_image_label.pack(
            side="top", anchor="w", padx=20, pady=10
        )

        # notebook
        self.tabview = ct.CTkTabview(master=self.consultas_frame)
        self.tabview.pack(anchor="w", padx=20, pady=20, fill="both", expand=True)

        self.consulta_cliente()
        self.consulta_presupuestos()

        return

    def consulta_cliente(self):

        self.tabview.add("Clientes")

        self.scrollable_frame = ct.CTkScrollableFrame(
            self.tabview.tab("Clientes"), orientation="horizontal"
        )
        self.scrollable_frame.pack(fill="both", expand=True)

        self.columns = ct.CTkFrame(self.scrollable_frame, fg_color=("gray80", "gray10"))
        self.columns.pack(fill="both", expand=True)
        self.columns.grid_columnconfigure(10)

        self.column1 = ct.CTkLabel(
            self.columns, text="Número", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column1.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.column2 = ct.CTkLabel(
            self.columns, text="Teléfono", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column2.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.column3 = ct.CTkLabel(
            self.columns, text="Nombre", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column3.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.column4 = ct.CTkLabel(
            self.columns, text="Contacto", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column4.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        self.column5 = ct.CTkLabel(
            self.columns, text="Dirección", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column5.grid(row=0, column=4, padx=20, pady=20, sticky="w")

        self.column6 = ct.CTkLabel(
            self.columns, text="Localidad", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column6.grid(row=0, column=5, padx=20, pady=20, sticky="w")

        self.column7 = ct.CTkLabel(
            self.columns, text="Provincia", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column7.grid(row=0, column=6, padx=20, pady=20, sticky="w")

        self.column8 = ct.CTkLabel(
            self.columns, text="NIF/DNI", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column8.grid(row=0, column=7, padx=20, pady=20, sticky="w")

        self.column9 = ct.CTkLabel(
            self.columns, text="CP", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column9.grid(row=0, column=8, padx=20, pady=20, sticky="w")

        self.column10 = ct.CTkLabel(
            self.columns, text="Correo", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column10.grid(row=0, column=9, padx=20, pady=20, sticky="w")

        query = "SELECT * FROM CLIENTES ORDER BY ID_CLIENTE LIMIT 10;"

        results = get_all(query)

        for i in range(len(results)):
            for j in range(len(results[i])):

                if j == 10:
                    break

                self.row1 = ct.CTkLabel(
                    self.columns, text=results[i][j], font=ct.CTkFont(size=15)
                )
                self.row1.grid(row=i + 1, column=j, padx=10, pady=10, sticky="w")

    def consulta_presupuestos(self):

        self.tabview.add("Presupuestos")

        self.scrollable_frame = ct.CTkScrollableFrame(
            self.tabview.tab("Presupuestos"), orientation="horizontal"
        )
        self.scrollable_frame.pack(fill="both", expand=True)

        self.columns = ct.CTkFrame(self.scrollable_frame, fg_color=("gray80", "gray10"))
        self.columns.pack(fill="both", expand=True)
        self.columns.grid_columnconfigure(10)

        self.column1 = ct.CTkLabel(
            self.columns, text="Número", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column1.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.column2 = ct.CTkLabel(
            self.columns, text="Nombre", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column2.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.column3 = ct.CTkLabel(
            self.columns, text="Fecha", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column3.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.column4 = ct.CTkLabel(
            self.columns, text="Aceptado", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column4.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        self.column5 = ct.CTkLabel(
            self.columns, text="Segundo Cont.", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column5.grid(row=0, column=4, padx=20, pady=20, sticky="w")

        self.column6 = ct.CTkLabel(
            self.columns, text="Observaciones", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column6.grid(row=0, column=5, padx=20, pady=20, sticky="w")

        self.column7 = ct.CTkLabel(
            self.columns, text="Precio", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column7.grid(row=0, column=6, padx=20, pady=20, sticky="w")

        self.column8 = ct.CTkLabel(
            self.columns, text="Total", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column8.grid(row=0, column=7, padx=20, pady=20, sticky="w")

        self.column9 = ct.CTkLabel(
            self.columns, text="Tipo", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column9.grid(row=0, column=8, padx=20, pady=20, sticky="w")

        self.column10 = ct.CTkLabel(
            self.columns, text="Distancia", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column10.grid(row=0, column=9, padx=20, pady=20, sticky="w")

        self.column11 = ct.CTkLabel(
            self.columns, text="Largo", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column11.grid(row=0, column=10, padx=20, pady=20, sticky="w")

        self.column12 = ct.CTkLabel(
            self.columns, text="Ancho", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column12.grid(row=0, column=11, padx=20, pady=20, sticky="w")

        self.column13 = ct.CTkLabel(
            self.columns, text="Skimmer", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column13.grid(row=0, column=12, padx=20, pady=20, sticky="w")

        self.column14 = ct.CTkLabel(
            self.columns, text="Jacuzzi", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column14.grid(row=0, column=13, padx=20, pady=20, sticky="w")

        self.column15 = ct.CTkLabel(
            self.columns, text="Superficie", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column15.grid(row=0, column=14, padx=20, pady=20, sticky="w")

        self.column16 = ct.CTkLabel(
            self.columns, text="Tubería", font=ct.CTkFont(size=15, weight="bold")
        )
        self.column16.grid(row=0, column=15, padx=20, pady=20, sticky="w")

        query = "SELECT * FROM PRESUPUESTOS ORDER BY ID_PRESUPUESTO LIMIT 10;"

        results = get_all(query)

        for i in range(len(results)):
            for j in range(len(results[i])):

                text = results[i][j]

                if text == False:
                    text = "No"

                if text == True:
                    text = "Si"

                if j == 1:
                    text = get_single(
                        "SELECT NOMBRE FROM CLIENTES WHERE ID_CLIENTE = %s", (text,)
                    )[0]

                if isinstance(text, str):
                    text = text.title()

                self.row1 = ct.CTkLabel(
                    self.columns, text=text, font=ct.CTkFont(size=15)
                )
                self.row1.grid(row=i + 1, column=j, padx=10, pady=10, sticky="w")

        self.imprimir = ct.CTkFrame(self.tabview.tab("Presupuestos"))
        self.imprimir.pack(side="bottom")
        self.imprimir.grid_columnconfigure(2)

        self.entry1 = ct.CTkEntry(self.imprimir, placeholder_text="Ingrese número")
        self.entry1.grid(column=0, row=0, padx=10, pady=10)

        id_presupuesto = int(self.entry1.get() or 0)

        def request_presupuesto():
            generar_presupuesto(id_presupuesto)

        self.button1 = ct.CTkButton(
            self.imprimir, text="Imprimir Presupuesto", command=request_presupuesto
        )
        self.button1.grid(column=1, row=0, padx=10, pady=10)
