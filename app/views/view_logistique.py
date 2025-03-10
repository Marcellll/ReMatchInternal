import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.views.view_calendrier import ViewCalendrier
from app.views.view_logistique_creation_camion import LogistiqueCamion
from app.views.view_message_erreur import MessageErreur
from app.controller.controller_chargement import ControllerChargement
from utils import settings
from datetime import datetime

class Logistique:

    def display_chargement(self, e, treeview:ttk.Treeview):
        chargement = treeview.identify('item',e.x,e.y)
        values = treeview.item(chargement, "values")
        self.chargement.set(values[0])
        self.date_debut.set(values[1])
        self.date_fin.set(values[2])
        self.list_camion(values[0])

    def display_camion(self, e):
        camion = self.frame3_treeview.identify('item',e.x,e.y)
        values = self.frame3_treeview.item(camion, "values")
        self.description_camion.set(value=values[0])

    def list_camion(self, numero_chargement: int):
        if numero_chargement == 0:
            MessageErreur("Double cliquez sur un chargement pour rafraîchir la liste des camions")
            return
        self.frame3_treeview.delete(*self.frame3_treeview.get_children())
        liste_camion = ControllerChargement.get_all_camion(numero_chargement)
        for camion in liste_camion:
            if camion[1] != None and camion[2] != None:
                entree = datetime.combine(camion[1], camion[2])
            else :
                entree = None
            if camion[3] != None and camion[4] != None:
                sortie = datetime.combine(camion[3], camion[4])
            else :
                sortie = None
            new_line = [camion[0], entree, sortie, camion[5], camion[6], camion[7]]
            self.frame3_treeview.insert("", "end", values=new_line)

    def __init__(self, parent_frame):
        """
        Initialize the Settings view.
        :param parent_frame: The frame where the Settings view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange the widgets for the Logistique view.
        """
        button_width = 50
        button_height = 50
        self.chargement = tk.IntVar(value=0)
        self.date_debut = tk.StringVar()
        self.date_fin = tk.StringVar()
        self.description_camion = tk.StringVar()
        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Logistique", font=("Verdana",16), padx=1, pady=1)
        frame1_info_label.grid(row=0, column=0)
        #Numéro chargement
        frame1_description_label = ctk.CTkLabel(self.frame1, text="Chargement",  padx=1, pady=1)
        frame1_description_label.grid(row=1,column=0)
        frame1_description = ctk.CTkEntry(self.frame1, textvariable=self.chargement, width=150, state=tk.DISABLED)
        frame1_description.grid(row=1,column=1)
        #Date début
        frame1_date_debut_label = ctk.CTkLabel(self.frame1, text="Date début",  padx=1, pady=1)
        frame1_date_debut_label.grid(row=2,column=0)
        frame1_date_debut = ctk.CTkEntry(self.frame1, textvariable=self.date_debut, width=150)
        frame1_date_debut.grid(row=2,column=1)
        frame1_date_debut_picker = ctk.CTkButton(self.frame1, text= "",
                                                 width=button_width, height=button_height,
                                                 image=settings.resize_image("static\\date.png", button_width, button_height),
                                                 command= lambda:ViewCalendrier(self.date_debut))
        frame1_date_debut_picker.grid(row=2, column=2)
        #Date fin
        frame1_date_fin_label = ctk.CTkLabel(self.frame1, text="Date début", padx=1, pady=1)
        frame1_date_fin_label.grid(row=3,column=0)
        frame1_date_fin = ctk.CTkEntry(self.frame1, textvariable=self.date_fin, width=150)
        frame1_date_fin.grid(row=3,column=1)
        frame1_date_fin_picker = ctk.CTkButton(self.frame1, text= "",
                                                 width=button_width, height=button_height,
                                                 image=settings.resize_image("static\\date.png", button_width, button_height),
                                                 command= lambda: ViewCalendrier(self.date_fin))
        frame1_date_fin_picker.grid(row=3, column=2)
        #Description camion
        frame1_description_label = ctk.CTkLabel(self.frame1, text="Description", padx=1, pady=1)
        frame1_description_label.grid(row=1,column=3)
        frame1_description = ctk.CTkEntry(self.frame1, textvariable=self.description_camion, width=150)
        frame1_description.grid(row=1,column=4)

        # Everything that goes into second frame
        self.frame2 = ctk.CTkFrame(self.parent_frame)
        self.frame2.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        # Add content to Frame 2
        frame2_info_label = ctk.CTkLabel(self.frame2, text="Chargement")
        frame2_info_label.pack(pady=1)
        frame2_button = ctk.CTkFrame(self.frame2)
        frame2_button.pack(fill='x', expand=True)
        #Add a button to create a new chargement
        frame2_chargement_button = ctk.CTkButton(frame2_button, text="Chargement",
                                            width=button_width, height=button_height, 
                                            image=settings.resize_image("static\\plus.png", button_width, button_height))
        frame2_chargement_button.pack(side='left')
        #Add a button for additional truck
        frame2_truck_button = ctk.CTkButton(frame2_button, text="Camion",
                                            width=button_width, height=button_height, 
                                            image=settings.resize_image("static\\plus.png", button_width, button_height),
                                            command= lambda:LogistiqueCamion(self.chargement.get()))
        frame2_truck_button.pack(side='left')
        self.frame21 = ctk.CTkFrame(self.frame2)
        self.frame21.pack(fill='x', expand=True)
        #Scrollbar for treeview
        frame2_treeview_scrollbar = tk.Scrollbar(self.frame21)
        frame2_treeview_scrollbar.pack(side="right", fill="y")
        #Treeview style
        treeview_style = ttk.Style()
        treeview_style.configure("treeview_style.Treeview", font=('Verdana', 16), rowheight=45)
        treeview_style.configure("treeview_style.Treeview.Heading", font=('Verdana', 20, 'bold'), padding=5)
        #Treeview for the current batchs
        frame2_treeview_columns =('Numero_chargement', 'Date_debut', 'Date_fin', 'Chargement_Dechargement', 'Lot')
        frame2_treeview = ttk.Treeview(self.frame21, columns=frame2_treeview_columns, show='headings', 
                                       yscrollcommand=frame2_treeview_scrollbar.set,
                                       style="treeview_style.Treeview",
                                       height=5)
        frame2_treeview.bind("<Double-1>", lambda e: self.display_chargement(e=e, treeview=frame2_treeview))
        frame2_treeview.pack(pady=2, fill='both', expand=True)
        frame2_treeview.column("Numero_chargement", width=20, stretch=True)
        frame2_treeview.column("Date_debut", width=20, stretch=True)
        frame2_treeview.column("Date_fin", width=20, stretch=True)
        frame2_treeview.column("Chargement_Dechargement", width=20, stretch=True)
        frame2_treeview.column("Lot", width=20, stretch=True)
        frame2_treeview.heading("Numero_chargement", text="Num chargement", anchor='center')
        frame2_treeview.heading("Date_debut", text="Date début", anchor='center')
        frame2_treeview.heading("Date_fin", text="Date fin", anchor='center')
        frame2_treeview.heading("Chargement_Dechargement", text="E/S", anchor='center')
        frame2_treeview.heading("Lot", text="Lot", anchor='center')
        #Config the scrollbar
        frame2_treeview_scrollbar.config(command=frame2_treeview.yview)
        liste_chargement_ouvert = ControllerChargement.get_all_chargement()
        for chargement in liste_chargement_ouvert:
            new_line = [chargement[0], chargement[1], chargement[2], chargement[3], chargement[4]]
            frame2_treeview.insert("", "end", values=new_line)


        # Frame 3: Bottom Frame for trucks
        self.frame3 = ctk.CTkFrame(self.parent_frame)
        self.frame3.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

        # Add content to Frame 3
        frame3_info_label = ctk.CTkLabel(self.frame3, text="Camion(s) du chargement")
        frame3_info_label.pack(side="top")
        #Frame for buttons
        frame3_button = ctk.CTkFrame(self.frame3)
        frame3_button.pack(fill='x', expand=True)
        #Refresh button
        frame3_refresh_button = ctk.CTkButton(frame3_button, text="Rafraîchir",
                                            width=button_width, height=button_height, 
                                            image=settings.resize_image("static\\recharger.png", button_width, button_height),
                                            command= lambda:self.list_camion(self.chargement.get()))
        frame3_refresh_button.pack(side='left')
        #Frame for Treeview
        self.frame31 = ctk.CTkFrame(self.frame3)
        self.frame31.pack(fill='both', expand=False)
        #Scrollbar for treeview
        frame3_treeview_columns =('Camion', 'Date_entree', 'Date_sortie', 'Poids_in', 'Poids_out', 'Numéro_interne')
        frame3_treeview_scrollbar = tk.Scrollbar(self.frame31)
        frame3_treeview_scrollbar.pack(side="right", fill="y")
        self.frame3_treeview = ttk.Treeview(self.frame31, columns=frame3_treeview_columns, show='headings', 
                                       yscrollcommand=frame3_treeview_scrollbar.set,
                                       style="treeview_style.Treeview",
                                       height=7)   
        self.frame3_treeview.pack(pady=2, fill='both', expand=True)
        self.frame3_treeview.bind("<Double-1>", lambda e: self.display_camion(e=e))
        self.frame3_treeview.column("Camion", width=20, stretch=True)
        self.frame3_treeview.column("Date_entree", width=20, stretch=True)
        self.frame3_treeview.column("Date_sortie", width=20, stretch=True)
        self.frame3_treeview.column("Poids_in", width=20, stretch=True)
        self.frame3_treeview.column("Poids_out", width=20, stretch=True)
        self.frame3_treeview.column("Numéro_interne", width=20, stretch=True)
        self.frame3_treeview.heading("Camion", text="Camion", anchor="center")
        self.frame3_treeview.heading("Date_entree", text="Entrée", anchor="center")
        self.frame3_treeview.heading("Date_sortie", text="Sortie", anchor="center")
        self.frame3_treeview.heading("Poids_in", text="In", anchor="center")
        self.frame3_treeview.heading("Poids_out", text="Out", anchor="center")
        self.frame3_treeview.heading("Numéro_interne", text="Carte", anchor="center")

