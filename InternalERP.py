from app.views.view_menu_principal import MenuPrincipal
import logging
import tkinter as tk
from datetime import datetime
from utils import updater

if __name__ == "__main__":
    logging.basicConfig(filename="logs.log", level=logging.INFO)
    updater.logger.info(f"Started application at {datetime.utcnow()}")
    #updater.check_for_update()
    root = MenuPrincipal()
    root.mainloop()