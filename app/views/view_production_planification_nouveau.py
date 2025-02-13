import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import Image
from app.views.view_calendrier import ViewCalendrier
from app.controller.controller_planification import ControllerPlanification

class PlanificationLot:

    def resize_image(self, path: str, image_width: int, image_height:int):
        try:
            image_path = f"{os.getcwd()}\\{path}"
            # Open the image
            original_image = Image.open(image_path)
            # Resize the image to fit the button
            resized_image = original_image.resize((image_width, image_height))
            # Convert the resized image to a Tkinter-compatible format
            return CTkImage(resized_image, resized_image)
        except Exception as e:
            print(f"Error loading or resizing image: {e}")

    def __init__(self, lot, date_debut, date_fin):
        button_width = 50
        button_height = 50
        planification_ordre = CTkToplevel()
        planification_ordre.title("Planifier Ordre de fabrication")
        planification_ordre.resizable(False, False)
        planification_ordre.geometry(f"600x200")
        planification_ordre.attributes("-topmost", True)

        self.lot = tk.StringVar(value=lot)
        self.date_debut = tk.StringVar(value=date_debut)
        self.date_fin = tk.StringVar(value=date_fin)

        #Lot
        lot_label = CTkLabel(planification_ordre, text="Lot :",  padx=1, pady=1)
        lot_label.grid(row=0,column=0, sticky="w")
        lot_entry = CTkEntry(planification_ordre, width= 250, textvariable=self.lot, state=tk.DISABLED)
        lot_entry.grid(row=0,column=1, sticky="w")
        #Date début
        date_debut_label = CTkLabel(planification_ordre, text="Date début :",  padx=1, pady=1)
        date_debut_label.grid(row=1,column=0, sticky="w")
        date_debut_entry = CTkEntry(planification_ordre, width= 250, textvariable=self.date_debut)
        date_debut_entry.grid(row=1,column=1, sticky="w")
        date_debut_picker = CTkButton(planification_ordre, text= "",
                                        width=button_width, height=button_height,
                                        image=self.resize_image("static\\date.png", button_width, button_height),
                                        command= lambda: ViewCalendrier(self.date_debut))
        date_debut_picker.grid(row=1, column=2)
        #Date fin
        date_fin_label = CTkLabel(planification_ordre, text="Date fin :",  padx=1, pady=1)
        date_fin_label.grid(row=2,column=0, sticky="w")
        date_fin_entry = CTkEntry(planification_ordre, width= 250, textvariable=self.date_fin)
        date_fin_entry.grid(row=2,column=1, sticky="w")
        date_debut_picker = CTkButton(planification_ordre, text= "",
                                        width=button_width, height=button_height,
                                        image=self.resize_image("static\\date.png", button_width, button_height),
                                        command= lambda: ViewCalendrier(self.date_fin))
        date_debut_picker.grid(row=2, column=2)

        #Add the save button
        nouveau_lot_save_button = CTkButton(planification_ordre, text="Valider", width=150,
                                            command= lambda:[ControllerPlanification.planifie_ordre(lot=self.lot.get(), 
                                                                                                 date_debut=self.date_debut.get(), 
                                                                                                 date_fin=self.date_fin.get()),
                                                             planification_ordre.destroy()])
        nouveau_lot_save_button.grid(row=3, column=1, sticky="NSEW", ipadx = 10, ipady= 10)
