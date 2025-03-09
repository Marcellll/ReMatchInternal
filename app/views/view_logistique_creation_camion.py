import tkinter as tk
from customtkinter import *
from app.controller.controller_chargement import ControllerChargement

class LogistiqueCamion:

    def __init__(self, chargement:int):
        new_camion = CTkToplevel()
        new_camion.title("Ajouter un camion")
        new_camion.resizable(False, False)
        new_camion.geometry(f"500x150")
        new_camion.attributes("-topmost", True)

        self.chargement = tk.IntVar(value=chargement)
        self.description = tk.StringVar()

        #Chargement
        chargement_label = CTkLabel(new_camion, text="Num chargement :",  padx=1, pady=1)
        chargement_label.grid(row=0,column=0, sticky="w")
        chargement_entry = CTkEntry(new_camion, width= 250, textvariable=self.chargement, state=tk.DISABLED)
        chargement_entry.grid(row=0,column=1, sticky="w")
        #Description
        description_label = CTkLabel(new_camion, text="Description :",  padx=1, pady=1)
        description_label.grid(row=1,column=0, sticky="w")
        description_entry = CTkEntry(new_camion, width= 250, textvariable=self.description)
        description_entry.grid(row=1,column=1, sticky="w")
        #Add the save button
        nouveau_lot_save_button = CTkButton(new_camion, text="Valider", width=150,
                                            command= lambda:[ControllerChargement.create_new_camion(self.chargement.get(),
                                                                                                    self.description.get()),
                                                             new_camion.destroy()])
        nouveau_lot_save_button.grid(row=3, column=1, sticky="NSEW", ipadx = 10, ipady= 10)