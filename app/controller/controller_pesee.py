import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from app.model.model_lot import Lot
from app.model.model_article_par_lot import ArticleParLot
from app.model.model_ordre_fabrication import OrdreFabrication, StatusOF
from app.views.view_message_erreur import MessageErreur
from dateutil import parser

class ControllerPesee:
    def __init__(self, view):
        self.view = view

    def get_open_ordre_fabrication():
        return OrdreFabrication.get_open_ordre_fabrication()
    
    def get_article_par_lot(numero_lot):
        if numero_lot == "" or numero_lot == None:
            MessageErreur("Choissisez un lot pour choisir un article")
        id_lot = Lot.get_id_from_lot(numero_lot)
        return ArticleParLot.get_article_par_lot(id_lot)