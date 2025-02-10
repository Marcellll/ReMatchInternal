import tkinter as tk
from tkinter import ttk
from app.model.model_lot import Lot
from app.model.model_article import Article, FrontBack
import datetime

class ControllerLot:
    def __init__(self, view):
        self.view = view

    def populate_all_lot(treeview: ttk.Treeview):
        all_lot = Lot.get_all_batch()     
        for lot in all_lot:
             new_line = [lot[0], lot[3], lot[2], lot[4], lot[5]]
             treeview.insert("", "end", values=new_line)
    
    def get_front_end_article():
        return Article.get_article_front_back(FrontBack.Frontend)
    
    def get_new_batch_number():
        return Lot.get_last_batch()[0][0] + 1

    def create_new_batch(lot, description, article, window):
        nouveau_lot = Lot(id_article=article, lot=lot, date_modification=datetime.datetime.now().strftime("%Y-%m-%d"),
            heure_modification=datetime.datetime.now().strftime("%H:%M:%S"), description=description)
        Lot.insert_new_batch(nouveau_lot=nouveau_lot)
        window.destroy()

    def create_new_OF():
        pass

    