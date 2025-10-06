import customtkinter as ct
import os
from PIL import Image


class Images:

    def __init__(self):

        # load images with light and dark mode image
        self.image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "Gui", "test_images"
        )

        self.logo_image = ct.CTkImage(
            Image.open(os.path.join(self.image_path, "aqua.png")), size=(200, 200)
        )

        self.piscina_image = ct.CTkImage(
            Image.open(os.path.join(self.image_path, "piscina.png")), size=(190, 190)
        )

        self.fuga_image = ct.CTkImage(
            Image.open(os.path.join(self.image_path, "fuga.png")), size=(190, 190)
        )

        self.midas_image = ct.CTkImage(
            Image.open(os.path.join(self.image_path, "midas.png")), size=(190, 190)
        )

        self.large_test_image = ct.CTkImage(
            Image.open(os.path.join(self.image_path, "large_test_image2.png")),
            size=(500, 150),
        )

        self.image_icon_image = ct.CTkImage(
            Image.open(os.path.join(self.image_path, "image_icon_light.png")),
            size=(20, 20),
        )

        self.home_image = ct.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "home_dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "home_light.png")),
            size=(20, 20),
        )

        self.chat_image = ct.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "chat_dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "chat_light.png")),
            size=(20, 20),
        )

        self.add_user_image = ct.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "add_user_light.png")),
            size=(20, 20),
        )

        self.presupuesto_image = ct.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "file-pen-dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "file-pen-light.png")),
            size=(20, 20),
        )

        self.consultas_image = ct.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "search_dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "search_light.png")),
            size=(20, 20),
        )

        return
