import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from app.model.model_article import Article, FrontBack
from app.model.model_nomenclature import Nomenclature
from app.views.view_message_erreur import MessageErreur

class ControllerNomenclature:
    def __init__(self, view):
        self.view = view

    def get_front_end_article():
        return Article.get_article_front_back(FrontBack.Frontend)
    
    def get_article_bom(article_description: str):
        id_article = Article.get_id_article_from_description(article=article_description)
        return Nomenclature.get_nomenclature(id_article=id_article)
    
    def get_back_end_article():
        return Article.get_article_front_back(FrontBack.Backend)
    
    def delete_article_in_bom(front_end_article:str, article_to_delete: str):
        if front_end_article == '':
            MessageErreur("""Choissisez un article dans la liste déroulante puis \n
                          sélectionnez un article à supprimer""")
            return
        
        if article_to_delete == '':
            MessageErreur("Veuillez cliquer sur un article à supprimer")
            return
        
        id_article_front_end = Article.get_id_article_from_description(front_end_article)
        id_article_to_delete = Article.get_id_article_from_description(article_to_delete)

        Nomenclature.delete_nomenclature(id_article_front_end, id_article_to_delete)

    def add_new_article_to_bom(front_end_article: str, article_to_add: str):
        if article_to_add == "":
            MessageErreur("Choissisez un article dans la liste déroulante")
            return
        
        id_front_end_article = Article.get_id_article_from_description(article=front_end_article)
        id_article_to_add = Article.get_id_article_from_description(article=article_to_add)

        if not(Nomenclature.is_article_present(id_article=id_front_end_article, id_nomenclature=id_article_to_add)):
            Nomenclature.insert_new_nomenclature(id_article=id_front_end_article, id_nomenclature=id_article_to_add)
        else:
            MessageErreur("L'article est déjà présent dans la nomenclature")
            
        
