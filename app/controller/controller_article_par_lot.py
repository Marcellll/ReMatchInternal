from app.views.view_message_erreur import MessageErreur
from app.model.model_article import Article, FrontBack
from app.model.model_lot import Lot
from app.model.model_article_par_lot import ArticleParLot

class ControllerArticleParLot:
    def __init__(self, view):
        self.view = view

    def delete_article_in_lot(article_to_delete: str, lot: str):
        if article_to_delete == '':
            MessageErreur("Veuillez cliquer sur un article à supprimer")
            return
        id_lot = Lot.get_id_from_lot(lot)[0][0]
        id_article_to_delete = Article.get_id_article_from_description(article_to_delete)
        ArticleParLot.delete_article_par_lot(id_lot, id_article_to_delete)

    def get_article_par_lot(lot: str):
        id_lot = Lot.get_id_from_lot(lot)[0][0]
        return ArticleParLot.get_article_par_lot(id_lot)
    
    def get_all_article():
        return Article.get_article_front_back(FrontBack.Backend)
    
    def add_article(lot: str, article_to_add: str):
        id_lot = Lot.get_id_from_lot(lot)[0][0]
        id_article_to_add = Article.get_id_article_from_description(article_to_add)

        ArticleParLot.insert_new_article_par_lot(id_lot, id_article_to_add)