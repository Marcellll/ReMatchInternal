import tkinter as tk
from tkinter import ttk
from app.controller.controller_menu_principal import ControllerMenuPrincipal, MenuButton
from app.views.view_production_planification import Batch
from app.views.view_production import Production
import customtkinter as ctk

class MenuPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Re-Match ERP")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.state("withdrawn")
        controller = ControllerMenuPrincipal(self)

        # Inner frame on the left, taking 20% of the screen on the left
        sidebar = ctk.CTkFrame(self, width = self.winfo_screenwidth()*0.2, height=self.winfo_screenheight())
        sidebar.pack(side="left")  # Fill whole height on the left
        sidebar.columnconfigure(0, weight=1)
        sidebar.grid_propagate(False)   #Restricts the buttons to not resize this frame
        sidebar.propagate(False)

        # Outer frame taking the whole space
        outer_frame = tk.Frame(self, bg="#242424", width=self.winfo_screenwidth()*1.1, height=self.winfo_screenheight()*1.2)
        outer_frame.pack(side="right", expand=True)
        outer_frame.columnconfigure(0, weight=1)
        outer_frame.grid_propagate(False)
        outer_frame.propagate(False)
        

        #Production Button
        prodButton = ctk.CTkButton(sidebar, text="Production", height= 100, 
                                   command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.PRODUCTION, prodSubSection))
        prodButton.grid(row=0, column=0, sticky='ew')
        prodSubSection = ctk.CTkFrame(sidebar)    
        #Sub section for Production to encapsulate the sub menu buttons
        prodSubSection.grid(row=1, column=0, sticky='ew')
        prodSubSection.columnconfigure(0, weight=1)
        prodSubSection.grid_remove()
        #Planification sub section
        planificationButton = ctk.CTkButton(prodSubSection, text="Planification", height=100, width=200 ,
                                        command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.PLANIFICATION))
        planificationButton.grid(row=0, column=0)

        #Quality Button
        qualityButton = ctk.CTkButton(sidebar, text="Qualité", height= 100, 
                                     command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.QUALITY, qualitySubSection))
        qualityButton.grid(row=2, column=0, sticky='ew')
        #Sub section for Quality to encapsulate the sub menu buttons
        qualitySubSection = ctk.CTkFrame(sidebar) 
        qualitySubSection.grid(row=3, column=0, sticky='ew')
        qualitySubSection.columnconfigure(0, weight=1)
        qualitySubSection.grid_remove()
        #Batch sub section
        batchButton = ctk.CTkButton(qualitySubSection, text="Lot", height=100, width=200 ,
                                        command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.LOT))
        batchButton.grid(row=0, column=0, )

        #Settings button
        settingsButton = ctk.CTkButton(sidebar, text="Paramètres", height= 100, 
                                     command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.SETTINGS))
        settingsButton.grid(row=4, column=0, sticky='ew')

        #Initializes the production view
        Production(outer_frame)

