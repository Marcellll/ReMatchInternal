import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.model.model_ordre_fabrication import StatusOF
from app.controller.controller_planification import ControllerPlanification
from app.views.view_calendrier import ViewCalendrier
from app.views.view_message_erreur import MessageErreur
from app.views.view_production_planification_nouveau import PlanificationLot
from PIL import Image
from os import path
import utils.settings as settings

class Batch:
    def __init__(self, parent_frame, status = ""):
        """
        Initialize the Batch view.
        :param parent_frame: The frame where the Batch view will be displayed.
        """
        self.parent_frame = parent_frame
        self.status = status
        self.create_widgets()

    def display_ordre(self, e, treeview):
        ordre = treeview.identify('item',e.x,e.y)
        values = treeview.item(ordre, "values")
        self.lot.set(values[0])
        self.description.set(values[5])
        self.type_terrain.set(values[1])
        self.date_debut.set(values[3])
        self.date_fin.set(values[4])
        self.status = values[2]


    def resize_image(self, icon_path: str, image_width: int, image_height:int):
        try:
            image_path = path.abspath(path.join(settings.path_name,icon_path))
            # Open the image
            original_image = Image.open(image_path)
            # Resize the image to fit the button
            resized_image = original_image.resize((image_width, image_height))
            # Convert the resized image to a Tkinter-compatible format
            return ctk.CTkImage(resized_image, resized_image)
        except Exception as e:
            print(f"Error loading or resizing image: {e}")

    def plan_lot(self, lot: str, status: str, date_debut: str, date_fin:str):
        if lot == '':
            MessageErreur(f"Double cliquez sur une ligne de lot pour créer l'OF")
            return
        
        if status != StatusOF.CREE.value:
            MessageErreur(f"Planification impossible de cet OF car il est en statut: {status}")
            return

        PlanificationLot(lot=lot,date_debut=date_debut, date_fin=date_fin)
    
    def clear_information_panel(self):
        self.description.set("")
        self.lot.set("")
        self.type_terrain.set("")
        self.date_debut.set("")
        self.date_fin.set("")

    def create_widgets(self):
        """
        Create and arrange the widgets for the Batch view.
        """
        button_width = 50
        button_height = 50
        self.status = ""
        self.description = tk.StringVar()
        self.lot = tk.StringVar()
        self.type_terrain = tk.StringVar()
        self.date_debut = tk.StringVar()
        self.date_fin = tk.StringVar()

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Planification", padx=5, pady=5, width = 250)
        frame1_info_label.grid(row=0, column=0)
        #Description
        frame1_description_label = ctk.CTkLabel(self.frame1, text="Description",  padx=1, pady=1)
        frame1_description_label.grid(row=1,column=0)
        frame1_description = ctk.CTkEntry(self.frame1, textvariable=self.description, width=450, state=tk.DISABLED)
        frame1_description.grid(row=1,column=1)
        #Batch
        frame1_lot_label = ctk.CTkLabel(self.frame1, text="Batch",  padx=1, pady=1)
        frame1_lot_label.grid(row=2,column=0)
        frame1_lot = ctk.CTkEntry(self.frame1, textvariable=self.lot, width=250, state=tk.DISABLED)
        frame1_lot.grid(row=2,column=1)
        #Type de terrain
        frame1_type_terrain_label = ctk.CTkLabel(self.frame1, text="Type de terrain", padx=1, pady=1)
        frame1_type_terrain_label.grid(row=3,column=0)
        frame1_type_terrain = ctk.CTkEntry(self.frame1, textvariable=self.type_terrain, width=250, state=tk.DISABLED)
        frame1_type_terrain.grid(row=3,column=1)
        #Date début
        frame1_date_debut_label = ctk.CTkLabel(self.frame1, text="Date début",  padx=1, pady=1)
        frame1_date_debut_label.grid(row=4,column=0)
        frame1_date_debut = ctk.CTkEntry(self.frame1, textvariable=self.date_debut, width=250)
        frame1_date_debut.grid(row=4,column=1)
        frame1_date_debut_picker = ctk.CTkButton(self.frame1, text= "",
                                                 width=button_width, height=button_height,
                                                 image=self.resize_image("static\\date.png", button_width, button_height),
                                                 command= lambda:ViewCalendrier(self.date_debut))
        frame1_date_debut_picker.grid(row=4, column=2)
        #Date fin
        frame1_date_fin_label = ctk.CTkLabel(self.frame1, text="Date début", padx=1, pady=1)
        frame1_date_fin_label.grid(row=5,column=0)
        frame1_date_fin = ctk.CTkEntry(self.frame1, textvariable=self.date_fin, width=250)
        frame1_date_fin.grid(row=5,column=1)
        frame1_date_fin_picker = ctk.CTkButton(self.frame1, text= "",
                                                 width=button_width, height=button_height,
                                                 image=self.resize_image("static\\date.png", button_width, button_height),
                                                 command= lambda: ViewCalendrier(self.date_fin))
        frame1_date_fin_picker.grid(row=5, column=2)

        #Planifier le batch
        self.frame1_adding_button = ctk.CTkButton(self.frame1, text ="Planifier lot", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\planification.png", button_width, button_height),
                                                  command= lambda: [self.plan_lot(lot=self.lot.get(), status=self.status, 
                                                                                  date_debut=self.date_debut.get(), date_fin=self.date_fin.get()),
                                                                    ControllerPlanification.populate_ordre_to_be_worked_on(treeview=frame2_treeview),
                                                                    ControllerPlanification.populate_all_ordre_to_work_on(treeview=frame3_treeview)])

        self.frame1_adding_button.grid(row=0, column=3)
        #Terminer un lot
        self.frame1_refresh_button = ctk.CTkButton(self.frame1, text ="Terminer lot", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\ok.png", button_width, button_height),
                                                  command= lambda: [ControllerPlanification.finish_ordre(self.lot.get()),
                                                                    self.clear_information_panel(),
                                                                    ControllerPlanification.populate_ordre_to_be_worked_on(treeview=frame2_treeview),
                                                                    ControllerPlanification.populate_all_ordre_to_work_on(treeview=frame3_treeview)])

        self.frame1_refresh_button.grid(row=1, column=3)
        #Sauvegarder changement de date
        self.frame1_save_button = ctk.CTkButton(self.frame1, text ="Enregistrer", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\sauvegarder.png", button_width, button_height),
                                                  command= lambda: [ControllerPlanification.update_date(lot=self.lot.get(),
                                                                                                       date_debut=self.date_debut.get(),
                                                                                                       date_fin=self.date_fin.get()),
                                                                    ControllerPlanification.populate_ordre_to_be_worked_on(treeview=frame2_treeview),
                                                                    ControllerPlanification.populate_all_ordre_to_work_on(treeview=frame3_treeview)])

        self.frame1_save_button.grid(row=2, column=3)
        #Rafraîchir les listes
        self.frame1_refresh_button = ctk.CTkButton(self.frame1, text ="Rafraîchir", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\recharger.png", button_width, button_height),
                                                  command= lambda: [self.clear_information_panel(),
                                                                    ControllerPlanification.populate_ordre_to_be_worked_on(treeview=frame2_treeview),
                                                                    ControllerPlanification.populate_all_ordre_to_work_on(treeview=frame3_treeview)])

        self.frame1_refresh_button.grid(row=3, column=3)


        # Verything that goes into second frame
        self.frame2 = ctk.CTkFrame(self.parent_frame)
        self.frame2.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        # Add content to Frame 2
        frame2_info_label = ctk.CTkLabel(self.frame2, text="Batch en-cours")
        frame2_info_label.pack(pady=1)
        #Frame for Treeview
        self.frame21 = ctk.CTkFrame(self.frame2)
        self.frame21.pack(fill='x', expand=False)
        #Scrollbar for treeview
        frame2_treeview_scrollbar = tk.Scrollbar(self.frame21)
        frame2_treeview_scrollbar.pack(side="right", fill="y")
        #Treeview style
        treeview_style = ttk.Style()
        treeview_style.configure("treeview_style.Treeview", font=('Verdana', 16), rowheight=45)
        treeview_style.configure("treeview_style.Treeview.Heading", font=('Verdana', 20, 'bold'), padding=5)
        #Treeview for the current batchs
        frame2_treeview_columns =('Lot', 'Type_terrain', 'Status', 'Date_debut', 'Date_fin', 'Description')
        frame2_treeview = ttk.Treeview(self.frame21, columns=frame2_treeview_columns, show='headings', 
                                       yscrollcommand=frame2_treeview_scrollbar.set,
                                       style="treeview_style.Treeview",
                                       height=5)
        frame2_treeview.bind("<Double-1>", lambda e: self.display_ordre(e=e, treeview=frame2_treeview))
        frame2_treeview.pack(pady=2, fill='both', expand=True)
        frame2_treeview.column("Lot", width=20, stretch=True)
        frame2_treeview.column("Type_terrain", width=50, stretch=True)
        frame2_treeview.column("Status", width=50, stretch=True)
        frame2_treeview.column("Date_debut", width=50, stretch=True)
        frame2_treeview.column("Date_fin", width=50, stretch=True)
        frame2_treeview.column("Description", width=50, stretch=True)
        frame2_treeview.heading("Lot", text="Lot", anchor='center')
        frame2_treeview.heading("Type_terrain", text="Type de terrain", anchor='center')
        frame2_treeview.heading("Status", text="Status", anchor='center')
        frame2_treeview.heading("Date_debut", text="Date de début", anchor='center')
        frame2_treeview.heading("Date_fin", text="Date de fin", anchor='center')
        frame2_treeview.heading("Description", text="Description", anchor='center')
        #Config the scrollbar
        frame2_treeview_scrollbar.config(command=frame2_treeview.yview)
        #Populate the treeview
        liste_OF_ouvert = ControllerPlanification.get_ordered_batches()
        for OF in liste_OF_ouvert:
             new_line = [OF[0], OF[1], OF[2], OF[3], OF[4], OF[5]]
             frame2_treeview.insert("", "end", values=new_line)

        # Frame 3: Bottom Frame
        self.frame3 = ctk.CTkFrame(self.parent_frame)
        self.frame3.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

        # Add content to Frame 3
        frame3_info_label = ctk.CTkLabel(self.frame3, text="Batch à choisir")
        frame3_info_label.pack(side="top")
           
        #Frame for Treeview
        self.frame31 = ctk.CTkFrame(self.frame3)
        self.frame31.pack(fill='both', expand=False)
        #Scrollbar for treeview
        frame3_treeview_columns =('Lot', 'Type_terrain', 'Status', 'Date_debut', 'Date_fin', 'Description')
        frame3_treeview_scrollbar = tk.Scrollbar(self.frame31)
        frame3_treeview_scrollbar.pack(side="right", fill="y")
        frame3_treeview = ttk.Treeview(self.frame31, columns=frame3_treeview_columns, show='headings', 
                                       yscrollcommand=frame3_treeview_scrollbar.set,
                                       style="treeview_style.Treeview",
                                       height=7)
        frame3_treeview.tag_configure("Crée", background="#ccffcc", foreground="black") # Light green
        frame3_treeview.tag_configure("Terminé", background="#ccccff", foreground="black") #Light blue
        frame3_treeview.bind("<Double-1>", lambda e: self.display_ordre(e=e, treeview=frame3_treeview))   
        frame3_treeview.pack(pady=2, fill='both', expand=True)
        frame3_treeview.column("Lot", width=50, stretch=True)
        frame3_treeview.column("Type_terrain", width=50, stretch=True)
        frame3_treeview.column("Status", width=50, stretch=True)
        frame3_treeview.column("Date_debut", width=50, stretch=True)
        frame3_treeview.column("Date_fin", width=50, stretch=True)
        frame3_treeview.column("Description", width=50, stretch=True)
        frame3_treeview.heading("Lot", text="Lot", anchor='center')
        frame3_treeview.heading("Type_terrain", text="Type de terrain", anchor='center')
        frame3_treeview.heading("Status", text="Status Ordre", anchor='center')
        frame3_treeview.heading("Date_debut", text="Date de début", anchor='center')
        frame3_treeview.heading("Date_fin", text="Date de fin", anchor='center')
        frame3_treeview.heading("Description", text="Description", anchor='center')
        #Config the scrollbar
        frame3_treeview_scrollbar.config(command=frame3_treeview.yview)

        ControllerPlanification.populate_ordre_to_be_worked_on(treeview=frame2_treeview)
        ControllerPlanification.populate_all_ordre_to_work_on(treeview=frame3_treeview)
        