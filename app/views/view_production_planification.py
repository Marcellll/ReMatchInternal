import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.controller.controller_planification import ControllerPlanification


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
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

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
        self.frame2.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        # Add content to Frame 2
        frame2_info_label = ctk.CTkLabel(self.frame2, text="Batch en-cours")
        frame2_info_label.pack(pady=1)
        #Frame for Treeview
        self.frame21 = ctk.CTkFrame(self.frame2)
        self.frame21.pack(fill='both', expand=True)
        #Scrollbar for treeview
        frame2_treeview_scrollbar = tk.Scrollbar(self.frame21)
        frame2_treeview_scrollbar.pack(side="right", fill="y")
        #Treeview for the current batchs
        treeview_columns =('Lot', 'Type_terrain', 'Status', 'Date_debut', 'Date_fin', 'Description', 'Ordre_planification')
        frame2_treeview = ttk.Treeview(self.frame21, columns=treeview_columns, show='headings', yscrollcommand=frame2_treeview_scrollbar.set)
        frame2_treeview.pack(pady=2, fill='both', expand=True)
        frame2_treeview.column("Lot", width=20, stretch=True)
        frame2_treeview.column("Type_terrain", width=50, stretch=True)
        frame2_treeview.column("Status", width=50, stretch=True)
        frame2_treeview.column("Date_debut", width=50, stretch=True)
        frame2_treeview.column("Date_fin", width=50, stretch=True)
        frame2_treeview.column("Description", width=50, stretch=True)
        frame2_treeview.column("Ordre_planification", width=50, stretch=True)
        frame2_treeview.heading("Lot", text="Lot", anchor='center')
        frame2_treeview.heading("Type_terrain", text="Type de terrain", anchor='center')
        frame2_treeview.heading("Status", text="Status", anchor='center')
        frame2_treeview.heading("Date_debut", text="Date de début", anchor='center')
        frame2_treeview.heading("Date_fin", text="Date de fin", anchor='center')
        frame2_treeview.heading("Description", text="Description", anchor='center')
        frame2_treeview.heading("Ordre_planification", text="Ordre de planification", anchor='center')
        #Config the scrollbar
        frame2_treeview_scrollbar.config(command=frame2_treeview.yview)
        #Populate the treeview
        liste_OF_ouvert = ControllerPlanification.get_ordered_batches()
        for OF in liste_OF_ouvert:
             new_line = [OF[0], OF[1], OF[2], OF[3], OF[4], OF[5], OF[6]]
             frame2_treeview.insert("", "end", values=new_line)

        # Frame 3: Bottom Frame
        self.frame3 = ctk.CTkFrame(self.parent_frame)
        self.frame3.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

        # Add content to Frame 3
        frame3_info_label = ctk.CTkLabel(self.frame3, text="Batch à choisir")
        frame3_info_label.pack(side="top")
           
        #Frame for Treeview
        self.frame31 = ctk.CTkFrame(self.frame3)
        self.frame31.pack(fill='both', expand=True)
        #Scrollbar for treeview
        frame3_treeview_scrollbar = tk.Scrollbar(self.frame31)
        frame3_treeview_scrollbar.pack(side="right", fill="y")
        frame3_treeview = ttk.Treeview(self.frame31, columns=treeview_columns, show='headings', yscrollcommand=frame3_treeview_scrollbar.set)      
        frame3_treeview.pack(pady=2, fill='both', expand=True)
        frame3_treeview.column("Lot", width=50, stretch=True)
        frame3_treeview.column("Type_terrain", width=50, stretch=True)
        frame3_treeview.column("Status", width=50, stretch=True)
        frame3_treeview.column("Date_debut", width=50, stretch=True)
        frame3_treeview.column("Date_fin", width=50, stretch=True)
        frame3_treeview.column("Description", width=50, stretch=True)
        frame3_treeview.heading("Lot", text="Lot", anchor='center')
        frame3_treeview.heading("Type_terrain", text="Type de terrain", anchor='center')
        frame3_treeview.heading("Status", text="Status", anchor='center')
        frame3_treeview.heading("Date_debut", text="Date de début", anchor='center')
        frame3_treeview.heading("Date_fin", text="Date de fin", anchor='center')
        frame3_treeview.heading("Description", text="Description", anchor='center')
        #Config the scrollbar
        frame3_treeview_scrollbar.config(command=frame3_treeview.yview)

        # Configure the parent frame's grid to center the frames
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid_rowconfigure(0, weight=2)
        self.parent_frame.grid_rowconfigure(1, weight=2)
        self.parent_frame.grid_rowconfigure(2, weight=6)

        #ControllerBatch.populate_all_batchs(treeview=frame3_treeview)