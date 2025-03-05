import tkinter as tk
from app.views.view_production import Production
from app.views.view_production_planification import Batch
from app.views.view_quality import Quality
from app.views.view_quality_lot import Lot
from app.views.view_settings import Settings
from app.views.view_nomenclature import Nomenclature
from app.views.view_pesee import Pesee
from app.views.view_logistique import Logistique
from app.views.view_camion import Camion
from enum import Enum
from queue import Queue

class MenuButton(Enum):
    PRODUCTION = 1
    PLANIFICATION = 2
    PESEE = 3
    LOGISTIQUE = 4
    CAMION = 5
    QUALITY = 6
    LOT = 7
    SETTINGS = 8
    NOMENCLATURE = 9


class ControllerMenuPrincipal:
    def __init__(self, view):
        self.view = view
        self.data_queue = Queue()

    def hide_show_widget(self, widget: tk.Frame):
        if widget.winfo_ismapped():
            widget.grid_remove()
        else:
            widget.grid()

    def create_new_view(self, mainWidget: tk.Frame, sideBar: tk.Frame, menuButton: MenuButton, subMenu: tk.Frame = None):
        #Cleans all the widgets from the main Frame
        for widgets in mainWidget.winfo_children():
            widgets.destroy()

        #Instantiates the new class view for the frame based on the button enum
        match menuButton:
            case MenuButton.PRODUCTION:
                self.hide_show_widget(subMenu)
                Production(mainWidget)
            case MenuButton.PLANIFICATION:
                Batch(mainWidget)
            case MenuButton.PESEE:
                Pesee(mainWidget, self.data_queue)
            case MenuButton.LOGISTIQUE:
                self.hide_show_widget(subMenu)
                Logistique(mainWidget)
            case MenuButton.CAMION:
                Camion(mainWidget)
            case MenuButton.QUALITY:
                self.hide_show_widget(subMenu)
                Quality(mainWidget)
            case MenuButton.LOT:
                Lot(mainWidget)
            case MenuButton.SETTINGS:
                self.hide_show_widget(subMenu)
                Settings(mainWidget)
            case MenuButton.NOMENCLATURE:
                Nomenclature(mainWidget)
