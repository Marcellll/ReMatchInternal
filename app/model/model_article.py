from app.model.database_handler import return_dbconnection
import datetime
from enum import Enum

class FrontBack(Enum):
    Frontend = "Front end"
    Backend = "Back end"

class Article:
    """
    A generic model class representing the "Lot" table in a database.
    Attributes:
        ID (int): Primary key, stored as bigint.
        Numero_article (int): Number of the item, stored as bigint.
        Description_article (str): Description of the item, stored as text.
        Front/Back (FrontBack): Type of item, stored as text.
        Nomenclature (int): Foreign key containing the related items, stored as bigint.
    """

    def __init__(self,
                 id: int = None,
                 numero_article: int = None,
                 description_article: str = None,
                 front_back: str = None,
                 nomenclature: int = None,
                ):
        """
        Initialize a new Lot instance.

        Args:
            description (str): The description of the terrain (default: None).
            adresse (str): The address of the terrain (default: None).
            id (int): The unique identifier for the terrain (default: None).
        """
        self.id = id
        self.numero_article = numero_article
        self.description_article = description_article
        self.front_back = front_back
        self.nomenclature = nomenclature

    def get_article_front_back(front_back: FrontBack):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT A."ID", A."Description_article"
                            FROM public."Article" A
                            WHERE A."Front/Back" = '{front_back.value}'
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
    
    def get_id_article_from_description(article: str) -> int:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT "ID" FROM public."Article"
                            WHERE "Description_article" = '{article}'
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows[0][0]
