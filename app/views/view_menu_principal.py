import tkinter as tk
from tkinter import ttk
from app.controller.controller_menu_principal import ControllerMenuPrincipal, MenuButton
from app.views.view_production_planification import Batch
from app.views.view_production import Production
import customtkinter as ctk

class MenuPrincipal(ctk.CTk):
    def __init__(self, version: str):
        super().__init__()
        self.title(f"Re-Match ERP - {version}")
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
        outer_frame = tk.Frame(self, bg="#242424", width=self.winfo_screenwidth()*1.2, height=self.winfo_screenheight()*1.4)
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
        #Pesee sub section
        planificationButton = ctk.CTkButton(prodSubSection, text="Pesee", height=100, width=200 ,
                                        command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.PESEE))
        planificationButton.grid(row=1, column=0)

        #Logistics Button
        logisticsButton = ctk.CTkButton(sidebar, text="Logistique", height= 100, 
                                   command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.LOGISTIQUE, logisticsSubSection))
        logisticsButton.grid(row=2, column=0, sticky='ew')
        logisticsSubSection = ctk.CTkFrame(sidebar)    
        #Sub section for Logistics to encapsulate the sub menu buttons
        logisticsSubSection.grid(row=3, column=0, sticky='ew')
        logisticsSubSection.columnconfigure(0, weight=1)
        logisticsSubSection.grid_remove()
        #Pesee sub section
        camionButton = ctk.CTkButton(logisticsSubSection, text="Camion", height=100, width=200 ,
                                        command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.CAMION))
        camionButton.grid(row=0, column=0)

        #Quality Button
        qualityButton = ctk.CTkButton(sidebar, text="Qualité", height= 100, 
                                     command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.QUALITY, qualitySubSection))
        qualityButton.grid(row=4, column=0, sticky='ew')
        #Sub section for Quality to encapsulate the sub menu buttons
        qualitySubSection = ctk.CTkFrame(sidebar) 
        qualitySubSection.grid(row=5, column=0, sticky='ew')
        qualitySubSection.columnconfigure(0, weight=1)
        qualitySubSection.grid_remove()
        #Batch sub section
        batchButton = ctk.CTkButton(qualitySubSection, text="Lot", height=100, width=200 ,
                                        command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.LOT))
        batchButton.grid(row=0, column=0)

        #Settings button
        settingsButton = ctk.CTkButton(sidebar, text="Paramètres", height= 100, 
                                     command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.SETTINGS, settingsSubSection))
        settingsButton.grid(row=6, column=0, sticky='ew')
        #Sub section for Settings to encapsulate the sub menu buttons
        settingsSubSection = ctk.CTkFrame(sidebar) 
        settingsSubSection.grid(row=7, column=0, sticky='ew')
        settingsSubSection.columnconfigure(0, weight=1)
        settingsSubSection.grid_remove()
        #Batch sub section
        nomenclatureButton = ctk.CTkButton(settingsSubSection, text="Nomenclature", height=100, width=200 ,
                                        command= lambda : controller.create_new_view(outer_frame, sidebar, MenuButton.NOMENCLATURE))
        nomenclatureButton.grid(row=0, column=0)

        #Initializes the production view
        Production(outer_frame)

