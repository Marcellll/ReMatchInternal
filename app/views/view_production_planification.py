import tkinter as tk
from tkinter import ttk
from app.controller.controller_batch import ControllerBatch
import customtkinter as ctk


class Batch:
    def __init__(self, parent_frame):
        """
        Initialize the Batch view.
        :param parent_frame: The frame where the Batch view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange the widgets for the Batch view.
        """

        description = tk.StringVar()
        lot = tk.StringVar()
        type_terrain = tk.StringVar()
        date_debut = tk.StringVar()
        date_fin = tk.StringVar()

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2,)

        # Everything that goes into the first frame
        frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Planification", padx=5, pady=5, width = 500)
        frame1_info_label.grid(row=0, column=0)
        #Description
        frame1_description_label = ctk.CTkLabel(self.frame1, text="Description",  padx=1, pady=1)
        frame1_description_label.grid(row=1,column=0)
        frame1_description = ctk.CTkLabel(self.frame1, text=description.get(), padx=1, pady=1)
        frame1_description.grid(row=1,column=1)
        #Batch
        frame1_lot_label = ctk.CTkLabel(self.frame1, text="Batch",  padx=1, pady=1)
        frame1_lot_label.grid(row=1,column=2)
        frame1_lot = ctk.CTkLabel(self.frame1, text=lot.get(), padx=1, pady=1)
        frame1_lot.grid(row=1,column=3)
        #Type de terrain
        frame1_type_terrain_label = ctk.CTkLabel(self.frame1, text="Type de terrain", padx=1, pady=1)
        frame1_type_terrain_label.grid(row=1,column=4)
        frame1_type_terrain = ctk.CTkLabel(self.frame1, text=type_terrain.get(), padx=1, pady=1)
        frame1_type_terrain.grid(row=1,column=5)
        #Date début
        frame1_date_debut_label = ctk.CTkLabel(self.frame1, text="Date début",  padx=1, pady=1)
        frame1_date_debut_label.grid(row=2,column=0)
        frame1_date_debut = ctk.CTkLabel(self.frame1, text=date_debut.get(), padx=1, pady=1)
        frame1_date_debut.grid(row=2,column=1)
        #Date fin
        frame1_date_fin_label = ctk.CTkLabel(self.frame1, text="Date début", padx=1, pady=1)
        frame1_date_fin_label.grid(row=2,column=3)
        frame1_date_fin = ctk.CTkLabel(self.frame1, text=date_fin.get(), padx=1, pady=1)
        frame1_date_fin.grid(row=2,column=4)


        # Verything that goes into second frame
        self.frame2 = ctk.CTkFrame(self.parent_frame)
        self.frame2.grid(row=1, column=0, sticky="nwse", padx=2, pady=2)

        # Add content to Frame 2
        frame2_info_label = ctk.CTkLabel(self.frame2, text="Batch en-cours")
        frame2_info_label.pack(pady=1)
        #Treeview for the current batchs
        treeview_columns =('Lot', 'Type_terrain', 'Status', 'Date_debut', 'Date_fin', 'Description', 'Ville', 'Pays')
        frame2_treeview = ttk.Treeview(self.frame2, columns=treeview_columns, show='headings')
        frame2_treeview.pack(pady=2, fill='both')
        frame2_treeview.column("Lot", minwidth=50, stretch=True)
        frame2_treeview.column("Type_terrain", width=50, stretch=True)
        frame2_treeview.column("Status", width=50, stretch=True)
        frame2_treeview.column("Date_debut", width=50, stretch=True)
        frame2_treeview.column("Date_fin", width=50, stretch=True)
        frame2_treeview.column("Description", width=50, stretch=True)
        frame2_treeview.column("Ville", width=50, stretch=True)
        frame2_treeview.column("Pays", width=50, stretch=True)
        frame2_treeview.heading("Lot", text="Lot", anchor='center')
        frame2_treeview.heading("Type_terrain", text="Type de terrain", anchor='center')
        frame2_treeview.heading("Status", text="Status", anchor='center')
        frame2_treeview.heading("Date_debut", text="Date de début", anchor='center')
        frame2_treeview.heading("Date_fin", text="Date de fin", anchor='center')
        frame2_treeview.heading("Description", text="Description", anchor='center')
        frame2_treeview.heading("Ville", text="Ville", anchor='center')
        frame2_treeview.heading("Pays", text="Pays", anchor='center')

        # Frame 3: Bottom Frame
        self.frame3 = ctk.CTkFrame(self.parent_frame)
        self.frame3.grid(row=2, column=0, sticky="nwse", padx=2, pady=2)

        # Add content to Frame 3
        frame3_info_label = ctk.CTkLabel(self.frame3, text="Batch à choisir")
        frame3_info_label.pack(pady=1)
        #Treeview of all the batchs
        frame3_treeview = ttk.Treeview(self.frame3, columns=treeview_columns, show='headings')
        frame3_treeview.pack(pady=2, fill='y')
        frame3_treeview.column("Lot", minwidth=50, stretch=True)
        frame3_treeview.column("Type_terrain", width=50, stretch=True)
        frame3_treeview.column("Status", width=50, stretch=True)
        frame3_treeview.column("Date_debut", width=50, stretch=True)
        frame3_treeview.column("Date_fin", width=50, stretch=True)
        frame3_treeview.column("Description", width=50, stretch=True)
        frame3_treeview.column("Ville", width=50, stretch=True)
        frame3_treeview.column("Pays", width=50, stretch=True)
        frame3_treeview.heading("Lot", text="Lot", anchor='center')
        frame3_treeview.heading("Type_terrain", text="Type de terrain", anchor='center')
        frame3_treeview.heading("Status", text="Status", anchor='center')
        frame3_treeview.heading("Date_debut", text="Date de début", anchor='center')
        frame3_treeview.heading("Date_fin", text="Date de fin", anchor='center')
        frame3_treeview.heading("Description", text="Description", anchor='center')
        frame3_treeview.heading("Ville", text="Ville", anchor='center')
        frame3_treeview.heading("Pays", text="Pays", anchor='center')

        # Configure the parent frame's grid to center the frames
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid_rowconfigure(0, weight=2)
        self.parent_frame.grid_rowconfigure(1, weight=2)
        self.parent_frame.grid_rowconfigure(2, weight=6)

        #ControllerBatch.populate_all_batchs(treeview=frame3_treeview)