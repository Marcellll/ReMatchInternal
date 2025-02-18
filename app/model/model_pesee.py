from app.model.database_handler import return_dbconnection
from enum import Enum
import datetime

class StatusPesee(Enum):
    CREE = "Crée"
    SUPPRIME = "Supprimé"
    RERUN = "Re-run"
    REMPLACE = "Remplacé"

class Pesee:
    """
    A generic model class representing the "Pesee_production" table in a database.
    Attributes:
        ID (int): Primary key, stored as bigint.
        ID_ordre_fabrication (int): Foreign key to the ordre_fabrication table, stored as bigint.
        Poids (int): weight of the big bag, stored as bigint.
        ID_Article (int): Foreign key to the article table, stored as bigint.
        Date_creation (datetime.date): Date at which the big bag was weighted, stored as date.
        Heure_creation (datetime.time): Time at which the big bag was weighted, stored as time.
        Status (StatusPesee): Status of the weight, stored as text.
    """

    def __init__(self,
                 id: int = None,
                 id_ordre_fabrication: int = None,
                 poids: int = None,
                 id_article: int = None,
                 date_creation: datetime.date = datetime.datetime.now().strftime("%Y-%m-%d"),
                 heure_creation: datetime.time = datetime.datetime.now().strftime("%H:%M:%S"),
                 status: StatusPesee = None,
                 numero_pesee: int = None
                ):
        """
        Initialize a new Pesee instance.

        Args:
            
        """
        self.id = id
        self.id_ordre_fabrication = id_ordre_fabrication
        self.poids = poids
        self.id_article = id_article
        self.date_creation = date_creation
        self.heure_creation = heure_creation
        self.status = status
        self.numero_pesee = numero_pesee

    def insert_new_pesee(id_ordre_fabrication:int, id_article:int, poids:int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" INSERT INTO public."Pesee_production" 
                            ("ID_ordre_fabrication", "ID_article", "Poids", "Date_creation", "Heure_creation", "Status", "Numero_pesee")
                            VALUES ({id_ordre_fabrication}, {id_article}, {poids}, '{datetime.datetime.now().strftime("%Y-%m-%d")}',
                             '{datetime.datetime.now().strftime("%H:%M:%S")}', '{StatusPesee.CREE.value}', {Pesee.get_nouveau_numero_pesee()})
                        """)
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def update_status_pesee(numero_pesee:int, nouveau_status:StatusPesee):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" UPDATE public."Pesee_production" 
                            SET "Status" = '{nouveau_status.value}'
                            WHERE "Numero_pesee"={numero_pesee}
                        """)
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def get_nouveau_numero_pesee() -> int:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT MAX("Numero_pesee") FROM public."Pesee_production" """) 
        maxvalue = cursor.fetchall()
        dbconnection.close()
        return maxvalue[0][0] + 1
    
    def get_last_pesee():
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT L."Lot", 
                            A."Description_article", 
                            P."Poids", 
                            P."Numero_pesee", 
                            P."Date_creation", 
                            P."Heure_creation"
                            FROM public."Pesee_production" P
                            LEFT JOIN public."Ordre_fabrication" OF
                            ON P."ID_ordre_fabrication" = OF."ID"
                            left join public."Lot" L
                            ON OF."ID_Lot" = L."ID"
                            LEFT JOIN public."Article" A
                            ON P."ID_article" = A."ID"
                            ORDER BY P."Numero_pesee" DESC LIMIT 1
                        """) 
        rows = cursor.fetchall()
        dbconnection.close()
        return rows

if __name__ == "__main__":
    print(Pesee.get_last_pesee()[0][3])