import tkinter as tk
from tkinter import ttk
from app.controller.controller_menu_principal import ControllerMenuPrincipal, MenuButton
from app.views.view_batch import Batch
from app.views.view_production import Production

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Re-Match ERP")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.state("zoomed")
        controller = ControllerMenuPrincipal(self)

        # Outer frame taking the whole space
        outer_frame = tk.Frame(self, bg="lightblue", width = self.winfo_screenwidth()*0.8, height=self.winfo_screenheight())
        outer_frame.pack(side="right", expand=True)
        outer_frame.grid_propagate(False)
        outer_frame.propagate(False)

        # Inner frame on the left, taking 20% of the screen on the left
        sidebar = tk.Frame(self, bg="black", width = self.winfo_screenwidth()*0.2, height=self.winfo_screenheight())
        sidebar.pack(side="left")  # Fill whole height on the left
        sidebar.columnconfigure(0, weight=1)
        sidebar.grid_propagate(False)   #Restricts the buttons to not resize this frame
        sidebar.propagate(False)

        #Add Buttons to the buttonSidebar
        prodButton = tk.Button(sidebar, text="Production", height= 5, command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.PRODUCTION, prodSubSection))
        prodButton.grid(row=0, column=0, sticky='ew')
        prodSubSection = tk.Frame(sidebar)    #Sub section to encapsulate the sub menu buttons
        prodSubSection.grid(row=1, column=0, sticky='ew')
        prodSubSection.columnconfigure(0, weight=1)
        prodSubSection.grid_remove()
        prodFirstButton = tk.Button(prodSubSection, text="Batch", height=5, command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.BATCH))
        prodFirstButton.grid(row=0, column=0, sticky='ew')

        prodSettings = tk.Button(sidebar, text="Settings", height= 5, command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.SETTINGS))
        prodSettings.grid(row=2, column=0, sticky='ew')

        #Initializes the production view
        Production(outer_frame)

