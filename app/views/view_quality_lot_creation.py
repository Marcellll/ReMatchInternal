import tkinter as tk
from tkinter import ttk
from customtkinter import *
from app.controller.controller_quality_lot import ControllerLot

class NouveauLot:
    def __init__(self):
        nouveau_lot = CTkToplevel()
        nouveau_lot.title("Nouveau batch")
        nouveau_lot.resizable(False, False)
        nouveau_lot.geometry(f"700x150")
        nouveau_lot.attributes("-topmost", True)

        description = tk.StringVar()
        lot = tk.StringVar(value=ControllerLot.get_new_batch_number())
        article = tk.StringVar()

        #Lot
        nouveau_lot_label = CTkLabel(nouveau_lot, text="Lot :",  padx=1, pady=1)
        nouveau_lot_label.grid(row=0,column=0, sticky="w")
        nouveau_lot_entry = CTkEntry(nouveau_lot, width= 250, textvariable=lot, state=tk.DISABLED)
        nouveau_lot_entry.grid(row=0,column=1, sticky="w")
        #Description
        nouveau_lot_description_label = CTkLabel(nouveau_lot, text="Description :",  padx=1, pady=1)
        nouveau_lot_description_label.grid(row=1,column=0, sticky="w")
        nouveau_lot_description_entry = CTkEntry(nouveau_lot, width= 500, textvariable=description)
        nouveau_lot_description_entry.grid(row=1,column=1, sticky="w")
        #Article
        nouveau_lot_article_label = CTkLabel(nouveau_lot, text="Article :",  padx=1, pady=1)
        nouveau_lot_article_label.grid(row=2,column=0, sticky="w")
        #Get only the description and not taking the id into account
        liste_article = ControllerLot.get_front_end_article()
        self.nouveau_lot_article_entry = CTkComboBox(nouveau_lot, width= 250, 
                                                values=[sublist[1] for sublist in liste_article], 
                                                variable=article)
        self.nouveau_lot_article_entry.grid(row=2,column=1, sticky="w")
        #Add the save button
        nouveau_lot_save_button = CTkButton(nouveau_lot, text="Valider", width=150, 
                                            command= lambda: ControllerLot.create_new_batch(lot=lot.get(),
                                                                                            description=description.get(),
                                                                                            article=liste_article[self.get_index_current_item()][0],
                                                                                            window=nouveau_lot))
        nouveau_lot_save_button.grid(row=3, column=1, sticky="NSEW", ipadx = 10, ipady= 10)

    def get_index_current_item(self):
        for index in range(len(self.nouveau_lot_article_entry.cget("values"))):
            if self.nouveau_lot_article_entry.get() == self.nouveau_lot_article_entry.cget("values")[index]:
                return index