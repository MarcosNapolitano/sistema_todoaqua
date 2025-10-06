import customtkinter as ct

class Side_Frame():

   def __init__(self, App, images):

       # create navigation frame
       self.navigation_frame = ct.CTkFrame(App, corner_radius=0)
       self.navigation_frame.grid(row=0, column=0, sticky="nsew")
       self.navigation_frame.grid_rowconfigure(5, weight=1)


       # title and logo
       self.navigation_frame_label = ct.CTkLabel(self.navigation_frame, 
              text="Sistema de Gestión Todo Aqua", 
              image=images.logo_image, 
              compound="top", 
              font=ct.CTkFont(size=15, weight="bold"))

       self.navigation_frame_label.grid(row=0, column=0, 
                                        padx=20, pady=20)

       # first panel
       self.alta_cliente = ct.CTkButton(self.navigation_frame,
              corner_radius=0, 
              height=40, 
              border_spacing=10, 
              text="Clientes y Llamadas",
              fg_color="transparent", 
              text_color=("gray10", "gray90"), 
              hover_color=("gray70", "gray30"), 
              image=images.add_user_image, 
              anchor="w", 
              command=App.alta_cliente_event)

       self.alta_cliente.grid(row=1, column=0, sticky="ew")
 
       # second panel
       self.presupuesto = ct.CTkButton(self.navigation_frame, 
              corner_radius=0,
              height=40, 
              border_spacing=10, 
              text="Presupuestos", 
              fg_color="transparent", 
              text_color=("gray10", "gray90"), 
              hover_color=("gray70", "gray30"), 
              image=images.presupuesto_image, 
              anchor="w", 
              command=App.presupuesto_event)
 
       self.presupuesto.grid(row=2, column=0, sticky="ew")

       # # third panel
       # self.actuaciones = ct.CTkButton(self.navigation_frame, corner_radius=0, 
       #        height=40, 
       #        border_spacing=10, 
       #        text="Actuaciones",
       #        fg_color="transparent", 
       #        text_color=("gray10", "gray90"), 
       #        hover_color=("gray70", "gray30"),
       #        image=images.home_image, 
       #        anchor="w", 
       #        command=App.actuaciones_event)
       #
       # self.actuaciones.grid(row=3, column=0, sticky="new")

       # fourth panel
       self.consultas = ct.CTkButton(self.navigation_frame, 
              corner_radius=0, 
              height=40, 
              border_spacing=10, 
              text="Consultas",
              fg_color="transparent", 
              text_color=("gray10", "gray90"), 
              hover_color=("gray70", "gray30"),
              image=images.consultas_image, 
              anchor="w", 
              command=App.consultas_event)
 
       self.consultas.grid(row=4, column=0, sticky="new")

 
       # color mode
       self.appearance_mode_menu = ct.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                command=App.change_appearance_mode_event)
        
       self.appearance_mode_menu.grid(row=5, column=0, 
                                      padx=20, pady=20, sticky="s")

       return
