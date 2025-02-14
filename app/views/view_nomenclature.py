import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from os import path
from PIL import Image
from app.controller.controller_nomenclature import ControllerNomenclature
from app.views.view_message_erreur import MessageErreur
from app.views.view_nomenclature_ajouter import NomenclatureNouveau
import utils.settings as settings

class Nomenclature:
    def __init__(self, parent_frame):
        """
        Initialize the Settings view.
        :param parent_frame: The frame where the Settings view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def bom_selection(self, choice):
        if choice == None:
            choice = self.article.get()
        bom_article = ControllerNomenclature.get_article_bom(article_description=choice)
        self.frame11_treeview.delete(*self.frame11_treeview.get_children())   
        for article in bom_article:
            new_line = [article[2], article[3]]
            self.frame11_treeview.insert("", "end", values=new_line)

    def set_article_to_delete(self, choice):
        entry = self.frame11_treeview.focus()
        if len(self.frame11_treeview.item(entry, "values")) > 0:
            self.article_to_delete = self.frame11_treeview.item(entry, "values")[1]

    def get_article_to_delete(self):
        return self.article_to_delete
    
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

    def new_article(self):
        if self.article.get() == '':
            MessageErreur("""Choissisez un article dans la liste déroulante""")
            return
        NomenclatureNouveau(type_terrain=self.article.get())

    def create_widgets(self):
        """
        Create and arrange the widgets for the Settings view.
        """
        self.article = tk.StringVar()
        self.article_nomenclature = tk.StringVar()
        self.article_to_delete = ""
        button_width = 50
        button_height = 50

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky='ew', padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Nomenclature")
        frame1_info_label.grid(row=0, column=0)

        #Type de terrain front-end
        frame1_article_label = ctk.CTkLabel(self.frame1, text="Type de terrain :",  padx=1, pady=1)
        frame1_article_label.grid(row=1,column=0, sticky="w")
        liste_article = ControllerNomenclature.get_front_end_article()
        #Get all the frontend type of fields
        self.frame1_article_entry = ctk.CTkComboBox(self.frame1, width= 250, values=[sublist[1] for sublist in liste_article], variable=self.article,
                                                    command=self.bom_selection)
        self.frame1_article_entry.grid(row=1,column=1, sticky="w")

        #Add button to add new article to bom
        self.frame1_adding_button = ctk.CTkButton(self.frame1, text ="Ajouter article", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\plus.png", button_width, button_height),
                                                  command=lambda:[self.new_article(),
                                                                self.bom_selection(choice=None)])
        self.frame1_adding_button.grid(row=2, column=2)
        #Rafraîchir la liste
        self.frame1_refresh_button = ctk.CTkButton(self.frame1, text ="Rafraîchir", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\recharger.png", button_width, button_height),
                                                  command= lambda: self.bom_selection(choice=None))

        self.frame1_refresh_button.grid(row=3, column=2)
        #Add button to delete article from bom
        self.frame1_delete_button = ctk.CTkButton(self.frame1, text ="Supprimer article", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\supprimer.png", button_width, button_height),
                                                  command=lambda:[ControllerNomenclature.delete_article_in_bom(front_end_article=self.article.get(),
                                                                                                               article_to_delete=self.get_article_to_delete()),
                                                                self.bom_selection(choice=None)])
        self.frame1_delete_button.grid(row=4, column=2)

        #Display all the articles that are connected to the choosen field
        frame11 = tk.Frame(self.frame1)
        frame11.grid(row=2, column=0, columnspan=2, rowspan=4, sticky='nsew')
        frame11_scrollbar = tk.Scrollbar(frame11)
        frame11_scrollbar.pack(side='right', fill='y')
        #Treeview for the attached articles
        treeview_style = ttk.Style()
        treeview_style.configure("treeview_style.Treeview", font=('Verdana', 14), rowheight=45)
        treeview_style.configure("treeview_style.Treeview.Heading", font=('Verdana', 16, 'bold'), padding=5)
        #Define tags and their styles
        treeview_columns = ('Numero_article', 'Description_article')
        self.frame11_treeview = ttk.Treeview(frame11, columns=treeview_columns, show='headings',
                                        yscrollcommand=frame11_scrollbar.set,
                                        style="treeview_style.Treeview")
        self.frame11_treeview.bind('<ButtonRelease-1>', self.set_article_to_delete)
        self.frame11_treeview.column("Numero_article", width=5, stretch=True)
        self.frame11_treeview.column("Description_article", width=20, stretch=True)
        self.frame11_treeview.heading("Numero_article", text="Numéro article", anchor='w')
        self.frame11_treeview.heading("Description_article", text="Description article", anchor='w')
        self.frame11_treeview.pack(fill='both', expand=True)
        frame11_scrollbar.config(command=self.frame11_treeview.yview)