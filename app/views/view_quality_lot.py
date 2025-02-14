import os
import tkinter as tk
from tkinter import ttk
from PIL import Image
import customtkinter as ctk
from app.controller.controller_quality_lot import ControllerLot
from app.views.view_quality_lot_creation import NouveauLot
from os import path
import utils.settings as settings

class Lot:
    def __init__(self, parent_frame):
        """
        Initialize the Lot view.
        :param parent_frame: The frame where the Lot view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def display_lot(self, e):
        item = self.frame2_treeview.identify('item',e.x,e.y)
        values = self.frame2_treeview.item(item, "values")
        self.lot.set(values[0])
        self.description.set(values[1])
        self.article.set(values[2])
    
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
        
    def create_widgets(self):
        """
        Create and arrange the widgets for the Lot view.
        """
        self.description = tk.StringVar(self.parent_frame)
        self.lot = tk.StringVar(self.parent_frame)
        self.article = tk.StringVar(self.parent_frame)

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)     

        # Everything that goes into the first information frame
        self.frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Lot", padx=5, pady=5, width = 250)
        self.frame1_info_label.grid(row=0, column=0)
        #Lot
        self.frame1_lot_label = ctk.CTkLabel(self.frame1, text="Lot :",  padx=1, pady=1)
        self.frame1_lot_label.grid(row=1,column=0, sticky="w")
        self.frame1_lot_entry = ctk.CTkEntry(self.frame1, width= 250, textvariable=self.lot, state=tk.DISABLED)
        self.frame1_lot_entry.grid(row=1,column=1, sticky="w")
        #Description
        self.frame1_description_label = ctk.CTkLabel(self.frame1, text="Description :",  padx=1, pady=1)
        self.frame1_description_label.grid(row=2,column=0, sticky="w")
        self.frame1_description_entry = ctk.CTkEntry(self.frame1, width= 500, textvariable=self.description)
        self.frame1_description_entry.grid(row=2,column=1, sticky="w")
        #Article
        self.frame1_article_label = ctk.CTkLabel(self.frame1, text="Article :",  padx=1, pady=1)
        self.frame1_article_label.grid(row=3,column=0, sticky="w")
        liste_article = ControllerLot.get_front_end_article()
        #Get only the description and not taking the id into account
        self.frame1_article_entry = ctk.CTkComboBox(self.frame1, width= 250, values=[sublist[1] for sublist in liste_article], variable=self.article)
        self.frame1_article_entry.grid(row=3,column=1, sticky="w")

        #Adding a new batch
        button_width = 50
        button_height = 50
        self.frame1_adding_button = ctk.CTkButton(self.frame1, text ="Nouveau lot", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\plus.png", button_width, button_height),

                                                  command= lambda: [NouveauLot(),
                                                                    ControllerLot.populate_all_lot(self.frame2_treeview)])

        self.frame1_adding_button.grid(row=0, column=2)

        #Converting a batch to an OF
        self.frame1_create_OF = ctk.CTkButton(self.frame1, text ="Créer OF", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\engrenage.png", button_width, button_height),

                                                  command= lambda: [ControllerLot.create_new_OF(lot=self.lot.get(), article=self.article.get()),
                                                                    ControllerLot.populate_all_lot(self.frame2_treeview)]
                                                  )
        self.frame1_create_OF.grid(row=1, column=2)

        #Saving changes to a batch
        self.frame1_save_OF = ctk.CTkButton(self.frame1, text ="Sauvegarder lot", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\sauvegarder.png", button_width, button_height),
                                                  command= lambda: [ControllerLot.save_lot(lot=self.lot.get(), 
                                                                                          article=self.article.get(),
                                                                                          update_description=self.description.get()),
                                                                    ControllerLot.populate_all_lot(self.frame2_treeview)]                                                  
                                                  )
        self.frame1_save_OF.grid(row=2, column=2)


        # Everything that goes into second frame with the treeview
        self.frame2 = ctk.CTkFrame(self.parent_frame)
        self.frame2.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        self.frame21 = tk.Frame(self.frame2)
        self.frame21.pack(fill='both', expand=True)
        self.frame21_scrollbar = tk.Scrollbar(self.frame21)
        self.frame21_scrollbar.pack(side="right", fill="y")
        #Treeview for the current batchs
        treeview_style = ttk.Style()
        treeview_style.configure("treeview_style.Treeview", font=('Verdana', 16), rowheight=45)
        treeview_style.configure("treeview_style.Treeview.Heading", font=('Verdana', 20, 'bold'), padding=5)
        # Define tags and their styles
        treeview_columns =('Lot', 'Description', 'Article', 'Date_modif', 'Heure_modif', 'Status_OF')
        self.frame2_treeview = ttk.Treeview(self.frame21, columns=treeview_columns, show='headings', 
                                            yscrollcommand=self.frame21_scrollbar.set,
                                            style="treeview_style.Treeview")
        self.frame2_treeview.tag_configure("Crée", background="#ccffcc", foreground="black")      # Light green
        self.frame2_treeview.tag_configure("Planifié", background="#ffffcc", foreground="black")  # Light yellow
        self.frame2_treeview.tag_configure("Terminé", background="#ccccff", foreground="black")

        self.frame2_treeview.bind("<Double-1>", self.display_lot)
        self.frame2_treeview.column("Lot", width=20, stretch=True)
        self.frame2_treeview.column("Description", width=100, stretch=True)
        self.frame2_treeview.column("Article", width=20, stretch=True)
        self.frame2_treeview.column("Date_modif", width=20, stretch=True)
        self.frame2_treeview.column("Heure_modif", width=20, stretch=True)
        self.frame2_treeview.column("Status_OF", width=20, stretch=True)
        self.frame2_treeview.heading("Lot", text="Lot", anchor='center')
        self.frame2_treeview.heading("Description", text="Description", anchor='center')
        self.frame2_treeview.heading("Article", text="Article", anchor='center')
        self.frame2_treeview.heading("Date_modif", text="Date dernière modification", anchor='center')
        self.frame2_treeview.heading("Heure_modif", text="Heure dernière modification", anchor='center')
        self.frame2_treeview.heading("Status_OF", text="Status Ordre de fabrication", anchor='center')
        self.frame2_treeview.pack(fill='both', expand= True)

        self.frame21_scrollbar.config(command=self.frame2_treeview.yview)

        #Division of the section
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid_rowconfigure(0, weight=3)
        self.parent_frame.grid_rowconfigure(1, weight=7)

        ControllerLot.populate_all_lot(self.frame2_treeview)


