from app.model.database_handler import return_dbconnection
import datetime

class ArticleParLot:
    """
    A generic model class representing the "Lot" table in a database.
    Attributes:
        ID (int): Primary key, stored as bigint.
        ID_Lot (int): Foreign key to the lot table, stored as bigint.
        ID_Article (str): Foreign key to the article table, stored as bigint.
        Date_creation (datetime.date): Date at which it was added to the table, stored as date.
        Heure_creation (datetime.time): Time at which it was added to the table, stored as time without timezone.
    """

    def __init__(self,
                 id: int = None,
                 id_lot: int = None,
                 id_article: str = None,
                 date_creation: datetime.date = None,
                 heure_creation: datetime.time = None,
                ):
        """
        Initialize a new ArticleParLot instance.

        Args:
            
        """
        self.id = id
        self.id_lot = id_lot
        self.id_article = id_article
        self.date_creation = date_creation
        self.heure_creation = heure_creation

    def insert_new_article_par_lot(id_lot: int, id_article:int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" INSERT INTO public."Article_par_lot" 
                            ("ID_Lot", "ID_Article", "Date_creation", "Heure_creation")
                            VALUES (%s, %s, %s, %s)
                        """, (id_lot, id_article, 
                              datetime.datetime.now().strftime("%Y-%m-%d"),
                              datetime.datetime.now().strftime("%H:%M:%S")))
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def get_article_par_lot(id_lot: int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT A."Numero_article", A."Description_article" 
                            FROM public."Article_par_lot" APL
                            LEFT JOIN public."Article" A
                            ON APL."ID_Article" = A."ID"
                            WHERE APL."ID_Lot" = {id_lot}
                            """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
    
    def delete_article_par_lot(id_lot: int, id_article:int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" DELETE FROM public."Article_par_lot"
                            WHERE "ID_Lot" = {id_lot} AND 
                            "ID_Article" = {id_article}

                        """)
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

if __name__ == "__main__":
    pass