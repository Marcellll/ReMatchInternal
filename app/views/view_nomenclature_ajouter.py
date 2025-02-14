import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import Image
from app.controller.controller_nomenclature import ControllerNomenclature

class NomenclatureNouveau:

    def __init__(self, type_terrain):
        button_width = 50
        button_height = 50
        nomenclature_nouveau = CTkToplevel()
        nomenclature_nouveau.title("Ajouter un article")
        nomenclature_nouveau.resizable(False, False)
        nomenclature_nouveau.geometry(f"500x150")
        nomenclature_nouveau.attributes("-topmost", True)

        self.type_terrain = tk.StringVar(value=type_terrain)
        self.article_to_add = tk.StringVar()

        #Article Front-end
        article_front_end_label = CTkLabel(nomenclature_nouveau, text="Type de terrain :",  padx=1, pady=1)
        article_front_end_label.grid(row=0,column=0, sticky="w")
        article_front_end_entry = CTkEntry(nomenclature_nouveau, width= 250, textvariable=self.type_terrain, state=tk.DISABLED)
        article_front_end_entry.grid(row=0,column=1, sticky="w")
        #Article à ajouter
        liste_article = ControllerNomenclature.get_back_end_article()
        article_ajouter_label = CTkLabel(nomenclature_nouveau, text="Article à ajouter :",  padx=1, pady=1)
        article_ajouter_label.grid(row=1,column=0, sticky="w")
        article_ajouter_entry = CTkComboBox(nomenclature_nouveau, width= 250, 
                                variable=self.article_to_add, 
                                values=[sublist[1] for sublist in liste_article])
        article_ajouter_entry.grid(row=1,column=1, sticky="w")

        #Add the save button
        nouvelle_nomenclature_save_button = CTkButton(nomenclature_nouveau, text="Valider", width=150,
                                                      command= lambda:[ControllerNomenclature.add_new_article_to_bom(front_end_article=self.type_terrain.get(),
                                                                                      article_to_add=self.article_to_add.get()),
                                                                        nomenclature_nouveau.destroy()])
        nouvelle_nomenclature_save_button.grid(row=2, column=1, sticky="NSEW", ipadx = 10, ipady= 10)