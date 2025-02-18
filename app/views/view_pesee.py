import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.controller.controller_pesee import ControllerPesee, Balance
from queue import Queue

class ScaleWeight:
    def __init__(self, scale_name):
        self.scale_name = scale_name
        self.weight = 0.0
        self.stability = "Unstable"

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_stability(self, new_stability):
        self.stability = new_stability

class Pesee(tk.Frame):
    def __init__(self, parent_frame, data_queue: Queue):
        """
        Initialize the Settings view.
        :param parent_frame: The frame where the Settings view will be displayed.
        """
        super().__init__(parent_frame)
        self.parent_frame = parent_frame
        self.controller = ControllerPesee(parent_frame, data_queue)
        self.data_queue = self.controller.data_queue
        self.controller.start_scales()
        self.scale_models = {balance.name: ScaleWeight(balance.name) for balance in Balance}
        self.create_widgets()

    def update_display(self):
        while not self.data_queue.empty():
            scale_name, weight, stability = self.data_queue.get()
            self.scale_models[scale_name].update_weight(weight)
            self.scale_models[scale_name].update_stability(stability)

        current_scale = self.balance.get()
        current_weight = self.scale_models[current_scale].weight
        current_stability = self.scale_models[current_scale].stability
        self.poids.set(current_weight)
        self.stability.set(current_stability)

        # Schedule next update
        self.after(100, self.update_display)

    def update_article_values(self, var, index, mode):
        liste_article = ControllerPesee.get_article_par_lot(self.lot.get())
        self.frame1_article_entry.configure(values=[str(sublist[0]) for sublist in liste_article])

    def clear_input(self):
        self.lot.trace_remove(['write'], self.trace_id)
        self.article.set("")
        self.lot.set("")
        self.trace_id = self.lot.trace_add(['write'], self.update_article_values)

    def create_widgets(self):
        """
        Create and arrange the widgets for the Settings view.
        """
        liste_ordre_fabrication = ControllerPesee.get_open_ordre_fabrication()
        liste_balance = ControllerPesee.get_balance_name_list()
        self.lot = tk.StringVar()
        self.trace_id = self.lot.trace_add(['write'], self.update_article_values)
        self.article = tk.StringVar()
        self.balance = tk.StringVar(value=liste_balance[0])
        self.poids = tk.IntVar()
        self.stability = tk.StringVar()
        self.connection = tk.StringVar()

        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame, height=400)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = tk.Label(self.frame1, text="Nouvelle Pesee", padx=1, pady=1)
        frame1_info_label.grid(row=0, column=0)


        #Lot
        frame1_lot_label = ctk.CTkLabel(self.frame1, text="Lot :",  padx=1, pady=1)
        frame1_lot_label.grid(row=1,column=0, sticky="w")
        frame1_lot_entry = ctk.CTkComboBox(self.frame1, width= 250, variable=self.lot, 
                                           values=[str(sublist[0]) for sublist in liste_ordre_fabrication])
        frame1_lot_entry.grid(row=1,column=1, sticky="w")
        #Article
        frame1_article_label = ctk.CTkLabel(self.frame1, text="Article :",  padx=1, pady=1)
        frame1_article_label.grid(row=2,column=0, sticky="w")
        self.frame1_article_entry = ctk.CTkComboBox(self.frame1, width= 250, variable=self.article)
        self.frame1_article_entry.grid(row=2,column=1, sticky="w")
        #Balance
        frame1_balance_label = ctk.CTkLabel(self.frame1, text="Balance :",  padx=1, pady=1)
        frame1_balance_label.grid(row=3,column=0, sticky="w")
        frame1_balance_entry = ctk.CTkComboBox(self.frame1, width= 250, variable=self.balance,
                                               values=liste_balance)
        frame1_balance_entry.grid(row=3, column=1, sticky='w')
        #Poids
        frame1_poids_label = ctk.CTkLabel(self.frame1, text="Poids :",  padx=1, pady=1)
        frame1_poids_label.grid(row=4,column=0, sticky="w")
        frame1_poids_entry = ctk.CTkEntry(self.frame1, textvariable=self.poids, width=250, state=tk.DISABLED)
        frame1_poids_entry.grid(row=4, column=1)
        frame1_stability = ctk.CTkLabel(self.frame1, textvariable=self.stability, padx=1, pady=1)
        frame1_stability.grid(row=4, column=2)
        frame1_connection = ctk.CTkLabel(self.frame1, textvariable=self.connection, padx=1, pady=1)
        frame1_connection.grid(row=4, column=3)
        #Button Valider la pesée
        frame1_pesee_button = ctk.CTkButton(self.frame1, text="Valider pesée", width=150,
                                            command=lambda : [self.controller.save_pesee(self.lot.get(),
                                                                                        self.article.get(),
                                                                                        self.poids.get(),
                                                                                        self.stability.get()),
                                                               self.clear_input()])
        frame1_pesee_button.grid(row=5, column=1)

        self.update_display()

