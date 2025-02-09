from app.model.database_handler import return_dbconnection
import datetime

class Lot:
    """
    A generic model class representing the "Lot" table in a database.
    Attributes:
        ID (int): Primary key, stored as bigint.
        ID_Article (int): Foreign key to the article table, stored as bigint.
        Lot (int): Batch number, stored as bigint.
        Date_modification (date): Date of the last modifcation of the entry, stored as date.
        Heure_modification (time): Time of the last modification of the entry, stored as time.
        Description (str): Description of the batch number, sotred as text.
    """

    def __init__(self,
                 id: int = None,
                 id_article: int = None,
                 lot: int = None,
                 date_modification: datetime.date = None,
                 heure_modification: datetime.time = None,
                 description: str = None,
                ):
        """
        Initialize a new Lot instance.

        Args:
            description (str): The description of the terrain (default: None).
            adresse (str): The address of the terrain (default: None).
            id (int): The unique identifier for the terrain (default: None).
        """
        self.id = id
        self.article = id_article
        self.lot = lot
        self.date_modification = date_modification
        self.heure_modification = heure_modification
        self.description = description

    def get_all_batch():
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" SELECT L."Lot",
                                  L."ID_Article",
                                  A."Description_article",
                                  L."Description",
                                  L."Date_modification",
                                  L."Heure_modification"
                            FROM public."Lot" L
                            LEFT JOIN public."Article" A
                            ON L."ID_Article" = A."ID"
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows

    
if __name__ == "__main__":
    print(Lot.get_all_batch())
        
