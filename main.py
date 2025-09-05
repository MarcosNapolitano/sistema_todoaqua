import customtkinter as ct
from images import Images
from Gui.Components.Side_Frame import Side_Frame
from Gui.Components.User_Frame import User_Frame
from Gui.Components.Pres_Frame import Pres_Frame
from Gui.Components.Actu_Frame import Actu_Frame
from Gui.Components.Cons_Frame import Cons_Frame
import os


class App(ct.CTk):
    def __init__(self):
        super().__init__()

        # basic config
        self.title("Gestión Todo Aqua")
        self.geometry("1920x1080")
        self.resizable(True, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # inits
        self.images = Images()
        self.side_frame = Side_Frame(self, self.images)
        self.user_frame = User_Frame(self, self.images)
        self.pres_frame = Pres_Frame(self, self.images)
        self.actu_frame = Actu_Frame(self, self.images)
        self.cons_frame = Cons_Frame(self, self.images)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):

        # show selected frame
        if name == "home":
            self.user_frame.user_frame.grid(row=0, column=1, sticky="nsew")
            self.side_frame.alta_cliente.configure(fg_color=("gray75", "gray25"))
        else:
            self.user_frame.user_frame.grid_forget()
            self.side_frame.alta_cliente.configure(fg_color="transparent")
        if name == "presupuestos":
            self.pres_frame.presupuesto_frame_1.grid(row=0, column=1, sticky="news")
            self.side_frame.presupuesto.configure(fg_color=("gray75", "gray25"))
        else:
            self.pres_frame.presupuesto_frame_1.grid_forget()
            self.pres_frame.presupuesto_frame_2.grid_forget()
            self.pres_frame.presupuesto_frame_3.grid_forget()
            self.pres_frame.presupuesto_frame_4.grid_forget()
            self.side_frame.presupuesto.configure(fg_color="transparent")
        if name == "actuaciones":
            self.actu_frame.actuaciones_frame.grid(row=0, column=1, sticky="nsew")
            self.side_frame.actuaciones.configure(fg_color=("gray75", "gray25"))
        else:
            self.actu_frame.actuaciones_frame.grid_forget()
            self.side_frame.actuaciones.configure(fg_color="transparent")
        if name == "consultas":
            self.cons_frame.consultas_frame.grid(row=0, column=1, sticky="nsew")
            self.cons_frame.tabview.delete("Clientes")
            self.cons_frame.tabview.delete("Presupuestos")
            self.cons_frame.consulta_cliente()
            self.cons_frame.consulta_presupuestos()
            self.side_frame.consultas.configure(fg_color=("gray75", "gray25"))
        else:
            self.cons_frame.consultas_frame.grid_forget()
            self.side_frame.consultas.configure(fg_color="transparent")

    def alta_cliente_event(self):
        self.select_frame_by_name("home")

    def presupuesto_event(self):
        self.select_frame_by_name("presupuestos")

    def actuaciones_event(self):
        self.select_frame_by_name("actuaciones")

    def consultas_event(self):
        self.select_frame_by_name("consultas")

    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
    app.iconbitmap(os.path.join(app.images.image_path, "aqua.ico"))
