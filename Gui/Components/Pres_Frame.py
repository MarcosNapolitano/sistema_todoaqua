import customtkinter as ct
from tkinter import messagebox
from Utils.search_client import search_client
from Services.Presupuesto import Presupuesto_Fuga_Piscinas
from Services.Presupuesto import Presupuesto_Todo_Fugas
from Services.Presupuesto import Presupuesto_Repa
from Services.Presupuesto import Presupuesto_Lamina


class Pres_Frame:

    def __init__(self, App, images):

        self.images = images

        self.presupuesto_frame_1 = ct.CTkFrame(
            App, corner_radius=0, fg_color="transparent"
        )

        self.presupuesto_frame_2 = ct.CTkFrame(
            App, corner_radius=0, fg_color="transparent"
        )

        self.presupuesto_frame_3 = ct.CTkFrame(
            App, corner_radius=0, fg_color="transparent"
        )

        self.presupuesto_frame_4 = ct.CTkFrame(
            App, corner_radius=0, fg_color="transparent"
        )

        self.change_presupuesto("Fuga Piscinas")

    def create_presupuesto_piscina(self):

        cliente = self.presupuesto_frame_entry_1.get()
        largo = self.presupuesto_frame_entry_2.get()
        ancho = self.presupuesto_frame_entry_3.get()
        distancia = self.presupuesto_frame_entry_4.get()
        skimmer = self.presupuesto_frame_label_5.get()
        jacuzzi = self.presupuesto_frame_label_6.get()

        if cliente == "" or largo == "" or ancho == "" or distancia == "":

            self.presupuesto_frame_label_100.configure(text="Faltan Datos.")
            return

        self.presupuesto_frame_label_100.configure(text="")
        id_cliente = search_client(cliente)

        if not id_cliente:
            return

        nuevo_presupuesto = Presupuesto_Fuga_Piscinas(
            distancia, largo, ancho, skimmer, jacuzzi, id_cliente
        )

        nuevo_presupuesto.id_cliente = id_cliente
        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{nuevo_presupuesto.tarifar()}",
        )

        try:
            nuevo_presupuesto.save_presupuesto("fuga piscinas")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )
            del nuevo_presupuesto

        except:
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )
            del nuevo_presupuesto
            return

        self.presupuesto_frame_entry_1.delete(0, "end")
        self.presupuesto_frame_entry_2.delete(0, "end")
        self.presupuesto_frame_entry_3.delete(0, "end")
        self.presupuesto_frame_entry_4.delete(0, "end")
        self.presupuesto_frame_label_5.deselect()
        self.presupuesto_frame_label_6.deselect()

        return

    def create_presupuesto_repa(self):

        cliente = self.presupuesto_frame_entry_1.get()
        concepto_1 = self.presupuesto_frame_entry_2.get()
        precio_1 = self.presupuesto_frame_entry_3.get()
        concepto_2 = self.presupuesto_frame_entry_4.get()
        precio_2 = self.presupuesto_frame_entry_5.get()
        concepto_3 = self.presupuesto_frame_entry_6.get()
        precio_3 = self.presupuesto_frame_entry_7.get()
        concepto_4 = self.presupuesto_frame_entry_8.get()
        precio_4 = self.presupuesto_frame_entry_9.get()

        if cliente == "" or concepto_1 == "" or precio_1 == "":
            self.presupuesto_frame_label_100.configure(text="Faltan Datos.")
            return

        self.presupuesto_frame_label_100.configure(text="")
        id_cliente = search_client(cliente)

        if not id_cliente:
            return

        nuevo_presupuesto = Presupuesto_Repa(id_cliente)

        nuevo_presupuesto.concepto.append((concepto_1, float(precio_1)))

        if concepto_2 != "" and precio_2 != "":
            nuevo_presupuesto.concepto.append((concepto_2, float(precio_2)))

        if concepto_3 != "" and precio_3 != "":
            nuevo_presupuesto.concepto.append((concepto_3, float(precio_3)))

        if concepto_4 != "" and precio_4 != "":
            nuevo_presupuesto.concepto.append((concepto_4, float(precio_4)))

        nuevo_presupuesto.id_cliente = id_cliente
        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{nuevo_presupuesto.tarifar()}",
        )

        try:
            nuevo_presupuesto.save_presupuesto("reparación")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )
            del nuevo_presupuesto

        except:
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )
            del nuevo_presupuesto
            return

        self.presupuesto_frame_entry_1.delete(0, "end")
        self.presupuesto_frame_entry_1.delete(0, "end")
        self.presupuesto_frame_entry_2.delete(0, "end")
        self.presupuesto_frame_entry_3.delete(0, "end")
        self.presupuesto_frame_entry_4.delete(0, "end")
        self.presupuesto_frame_entry_5.delete(0, "end")
        self.presupuesto_frame_entry_6.delete(0, "end")
        self.presupuesto_frame_entry_7.delete(0, "end")
        self.presupuesto_frame_entry_8.delete(0, "end")
        self.presupuesto_frame_entry_9.delete(0, "end")

        return

    def create_presupuesto_lamina(self):

        def check_dec_point(var, var_name, entero=False):

            try:
                if entero:
                    var = int(var)
                else:
                    var = var.replace(",", ".")
                    var = float(var)
                return var

            except:
                messagebox.showinfo(
                    title="Sistema de Gestión Todo Aqua",
                    message=f"{var_name} debe ser un número.",
                )
                return False

        cliente = self.presupuesto_frame_entry_1.get()
        metros = self.presupuesto_frame_entry_2.get()
        tarifa = self.presupuesto_frame_entry_3.get()
        modelo = self.presupuesto_frame_entry_4.get()
        impulsiones = self.presupuesto_frame_entry_5.get()
        barrefondos = self.presupuesto_frame_entry_6.get()
        skimmers = self.presupuesto_frame_entry_7.get()
        focos = self.presupuesto_frame_entry_8.get()
        sumideros = self.presupuesto_frame_entry_9.get()
        sumideros_grande = self.presupuesto_frame_entry_10.get()
        concepto_1 = self.presupuesto_frame_entry_11.get()
        precio_1 = self.presupuesto_frame_entry_12.get()

        if cliente == "" or metros == "":
            self.presupuesto_frame_label_100.configure(text="Faltan Datos.")
            return

        if tarifa != "":
            tarifa = check_dec_point(tarifa, "Tarifa")
            if not tarifa:
                return
        else:
            tarifa = 75

        if modelo == "":
            modelo = "A Definir"

        self.presupuesto_frame_label_100.configure(text="")
        id_cliente = search_client(cliente)

        if not id_cliente:
            return

        metros = check_dec_point(tarifa, "Metros", True)

        if not metros:
            return

        nuevo_presupuesto = Presupuesto_Lamina(metros, modelo, tarifa, id_cliente)

        nuevo_presupuesto.id_cliente = id_cliente

        if impulsiones != "":

            impulsiones = check_dec_point(impulsiones, "Impulsiones", True)

            if not impulsiones:
                return
            nuevo_presupuesto.impulsion = impulsiones

        if barrefondos != "":

            barrefondos = check_dec_point(barrefondos, "Barrefondos", True)

            if not barrefondos:
                return
            nuevo_presupuesto.barrefondo = barrefondos

        if skimmers != "":

            skimmers = check_dec_point(skimmers, "Skimmers", True)

            if not skimmers:
                return
            nuevo_presupuesto.skimmers = skimmers

        if sumideros != "":

            sumideros = check_dec_point(sumideros, "Sumideros", True)

            if not sumideros:
                return
            nuevo_presupuesto.sumidero = sumideros

        if sumideros_grande != "":

            sumideros_grande = check_dec_point(
                sumideros_grande, "Sumideros Grandes", True
            )

            if not sumideros_grande:
                return
            nuevo_presupuesto.sumidero_grande = sumideros_grande

        if focos != "":

            focos = check_dec_point(focos, "Focos", True)

            if not focos:
                return
            nuevo_presupuesto.nicho = focos

        if concepto_1 != "" and precio_1 != "":

            nuevo_presupuesto.otros = 1
            precio_1 = check_dec_point(precio_1, "Precio", True)

            if not precio_1:
                return

            nuevo_presupuesto.otros_concepto = concepto_1
            nuevo_presupuesto.otros_precio = precio_1

        nuevo_presupuesto.id_cliente = id_cliente
        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{nuevo_presupuesto.tarifar()}",
        )

        try:
            nuevo_presupuesto.save_presupuesto("lámina armada")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )
            del nuevo_presupuesto

        except Exception as error:
            print(error)
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )
            del nuevo_presupuesto
            return

        self.presupuesto_frame_entry_1.delete(0, "end")
        self.presupuesto_frame_entry_1.delete(0, "end")
        self.presupuesto_frame_entry_2.delete(0, "end")
        self.presupuesto_frame_entry_3.delete(0, "end")
        self.presupuesto_frame_entry_4.delete(0, "end")
        self.presupuesto_frame_entry_5.delete(0, "end")
        self.presupuesto_frame_entry_6.delete(0, "end")
        self.presupuesto_frame_entry_7.delete(0, "end")
        self.presupuesto_frame_entry_8.delete(0, "end")
        self.presupuesto_frame_entry_9.delete(0, "end")
        self.presupuesto_frame_entry_10.delete(0, "end")
        self.presupuesto_frame_entry_11.delete(0, "end")
        self.presupuesto_frame_entry_12.delete(0, "end")

        return

    def create_presupuesto_fuga(self):

        cliente = self.presupuesto_frame_entry_1.get()
        superficie = self.presupuesto_frame_entry_2.get()
        distancia = self.presupuesto_frame_entry_3.get()
        tipo = self.presupuesto_frame_entry_4.get()

        if cliente == "" or distancia == "":

            self.presupuesto_frame_label_100.configure(text="Faltan Datos.")
            return

        if superficie == "":
            superficie = 90

        self.presupuesto_frame_label_100.configure(text="")
        id_cliente = search_client(cliente)

        if not id_cliente:
            return

        nuevo_presupuesto = Presupuesto_Todo_Fugas(
            distancia, tipo, superficie, id_cliente
        )

        nuevo_presupuesto.id_cliente = id_cliente
        messagebox.showinfo(
            title="Sistema de Gestión Todo Aqua",
            message=f"El presupuesto es de: €{nuevo_presupuesto.tarifar()}",
        )

        try:
            nuevo_presupuesto.save_presupuesto("todo fugas")
            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message=f"Presupuesto guardado correctamente.",
            )
            del nuevo_presupuesto

        except:
            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message=f"Error al crear presupuesto. Contacte al administrador.",
            )
            del nuevo_presupuesto
            return

        self.presupuesto_frame_entry_1.delete(0, "end")
        self.presupuesto_frame_entry_2.delete(0, "end")
        self.presupuesto_frame_entry_3.delete(0, "end")
        self.presupuesto_frame_entry_4.set("Doméstica")

        return

    # user choice
    def change_presupuesto(self, option):

        self.presupuesto_frame_1.grid_forget()
        self.presupuesto_frame_2.grid_forget()
        self.presupuesto_frame_3.grid_forget()
        self.presupuesto_frame_4.grid_forget()

        if option == "Todo Fugas":
            self.presupuesto_fuga()

        if option == "Fuga Piscinas":
            self.presupuesto_piscina()

        if option == "Lámina Armada":
            self.presupuesto_lamina()

        if option == "Reparación":
            self.presupuesto_repa()

        return

    def presupuesto_piscina(self):

        self.presupuesto_frame_1.grid(row=0, column=1, sticky="news")

        self.presupuesto_frame_large_image_label = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="Presupuestos",
            font=ct.CTkFont(size=30, weight="bold"),
            image=self.images.large_test_image,
        )

        self.presupuesto_frame_large_image_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w"
        )

        # drop choice
        self.tipo_presupuesto = ct.CTkOptionMenu(
            self.presupuesto_frame_1,
            values=["Fuga Piscinas", "Todo Fugas", "Reparación", "Lámina Armada"],
            command=self.change_presupuesto,
        )
        self.tipo_presupuesto.grid(row=0, column=2, pady=30, sticky="sew")

        # Title
        self.presupuesto_frame_label_1 = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="Presupuesto Fuga Piscinas",
            font=ct.CTkFont(size=30, weight="bold"),
        )
        self.presupuesto_frame_label_1.grid(
            row=1, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # logo
        self.presupuesto_frame_label_0 = ct.CTkLabel(
            self.presupuesto_frame_1, text="", image=self.images.piscina_image
        )
        self.presupuesto_frame_label_0.grid(
            row=1, column=2, rowspan=4, padx=20, pady=20
        )

        # field 1
        self.presupuesto_frame_label_2 = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="Nombre Cliente:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_2.grid(
            row=2, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_1 = ct.CTkEntry(
            self.presupuesto_frame_1, placeholder_text="José Antonio"
        )
        self.presupuesto_frame_entry_1.grid(
            row=2, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 2
        self.presupuesto_frame_label_3 = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="Largo:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_3.grid(
            row=3, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_2 = ct.CTkEntry(
            self.presupuesto_frame_1, placeholder_text="8"
        )
        self.presupuesto_frame_entry_2.grid(
            row=3, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 3
        self.presupuesto_frame_label_4 = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="Ancho:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_4.grid(
            row=4, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_3 = ct.CTkEntry(
            self.presupuesto_frame_1, placeholder_text="4"
        )
        self.presupuesto_frame_entry_3.grid(
            row=4, column=1, padx=45, pady=10, sticky="ew"
        )

        # check 1
        self.presupuesto_frame_label_5 = ct.CTkCheckBox(
            self.presupuesto_frame_1, text="Skimmer", onvalue=True, offvalue=False
        )
        self.presupuesto_frame_label_5.grid(
            row=5, column=0, padx=45, pady=10, sticky="w"
        )

        # check 2
        self.presupuesto_frame_label_6 = ct.CTkCheckBox(
            self.presupuesto_frame_1, text="Jacuzzi", onvalue=True, offvalue=False
        )
        self.presupuesto_frame_label_6.grid(
            row=6, column=0, padx=45, pady=10, sticky="w"
        )

        # field 4
        self.presupuesto_frame_label_7 = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="Ingrese Distancia en Km:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_7.grid(
            row=7, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_4 = ct.CTkEntry(
            self.presupuesto_frame_1, placeholder_text="30"
        )
        self.presupuesto_frame_entry_4.grid(
            row=7, column=1, padx=45, pady=10, sticky="ew"
        )

        # button
        self.presupuesto_frame_button_1 = ct.CTkButton(
            self.presupuesto_frame_1,
            text="Crear",
            image=self.images.chat_image,
            compound="left",
            command=self.create_presupuesto_piscina,
        )
        self.presupuesto_frame_button_1.grid(
            row=8, column=1, padx=45, pady=10, sticky="ew"
        )

        # hidden
        self.presupuesto_frame_label_100 = ct.CTkLabel(
            self.presupuesto_frame_1,
            text="",
            text_color="red",
            font=ct.CTkFont(size=15, weight="bold"),
        )

        self.presupuesto_frame_label_100.grid(
            row=8, column=0, padx=45, pady=10, sticky="w"
        )

        return

    def presupuesto_fuga(self):

        self.presupuesto_frame_2.grid(row=0, column=1, sticky="news")

        self.presupuesto_frame_large_image_label = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="Presupuestos",
            font=ct.CTkFont(size=30, weight="bold"),
            image=self.images.large_test_image,
        )
        self.presupuesto_frame_large_image_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w"
        )

        # drop choice
        self.tipo_presupuesto = ct.CTkOptionMenu(
            self.presupuesto_frame_2,
            values=["Todo Fugas", "Fuga Piscinas", "Reparación", "Lámina Armada"],
            command=self.change_presupuesto,
        )
        self.tipo_presupuesto.grid(row=0, column=2, pady=30, sticky="sew")

        # Title
        self.presupuesto_frame_label_1 = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="Presupuesto Todo Fugas",
            font=ct.CTkFont(size=30, weight="bold"),
        )
        self.presupuesto_frame_label_1.grid(
            row=1, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # logo
        self.presupuesto_frame_label_0 = ct.CTkLabel(
            self.presupuesto_frame_2, text="", image=self.images.fuga_image
        )
        self.presupuesto_frame_label_0.grid(
            row=1, column=2, rowspan=4, padx=20, pady=20
        )

        # field 1
        # Ver como hago que el cliente que se busca siempre exista
        # o dar resultados similares

        self.presupuesto_frame_label_2 = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="Nombre Cliente:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_2.grid(
            row=2, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_1 = ct.CTkEntry(
            self.presupuesto_frame_2, placeholder_text="José Antonio"
        )
        self.presupuesto_frame_entry_1.grid(
            row=2, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 2
        self.presupuesto_frame_label_3 = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="Superficie:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_3.grid(
            row=3, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_2 = ct.CTkEntry(
            self.presupuesto_frame_2, placeholder_text="Valor defecto 90m2"
        )
        self.presupuesto_frame_entry_2.grid(
            row=3, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 3
        self.presupuesto_frame_label_4 = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="Distancia:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_4.grid(
            row=4, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_3 = ct.CTkEntry(
            self.presupuesto_frame_2, placeholder_text="en Km"
        )
        self.presupuesto_frame_entry_3.grid(
            row=4, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 4
        self.presupuesto_frame_label_7 = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="Tipo de Tubería",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_7.grid(
            row=5, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_4 = ct.CTkOptionMenu(
            self.presupuesto_frame_2, values=["Doméstica", "Urbanización", "Comercial"]
        )
        self.presupuesto_frame_entry_4.grid(
            row=5, column=1, padx=45, pady=10, sticky="w"
        )

        # button
        self.presupuesto_frame_button_1 = ct.CTkButton(
            self.presupuesto_frame_2,
            text="Crear",
            image=self.images.chat_image,
            compound="left",
            command=self.create_presupuesto_fuga,
        )
        self.presupuesto_frame_button_1.grid(
            row=6, column=1, padx=45, pady=10, sticky="ew"
        )

        # hidden
        self.presupuesto_frame_label_100 = ct.CTkLabel(
            self.presupuesto_frame_2,
            text="",
            text_color="red",
            font=ct.CTkFont(size=15, weight="bold"),
        )

        self.presupuesto_frame_label_100.grid(
            row=6, column=0, padx=45, pady=10, sticky="w"
        )

        return

    def presupuesto_repa(self):

        self.presupuesto_frame_3.grid(row=0, column=1, sticky="news")

        self.presupuesto_frame_large_image_label = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Presupuestos",
            font=ct.CTkFont(size=30, weight="bold"),
            image=self.images.large_test_image,
        )
        self.presupuesto_frame_large_image_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w"
        )

        # drop choice
        self.tipo_presupuesto = ct.CTkOptionMenu(
            self.presupuesto_frame_3,
            values=["Reparación", "Todo Fugas", "Fuga Piscinas", "Lámina Armada"],
            command=self.change_presupuesto,
        )
        self.tipo_presupuesto.grid(row=0, column=2, pady=30, sticky="sew")

        # Title
        self.presupuesto_frame_label_1 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Presupuesto Reparación",
            font=ct.CTkFont(size=30, weight="bold"),
        )
        self.presupuesto_frame_label_1.grid(
            row=1, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # logo
        self.presupuesto_frame_label_0 = ct.CTkLabel(
            self.presupuesto_frame_3, text="", image=self.images.midas_image
        )
        self.presupuesto_frame_label_0.grid(
            row=1, column=2, rowspan=4, padx=20, pady=20
        )

        # field 1

        self.presupuesto_frame_label_2 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Nombre Cliente:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_2.grid(
            row=2, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_1 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="José Antonio"
        )
        self.presupuesto_frame_entry_1.grid(
            row=2, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 2
        self.presupuesto_frame_label_3 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Concepto 1:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_3.grid(
            row=3, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_2 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="Reparación tubería"
        )
        self.presupuesto_frame_entry_2.grid(
            row=3, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 3
        self.presupuesto_frame_label_4 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Precio 1:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_4.grid(
            row=4, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_3 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="sin simbolo €"
        )
        self.presupuesto_frame_entry_3.grid(
            row=4, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 4
        self.presupuesto_frame_label_5 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Concepto 2:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_5.grid(
            row=5, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_4 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="Reparación gresite"
        )
        self.presupuesto_frame_entry_4.grid(
            row=5, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 5
        self.presupuesto_frame_label_6 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Precio 2:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_6.grid(
            row=6, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_5 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="sin simbolo €"
        )
        self.presupuesto_frame_entry_5.grid(
            row=6, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 6
        self.presupuesto_frame_label_7 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Concepto 3:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_7.grid(
            row=7, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_6 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="Mano de Obra"
        )
        self.presupuesto_frame_entry_6.grid(
            row=7, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 7
        self.presupuesto_frame_label_8 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Precio 3:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_8.grid(
            row=8, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_7 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="sin simbolo €"
        )
        self.presupuesto_frame_entry_7.grid(
            row=8, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 8
        self.presupuesto_frame_label_9 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Concepto 4:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_9.grid(
            row=9, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_8 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="Lechado"
        )
        self.presupuesto_frame_entry_8.grid(
            row=9, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 9
        self.presupuesto_frame_label_10 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="Precio 4:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_10.grid(
            row=10, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_9 = ct.CTkEntry(
            self.presupuesto_frame_3, placeholder_text="sin simbolo €"
        )
        self.presupuesto_frame_entry_9.grid(
            row=10, column=1, padx=45, pady=10, sticky="ew"
        )

        # button
        self.presupuesto_frame_button_1 = ct.CTkButton(
            self.presupuesto_frame_3,
            text="Crear",
            image=self.images.chat_image,
            compound="left",
            command=self.create_presupuesto_repa,
        )
        self.presupuesto_frame_button_1.grid(
            row=11, column=1, padx=45, pady=10, sticky="ew"
        )

        # hidden
        self.presupuesto_frame_label_100 = ct.CTkLabel(
            self.presupuesto_frame_3,
            text="",
            text_color="red",
            font=ct.CTkFont(size=15, weight="bold"),
        )

        self.presupuesto_frame_label_100.grid(
            row=11, column=0, padx=45, pady=10, sticky="w"
        )

        return

    def presupuesto_lamina(self):

        self.presupuesto_frame_4.grid(row=0, column=1, sticky="news")

        self.presupuesto_frame_large_image_label = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Presupuestos",
            font=ct.CTkFont(size=30, weight="bold"),
            image=self.images.large_test_image,
        )
        self.presupuesto_frame_large_image_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w"
        )

        # drop choice
        self.tipo_presupuesto = ct.CTkOptionMenu(
            self.presupuesto_frame_4,
            values=["Lámina Armada", "Reparación", "Todo Fugas", "Fuga Piscinas"],
            command=self.change_presupuesto,
        )
        self.tipo_presupuesto.grid(row=0, column=2, pady=30, sticky="sew")

        # Title
        self.presupuesto_frame_label_1 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Presupuesto Lámina Armada",
            font=ct.CTkFont(size=30, weight="bold"),
        )
        self.presupuesto_frame_label_1.grid(
            row=1, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # logo
        self.presupuesto_frame_label_0 = ct.CTkLabel(
            self.presupuesto_frame_4, text="", image=self.images.midas_image
        )
        self.presupuesto_frame_label_0.grid(
            row=1, column=2, rowspan=4, columnspan=2, padx=20, pady=20
        )

        # field 1
        # Ver como hago que el cliente que se busca siempre exista
        # o dar resultados similares

        self.presupuesto_frame_label_2 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Nombre Cliente:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_2.grid(
            row=2, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_1 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="José Antonio"
        )
        self.presupuesto_frame_entry_1.grid(
            row=2, column=1, padx=45, pady=10, sticky="ew"
        )

        # Title-1
        self.presupuesto_frame_label_15 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Primera Partida",
            font=ct.CTkFont(size=20, weight="bold"),
        )
        self.presupuesto_frame_label_15.grid(
            row=3, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # field 2
        self.presupuesto_frame_label_3 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Metros:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_3.grid(
            row=4, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_2 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="Ingrese en m2"
        )
        self.presupuesto_frame_entry_2.grid(
            row=4, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 3
        self.presupuesto_frame_label_4 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Tarifa:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_4.grid(
            row=5, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_3 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="Valor defecto 75€"
        )
        self.presupuesto_frame_entry_3.grid(
            row=5, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 4
        self.presupuesto_frame_label_5 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Modelo:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_5.grid(
            row=6, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_4 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text='Valor defecto "A Definir"'
        )
        self.presupuesto_frame_entry_4.grid(
            row=6, column=1, padx=45, pady=10, sticky="ew"
        )

        # Title-2
        self.presupuesto_frame_label_25 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Segunda Partida",
            font=ct.CTkFont(size=20, weight="bold"),
        )
        self.presupuesto_frame_label_25.grid(
            row=7, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # field 5
        self.presupuesto_frame_label_6 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Impulsiones:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_6.grid(
            row=8, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_5 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="1"
        )
        self.presupuesto_frame_entry_5.grid(
            row=8, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 6
        self.presupuesto_frame_label_7 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Barrefondos:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_7.grid(
            row=8, column=2, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_6 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="1"
        )
        self.presupuesto_frame_entry_6.grid(
            row=8, column=3, padx=45, pady=10, sticky="ew"
        )

        # field 7
        self.presupuesto_frame_label_8 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Skimmers:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_8.grid(
            row=9, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_7 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="2"
        )
        self.presupuesto_frame_entry_7.grid(
            row=9, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 8
        self.presupuesto_frame_label_9 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Focos + Nicho:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_9.grid(
            row=9, column=2, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_8 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="1"
        )
        self.presupuesto_frame_entry_8.grid(
            row=9, column=3, padx=45, pady=10, sticky="ew"
        )

        # field 9
        self.presupuesto_frame_label_10 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Sumidero:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_10.grid(
            row=10, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_9 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="1"
        )
        self.presupuesto_frame_entry_9.grid(
            row=10, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 10
        self.presupuesto_frame_label_11 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Sumidero Grande:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_11.grid(
            row=10, column=2, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_10 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="0"
        )
        self.presupuesto_frame_entry_10.grid(
            row=10, column=3, padx=45, pady=10, sticky="ew"
        )

        # Title-3
        self.presupuesto_frame_label_35 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Tercera Partida",
            font=ct.CTkFont(size=20, weight="bold"),
        )
        self.presupuesto_frame_label_35.grid(
            row=11, column=0, padx=45, pady=10, columnspan=2, sticky="w"
        )

        # field 11
        self.presupuesto_frame_label_12 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Concepto:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_12.grid(
            row=12, column=0, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_11 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="Escalera de Obra"
        )
        self.presupuesto_frame_entry_11.grid(
            row=12, column=1, padx=45, pady=10, sticky="ew"
        )

        # field 12
        self.presupuesto_frame_label_13 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="Precio:",
            font=ct.CTkFont(size=15, weight="bold"),
        )
        self.presupuesto_frame_label_13.grid(
            row=12, column=2, padx=45, pady=10, sticky="w"
        )
        self.presupuesto_frame_entry_12 = ct.CTkEntry(
            self.presupuesto_frame_4, placeholder_text="sin simbolo €"
        )
        self.presupuesto_frame_entry_12.grid(
            row=12, column=3, padx=45, pady=10, sticky="ew"
        )

        # button
        self.presupuesto_frame_button_1 = ct.CTkButton(
            self.presupuesto_frame_4,
            text="Crear",
            image=self.images.chat_image,
            compound="left",
            command=self.create_presupuesto_lamina,
        )
        self.presupuesto_frame_button_1.grid(
            row=13, column=3, padx=45, pady=10, sticky="ew"
        )

        # hidden
        self.presupuesto_frame_label_100 = ct.CTkLabel(
            self.presupuesto_frame_4,
            text="",
            text_color="red",
            font=ct.CTkFont(size=15, weight="bold"),
        )

        self.presupuesto_frame_label_100.grid(
            row=13, column=2, padx=45, pady=10, sticky="w"
        )

        return
