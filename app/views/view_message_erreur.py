import tkinter as tk
import customtkinter as ctk

class MessageErreur():
    def __init__(self, message_erreur: str):
            pop_erreur = ctk.CTkToplevel()
            pop_erreur.title("Erreur")
            pop_erreur.attributes("-topmost", True)
            message_erreur_label = ctk.CTkLabel(pop_erreur, text=message_erreur)
            message_erreur_label.pack(fill='both')