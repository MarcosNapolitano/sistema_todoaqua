import customtkinter as ct
from Models.Cliente import Cliente
from Models.Llamada import Llamada
from tkinter import messagebox


class User_Frame:

    def __init__(self, App, images):

        self.images = images

        # create user frame
        self.user_frame = ct.CTkFrame(App, corner_radius=0, fg_color="transparent")

        self.user_frame.grid_columnconfigure(2, weight=1)

        # main image
        self.user_frame_large_image_label = ct.CTkLabel(
            self.user_frame,
            text="Clientes y Llamadas",
            font=ct.CTkFont(size=30, weight="bold"),
            image=self.images.large_test_image,
        )

        self.user_frame_large_image_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=10, sticky="w"
        )

        # drop choice
        self.tipo_usuario = ct.CTkOptionMenu(
            self.user_frame,
            values=["Alta Cliente", "Llamada General"],
            command=self.change_user_actions,
        )

        self.tipo_usuario.grid(row=0, column=2, pady=30, sticky="sw")

        self.user_frame_label_6 = ct.CTkLabel(
            self.user_frame,
            text="Alta Cliente:",
            font=ct.CTkFont(size=30, weight="bold"),
        )

        self.user_frame_label_6.grid(row=1, column=0, padx=45, pady=10, sticky="w")

        # field 1
        self.user_frame_label_1 = ct.CTkLabel(
            self.user_frame, text="Teléfono:", font=ct.CTkFont(size=15, weight="bold")
        )

        self.user_frame_label_1.grid(row=2, column=0, padx=45, pady=10, sticky="w")

        self.user_frame_entry_1 = ct.CTkEntry(
            self.user_frame, placeholder_text="Formato 649-320-241"
        )

        self.user_frame_entry_1.grid(row=2, column=1, padx=45, pady=10, sticky="ew")

        # field 2
        self.user_frame_label_2 = ct.CTkLabel(
            self.user_frame, text="Nombre:", font=ct.CTkFont(size=15, weight="bold")
        )

        self.user_frame_label_2.grid(row=3, column=0, padx=45, pady=10, sticky="w")

        self.user_frame_entry_2 = ct.CTkEntry(
            self.user_frame, placeholder_text="José Antonio Romero"
        )

        self.user_frame_entry_2.grid(row=3, column=1, padx=45, pady=10, sticky="ew")

        self.change_user_actions("Alta Cliente")

    def create_user(self):

        numero = int(self.user_frame_entry_1.get())
        nombre = self.user_frame_entry_2.get()
        direccion = self.user_frame_entry_3.get()
        localidad = self.user_frame_entry_4.get()
        provincia = self.user_frame_entry_5.get()

        if (
            not numero
            or nombre == ""
            or direccion == ""
            or localidad == ""
            or provincia == ""
        ):

            self.user_frame_label_100.configure(text="Faltan Datos.")
            return

        self.user_frame_label_100.configure(text="")

        cliente = Cliente()
        cliente.create_client(numero, nombre, direccion, localidad, provincia)

        self.user_frame_entry_1.delete(0, "end")
        self.user_frame_entry_2.delete(0, "end")
        self.user_frame_entry_3.delete(0, "end")
        self.user_frame_entry_4.delete(0, "end")
        self.user_frame_entry_5.delete(0, "end")

        return

    def create_llamada(self):

        numero = self.user_frame_entry_1.get()
        nombre = self.user_frame_entry_2.get()
        motivo = self.user_frame_entry_3.get()

        if numero == "" or nombre == "" or motivo == "":

            self.user_frame_label_100.configure(text="Faltan Datos.")
            return

        self.user_frame_label_100.configure(text="")

        try:

            llamada = Llamada(numero, nombre, motivo)

            llamada.save_client()

            messagebox.showinfo(
                title="Sistema de Gestión Todo Aqua",
                message="Llamada correctamente creada.",
            )

        except:

            messagebox.showerror(
                title="Sistema de Gestión Todo Aqua",
                message="Error al crear llamada. Contacte al administrador.",
            )
            return

        self.user_frame_entry_1.delete(0, "end")
        self.user_frame_entry_2.delete(0, "end")
        self.user_frame_entry_3.delete(0, "end")

        return

    # user choice
    def change_user_actions(self, option):

        self.user_frame_label_6.configure(text=option)

        if option == "Llamada General":

            self.user_frame_label_3.grid_forget()
            self.user_frame_entry_3.grid_forget()

            self.user_frame_label_4.grid_forget()
            self.user_frame_entry_4.grid_forget()

            self.user_frame_label_5.grid_forget()
            self.user_frame_entry_5.grid_forget()

            self.user_frame_button_1.grid_forget()

            # field 3
            self.user_frame_label_3 = ct.CTkLabel(
                self.user_frame, text="Motivo:", font=ct.CTkFont(size=15, weight="bold")
            )

            self.user_frame_label_3.grid(row=4, column=0, padx=45, pady=10, sticky="w")

            self.user_frame_entry_3 = ct.CTkEntry(
                self.user_frame, placeholder_text="Ingrese motivo general"
            )

            self.user_frame_entry_3.grid(row=4, column=1, padx=45, pady=10, sticky="ew")

            self.user_frame_button_1 = ct.CTkButton(
                self.user_frame,
                text="Crear",
                image=self.images.add_user_image,
                compound="left",
                command=self.create_llamada,
            )

            self.user_frame_button_1.grid(
                row=5, column=1, padx=45, pady=10, sticky="ew"
            )

            # hidden
            self.user_frame_label_100 = ct.CTkLabel(
                self.user_frame,
                text="",
                text_color="red",
                font=ct.CTkFont(size=15, weight="bold"),
            )

            self.user_frame_label_100.grid(
                row=5, column=0, padx=45, pady=10, sticky="w"
            )

        else:
            # field 3
            self.user_frame_label_3 = ct.CTkLabel(
                self.user_frame,
                text="Dirección:",
                font=ct.CTkFont(size=15, weight="bold"),
            )

            self.user_frame_label_3.grid(row=4, column=0, padx=45, pady=10, sticky="w")

            self.user_frame_entry_3 = ct.CTkEntry(
                self.user_frame, placeholder_text="Av. Camas 10"
            )

            self.user_frame_entry_3.grid(row=4, column=1, padx=45, pady=10, sticky="ew")

            # field 4
            self.user_frame_label_4 = ct.CTkLabel(
                self.user_frame,
                text="Localidad:",
                font=ct.CTkFont(size=15, weight="bold"),
            )

            self.user_frame_label_4.grid(row=5, column=0, padx=45, pady=10, sticky="w")

            self.user_frame_entry_4 = ct.CTkEntry(
                self.user_frame, placeholder_text="Bollullos de la Mitación"
            )

            self.user_frame_entry_4.grid(row=5, column=1, padx=45, pady=10, sticky="ew")

            # field 5
            self.user_frame_label_5 = ct.CTkLabel(
                self.user_frame,
                text="Provincia:",
                font=ct.CTkFont(size=15, weight="bold"),
            )

            self.user_frame_label_5.grid(row=6, column=0, padx=45, pady=10, sticky="w")

            self.user_frame_entry_5 = ct.CTkEntry(
                self.user_frame, placeholder_text="Sevilla"
            )

            self.user_frame_entry_5.grid(row=6, column=1, padx=45, pady=10, sticky="ew")

            self.user_frame_button_1 = ct.CTkButton(
                self.user_frame,
                text="Crear",
                image=self.images.add_user_image,
                compound="left",
                command=self.create_user,
            )

            self.user_frame_button_1.grid(
                row=7, column=1, padx=45, pady=10, sticky="ew"
            )

            # hidden
            self.user_frame_label_100 = ct.CTkLabel(
                self.user_frame,
                text="",
                text_color="red",
                font=ct.CTkFont(size=15, weight="bold"),
            )

            self.user_frame_label_100.grid(
                row=7, column=0, padx=45, pady=10, sticky="w"
            )

        return
