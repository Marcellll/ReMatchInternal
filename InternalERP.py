from app.views.view_menu_principal import MenuPrincipal
import logging
import tkinter as tk
from datetime import datetime
from utils import updater
import customtkinter as ctk
from os import path
import utils.settings as settings

if __name__ == "__main__":
    settings.global_init(path.dirname(__file__))
    logging.basicConfig(filename="logs.log", level=logging.INFO)
    updater.logger.info(f"Started application at {datetime.now()}")
    #updater.check_for_update()
    ctk.set_default_color_theme(path.abspath(path.join(settings.path_name, 'static\\rematch_theme.json')))                          
    ctk.set_appearance_mode("dark")
    root = MenuPrincipal()
    root.mainloop()