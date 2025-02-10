import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.controller.controller_quality_lot import ControllerLot

class Lot:
    def __init__(self, parent_frame):
        """
        Initialize the Lot view.
        :param parent_frame: The frame where the Lot view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange the widgets for the Lot view.
        """
        description = tk.StringVar()
        lot = tk.StringVar()
        article = tk.StringVar()

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)     

        # Everything that goes into the first information frame
        frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Lot", padx=5, pady=5, width = 250)
        frame1_info_label.grid(row=0, column=0)
        #Lot
        frame1_lot_label = ctk.CTkLabel(self.frame1, text="Lot :",  padx=1, pady=1)
        frame1_lot_label.grid(row=1,column=0, sticky="w")
        frame1_lot_entry = ctk.CTkEntry(self.frame1, width= 250, textvariable=lot.get(), placeholder_text="Lot")
        frame1_lot_entry.grid(row=1,column=1, sticky="w")
        #Description
        frame1_description_label = ctk.CTkLabel(self.frame1, text="Description :",  padx=1, pady=1)
        frame1_description_label.grid(row=2,column=0, sticky="w")
        frame1_description_entry = ctk.CTkEntry(self.frame1, width= 500, textvariable=description.get(), placeholder_text="Description")
        frame1_description_entry.grid(row=2,column=1, sticky="w")
        #Article
        frame1_article_label = ctk.CTkLabel(self.frame1, text="Article :",  padx=1, pady=1)
        frame1_article_label.grid(row=3,column=0, sticky="w")
        liste_article = ControllerLot.get_front_end_article()
        #Get only the description and not taking the id into account
        frame1_article_entry = ctk.CTkComboBox(self.frame1, width= 250, values=[sublist[1] for sublist in liste_article], variable=article)
        frame1_article_entry.grid(row=3,column=1, sticky="w")

        # Everything that goes into second frame with the treeview
        self.frame2 = ctk.CTkFrame(self.parent_frame)
        self.frame2.grid(row=1, column=0, sticky="nwse", padx=2, pady=2)
        #Treeview for the current batchs
        treeview_columns =('Lot', 'Description', 'Article', 'Date_modif', 'Heure_modif')
        frame2_treeview = ttk.Treeview(self.frame2, columns=treeview_columns, show='headings')
        #TODO: make the binding work
        frame2_treeview.bind("<<TreeviewSelect>>", Lot.printItems(frame2_treeview))
        frame2_treeview.column("Lot", width=20, stretch=True)
        frame2_treeview.column("Description", width=100, stretch=True)
        frame2_treeview.column("Article", width=20, stretch=True)
        frame2_treeview.column("Date_modif", width=20, stretch=True)
        frame2_treeview.column("Heure_modif", width=20, stretch=True)
        frame2_treeview.heading("Lot", text="Lot", anchor='center')
        frame2_treeview.heading("Description", text="Description", anchor='center')
        frame2_treeview.heading("Article", text="Article", anchor='center')
        frame2_treeview.heading("Date_modif", text="Date dernière modification", anchor='center')
        frame2_treeview.heading("Heure_modif", text="Heure dernière modification", anchor='center')
        frame2_treeview.pack(pady=20, fill='both')

        #Division of the section
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid_rowconfigure(0, weight=3)
        self.parent_frame.grid_rowconfigure(1, weight=5)

        ControllerLot.populate_all_lot(frame2_treeview)

    def printItems(treeview: ttk.Treeview):
        #print(f"test:")
        selected = treeview.focus()
        print(treeview.item(selected, 'values'))

