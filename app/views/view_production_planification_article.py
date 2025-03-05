import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import Image
from app.controller.controller_article_par_lot import ControllerArticleParLot
from os import path
import utils.settings as settings

class PlanificationArticle:

    def selection_lot(self, lot):
        article_par_lot = ControllerArticleParLot.get_article_par_lot(lot)
        self.frame11_treeview.delete(*self.frame11_treeview.get_children())   
        for article in article_par_lot:
            new_line = [article[0], article[1]]
            self.frame11_treeview.insert("", "end", values=new_line)
        self.article.set("")

    def resize_image(self, icon_path: str, image_width: int, image_height:int):
        try:
            image_path = path.abspath(path.join(settings.path_name,icon_path))
            # Open the image
            original_image = Image.open(image_path)
            # Resize the image to fit the button
            resized_image = original_image.resize((image_width, image_height))
            # Convert the resized image to a Tkinter-compatible format
            return CTkImage(resized_image, resized_image)
        except Exception as e:
            print(f"Error loading or resizing image: {e}")
    
    def set_article_to_delete(self, choice):
        entry = self.frame11_treeview.focus()
        if len(self.frame11_treeview.item(entry, "values")) > 0:
            self.article_to_delete = self.frame11_treeview.item(entry, "values")[1]

    def __init__(self, lot: str):
        button_width = 50
        button_height = 50
        planification_ordre = CTkToplevel()
        planification_ordre.title(f"Article pour lot {lot}")
        planification_ordre.resizable(False, False)
        planification_ordre.geometry(f"600x500")
        planification_ordre.attributes("-topmost", True)

        self.article = tk.StringVar()

        liste_article = ControllerArticleParLot.get_all_article()
        #Get all the frontend type of fields
        self.frame1_article_entry = CTkComboBox(planification_ordre, width= 250, values=[sublist[1] for sublist in liste_article], variable=self.article)
        self.frame1_article_entry.grid(row=0,column=0, sticky="w")

        #Add button to add an article to the batch
        frame1_delete_button = CTkButton(planification_ordre, text ="Ajouter article", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\plus.png", button_width, button_height),
                                                  command= lambda:[ControllerArticleParLot.add_article(lot, self.article.get()),
                                                                   self.selection_lot(lot)])
        frame1_delete_button.grid(row=0, column=1)

        #Add button to delete article from batch
        frame1_delete_button = CTkButton(planification_ordre, text ="Supprimer article", 
                                                  width=button_width, height=button_height, 
                                                  image=self.resize_image("static\\supprimer.png", button_width, button_height),
                                                  command= lambda:[ControllerArticleParLot.delete_article_in_lot(self.article_to_delete, lot),
                                                                   self.selection_lot(lot)])
        frame1_delete_button.grid(row=1, column=1)

        #Display all the articles that are connected to the choosen field
        frame1 = tk.Frame(planification_ordre)
        frame1.grid(row=2, column=0, columnspan=2, rowspan=4, sticky='nsew')
        frame11_scrollbar = tk.Scrollbar(frame1)
        frame11_scrollbar.pack(side='right', fill='y')
        #Treeview for the attached articles
        treeview_style = ttk.Style()
        treeview_style.configure("treeview_style.Treeview", font=('Verdana', 14), rowheight=45)
        treeview_style.configure("treeview_style.Treeview.Heading", font=('Verdana', 16, 'bold'), padding=5)
        #Define tags and their styles
        treeview_columns = ('Numero_article', 'Description_article')
        self.frame11_treeview = ttk.Treeview(frame1, columns=treeview_columns, show='headings',
                                        yscrollcommand=frame11_scrollbar.set,
                                        style="treeview_style.Treeview")
        self.frame11_treeview.bind('<ButtonRelease-1>', self.set_article_to_delete)
        self.frame11_treeview.column("Numero_article", width=5, stretch=True)
        self.frame11_treeview.column("Description_article", width=20, stretch=True)
        self.frame11_treeview.heading("Numero_article", text="Numéro article", anchor='w')
        self.frame11_treeview.heading("Description_article", text="Description article", anchor='w')
        self.frame11_treeview.pack(fill='both', expand=True)
        frame11_scrollbar.config(command=self.frame11_treeview.yview)

        self.selection_lot(lot)