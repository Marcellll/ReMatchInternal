import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from app.model.model_lot import Lot
from app.model.model_ordre_fabrication import OrdreFabrication, StatusOF
from app.views.view_message_erreur import MessageErreur
from dateutil import parser

class ControllerPlanification:
    def __init__(self, view):
        self.view = view

    def get_ordered_batches():
        return OrdreFabrication.get_open_ordre_fabrication()
    
    def populate_all_ordre_to_work_on(treeview: ttk.Treeview):
        open_ordre = OrdreFabrication.get_batch_to_work_on()
        treeview.delete(*treeview.get_children())   
        for ordre in open_ordre:
            new_line = [ordre[0], ordre[1], ordre[2], ordre[3], ordre[4], ordre[5]]
            treeview.insert("", "end", values=new_line, tags=(f"{ordre[2]}"))

    def populate_ordre_to_be_worked_on(treeview: ttk.Treeview):
        open_ordre = OrdreFabrication.get_open_ordre_fabrication()
        treeview.delete(*treeview.get_children())   
        for ordre in open_ordre:
            new_line = [ordre[0], ordre[1], ordre[2], ordre[3], ordre[4], ordre[5]]
            treeview.insert("", "end", values=new_line, tags=(f"{ordre[2]}"))

    def update_date(lot: str, date_debut: str, date_fin: str) -> int:
        if lot == "":
            MessageErreur("""Double cliquez sur une ligne d'ordre de fabrication \n
                          pour modifier les dates""")
            return
        
        id_lot = Lot.get_id_from_lot(lot=lot)[0][0]
        if date_debut == "" or date_fin=="" or date_debut == "None" or date_fin=="None":
            MessageErreur("Il manque la date de début ou de fin")
            return -1
        date_debut = parser.parse(date_debut)
        date_fin = parser.parse(date_fin)

        OrdreFabrication.update_date(id_lot=id_lot, date_debut=date_debut, date_fin=date_fin)
        return 0

    def set_ordre_planifie(lot: str):
        if lot == "":
            MessageErreur("""Aucun lot choisi""")
            return
        id_lot = Lot.get_id_from_lot(lot=lot)[0][0]
        OrdreFabrication.update_status_ordre(id_lot=id_lot, nouveau_status=StatusOF.PLANIFIE)

    def planifie_ordre(lot: str, date_debut: str, date_fin: str):
        if ControllerPlanification.update_date(lot=lot, date_debut=date_debut, date_fin=date_fin) == 0:
            ControllerPlanification.set_ordre_planifie(lot=lot)

    def finish_ordre(lot: str):
        if lot == "":
            MessageErreur("""Aucun lot choisi""")
            return
        id_lot = Lot.get_id_from_lot(lot=lot)[0][0]
        OrdreFabrication.update_status_ordre(id_lot=id_lot, nouveau_status=StatusOF.TERMINE)