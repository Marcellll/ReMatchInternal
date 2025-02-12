from tkcalendar import *
import tkinter as tk
import customtkinter as ctk

class ViewCalendrier():
    def __init__(self, date: tk.StringVar):
        date_window = ctk.CTkToplevel()
        date_window.grab_set()
        date_window.title("Choix date")
        date_window.attributes("-topmost", True)
        date_window.geometry("300x175+500+400")
        cal = Calendar(date_window, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack(fill='both')
        valider_button = ctk.CTkButton(date_window, text="Valider", command= lambda: [date.set(cal.get_date()), date_window.destroy()])
        valider_button.pack(fill='x')