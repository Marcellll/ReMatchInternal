import tkinter as tk
from tkinter import ttk
from app.model.model_lot import Lot
from app.model.model_article import Article, FrontBack
from app.model.model_ordre_fabrication import OrdreFabrication
from app.views.view_message_erreur import MessageErreur
from app.model.model_article_par_lot import ArticleParLot
from app.model.model_nomenclature import Nomenclature
import datetime

class ControllerLot:
    def __init__(self, view):
        self.view = view

    def populate_all_lot(treeview: ttk.Treeview):
        all_lot = Lot.get_all_batch()
        treeview.delete(*treeview.get_children())   
        for lot in all_lot:
            status = "Non crée" if lot[6] == None else lot[6]
            new_line = [lot[0], lot[3], lot[2], lot[4], lot[5], status]
            treeview.insert("", "end", values=new_line, tags=(f"{status}"))
    
    def get_front_end_article():
        return Article.get_article_front_back(FrontBack.Frontend)
    
    def get_new_batch_number():
        return Lot.get_last_batch()[0][0] + 1

    def create_new_batch(lot, description, article, window):
        nouveau_lot = Lot(id_article=article, lot=lot, date_modification=datetime.datetime.now().strftime("%Y-%m-%d"),
            heure_modification=datetime.datetime.now().strftime("%H:%M:%S"), description=description)
        Lot.insert_new_batch(nouveau_lot=nouveau_lot)
        window.destroy()

    def create_new_OF(lot: int, article: str):
        if lot == '':
            MessageErreur(f"Double cliquez sur une ligne de lot pour créer l'OF")
            return
        
        if article == 'None':
            MessageErreur("Attribuez un article au lot avant de créer l'OF")
            return
        
        id_lot = Lot.get_id_from_lot(lot)[0][0]
        id_article = Article.get_id_article_from_description(article=article)
                
        if OrdreFabrication.is_ordre_fabrication_present(id_lot):
            MessageErreur(f"L'ordre de fabrication existe déjà pour le lot: {lot}")
            return
        
        nomenclature = Nomenclature.get_nomenclature(id_article=id_article)
        for row in nomenclature:
            id_nomenclature = Article.get_id_article_from_description(row[3])
            ArticleParLot.insert_new_article_par_lot(id_lot=id_lot, id_article=id_nomenclature)
        OrdreFabrication.insert_new_ordre_fabrication(id_nouveau_lot=id_lot)
    
    def save_lot(lot: int, article: str, update_description: str):
        id_update_article = Article.get_id_article_from_description(article)
        id_update_lot = Lot.get_id_from_lot(lot)[0][0]
        update_lot = Lot(id=id_update_lot,
                         id_article=id_update_article,
                         date_modification=datetime.datetime.now().strftime("%Y-%m-%d"),
                         heure_modification=datetime.datetime.now().strftime("%H:%M:%S"),
                         description=update_description)
        
        if OrdreFabrication.is_ordre_fabrication_present(id_update_lot):
            MessageErreur(f"""L'ordre de fabrication pour le lot {lot} existe déjà.\n
                          Impossible de changer les caractéristiques du lot""")
            return
        
        Lot.update_information_lot(update_lot=update_lot)