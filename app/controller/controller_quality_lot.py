import tkinter as tk
from tkinter import ttk
from app.model.model_lot import Lot
from app.model.model_article import Article, FrontBack

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