import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.controller.controller_pesee import ControllerPesee

class Pesee:
    def __init__(self, parent_frame):
        """
        Initialize the Settings view.
        :param parent_frame: The frame where the Settings view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange the widgets for the Settings view.
        """

        self.lot = tk.StringVar()
        self.article = tk.StringVar()

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = tk.Label(self.frame1, text="Nouvelle Pesee", font=("Verdana",16), padx=1, pady=1)
        frame1_info_label.grid(row=0, column=0)

        liste_ordre_fabrication = ControllerPesee.get_open_ordre_fabrication()

        #Lot
        frame1_lot_label = ctk.CTkLabel(self.frame1, text="Lot :",  padx=1, pady=1)
        frame1_lot_label.grid(row=1,column=0, sticky="w")
        frame1_lot_entry = ctk.CTkComboBox(self.frame1, width= 250, variable=self.lot, values=[sublist[0] for sublist in liste_ordre_fabrication], state=tk.DISABLED)
        frame1_lot_entry.grid(row=1,column=1, sticky="w")
        #Article #TODO: update the values after the batch selection
        frame1_article_label = ctk.CTkLabel(self.frame1, text="Description :",  padx=1, pady=1)
        frame1_article_label.grid(row=2,column=0, sticky="w")
        frame1_article_entry = ctk.CTkComboBox(self.frame1, width= 250, textvariable=self.article)
        frame1_article_entry.grid(row=2,column=1, sticky="w")
        #Article
        self.frame1_article_label = ctk.CTkLabel(self.frame1, text="Article :",  padx=1, pady=1)
        self.frame1_article_label.grid(row=3,column=0, sticky="w")