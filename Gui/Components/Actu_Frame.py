import customtkinter as ct


class Actu_Frame:

    def __init__(self, App, images):

        self.images = images
        # create consultas frame
        self.actuaciones_frame = ct.CTkFrame(
            App, corner_radius=0, fg_color="transparent"
        )

        self.actuaciones_frame_button_1 = ct.CTkButton(
            self.actuaciones_frame, text="", image=self.images.image_icon_image
        )
        self.actuaciones_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.actuaciones_frame_button_2 = ct.CTkButton(
            self.actuaciones_frame,
            text="CTkButton",
            image=self.images.image_icon_image,
            compound="right",
        )
        self.actuaciones_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.actuaciones_frame_button_3 = ct.CTkButton(
            self.actuaciones_frame,
            text="CTkButton",
            image=self.images.image_icon_image,
            compound="top",
        )
        self.actuaciones_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.actuaciones_frame_button_4 = ct.CTkButton(
            self.actuaciones_frame,
            text="CTkButton",
            image=self.images.image_icon_image,
            compound="bottom",
            anchor="w",
        )
        self.actuaciones_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        return
