import tkinter as tk
from customtkinter import *
from app.controller.controller_chargement import ControllerChargement
from app.views.view_calendrier import ViewCalendrier
from utils import settings

class NouvelleReception:

    def check_input(self, var, index, mode):
        try:
            self.nombre_camion.get()
        except:
            self.nombre_camion.set(0)

    def __init__(self, lot:str):
        nouveau_lot = CTkToplevel()
        nouveau_lot.title("Nouveau chargement")
        nouveau_lot.resizable(False, False)
        nouveau_lot.geometry(f"600x250")
        nouveau_lot.attributes("-topmost", True)

        button_width = 50
        button_height = 50
        numero_chargement = tk.StringVar(value=ControllerChargement.get_new_chargement())
        date_debut = tk.StringVar()
        date_fin = tk.StringVar()
        self.nombre_camion = tk.IntVar()

        #Chargement
        nouveau_chargement_label = CTkLabel(nouveau_lot, text="Chargement :",  padx=1, pady=1)
        nouveau_chargement_label.grid(row=0,column=0, sticky="w")
        nouveau_chargement_entry = CTkEntry(nouveau_lot, width= 250, textvariable=numero_chargement, state=tk.DISABLED)
        nouveau_chargement_entry.grid(row=0,column=1, sticky="w")
        #Date début
        date_debut_label = CTkLabel(nouveau_lot, text="Date début :",  padx=1, pady=1)
        date_debut_label.grid(row=1,column=0, sticky='w')
        date_debut_entry = CTkEntry(nouveau_lot, textvariable=date_debut, width=250)
        date_debut_entry.grid(row=1,column=1)
        date_debut_picker = CTkButton(nouveau_lot, text= "",
                                                 width=button_width, height=button_height,
                                                 image=settings.resize_image("static\\date.png", button_width, button_height),
                                                 command= lambda:ViewCalendrier(date_debut))
        date_debut_picker.grid(row=1, column=2)
        #Date fin
        date_fin_label = CTkLabel(nouveau_lot, text="Date fin :",  padx=1, pady=1)
        date_fin_label.grid(row=2,column=0, sticky='w')
        date_fin_entry = CTkEntry(nouveau_lot, textvariable=date_fin, width=250)
        date_fin_entry.grid(row=2,column=1)
        date_fin_picker = CTkButton(nouveau_lot, text= "",
                                                 width=button_width, height=button_height,
                                                 image=settings.resize_image("static\\date.png", button_width, button_height),
                                                 command= lambda:ViewCalendrier(date_fin))
        date_fin_picker.grid(row=2, column=2)
        #Nombre camion
        nombre_camion_label = CTkLabel(nouveau_lot, text="Nbr camion :",  padx=1, pady=1)
        nombre_camion_label.grid(row=3,column=0, sticky="w")
        nombre_camion_entry = CTkEntry(nouveau_lot, width= 250, textvariable=self.nombre_camion)
        nombre_camion_entry.grid(row=3,column=1, sticky="w")
        #Add the save button
        nouveau_chargement_save_button = CTkButton(nouveau_lot, text="Valider", width=150, 
                                                   image=settings.resize_image("static\\sauvegarder.png", button_width, button_height),
                                                   command=lambda:[ControllerChargement.create_new_chargement(numero_chargement=numero_chargement.get(),
                                                                                                              date_debut=date_debut.get(),
                                                                                                              date_fin=date_fin.get(),
                                                                                                              nombre_camion=self.nombre_camion.get(),
                                                                                                              lot=lot,
                                                                                                              window=nouveau_lot)]
                                                   )
        nouveau_chargement_save_button.grid(row=4, column=1, sticky="NSEW", ipadx = 10, ipady= 10)

        trace_id = self.nombre_camion.trace_add(['write'], self.check_input)