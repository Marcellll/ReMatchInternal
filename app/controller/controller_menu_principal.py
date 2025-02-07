import tkinter as tk
from app.views.view_production import Production
from app.views.view_batch import Batch
from app.views.view_settings import Settings
from enum import Enum

class MenuButton(Enum):
    PRODUCTION = 1
    BATCH = 2
    SETTINGS = 3


class ControllerMenuPrincipal:
    def __init__(self, view):
        self.view = view

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
            case MenuButton.BATCH:
                Batch(mainWidget)
            case MenuButton.SETTINGS:
                Settings(mainWidget)
