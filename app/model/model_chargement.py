from app.model.database_handler import return_dbconnection
import datetime
from enum import Enum

class ChargementDechargement(Enum):
    Chargement = "Chargement"
    Dechargement = "Dechargement"

class ChargementStatus(Enum):
    OUVERT = "Ouvert"
    TERMINE = "Terminé"

class Chargement:
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
                 date_debut: datetime.date = None,
                 date_fin: datetime.date = None,
                 id_lot: int = None,
                 numero_chargement: int = None,
                 chargement_dechargement: ChargementDechargement = ChargementDechargement.Chargement,
                 client: str = "",
                 adresse_livraison: str = "",
                 status: ChargementStatus = ChargementStatus.OUVERT,
                ):
        """
        Initialize a new Lot instance.

        Args:
            description (str): The description of the terrain (default: None).
            adresse (str): The address of the terrain (default: None).
            id (int): The unique identifier for the terrain (default: None).
        """
        self.id = id
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.id_lot = id_lot
        self.numero_chargement = numero_chargement
        self.chargement_dechargement = chargement_dechargement
        self.client = client
        self.adresse_livraison = adresse_livraison
        self.status = status

    def insert_new_chargement(nouveau_chargement: 'Chargement'):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" INSERT INTO public."Chargement" 
                            ("Date_debut", "Date_fin", "ID_Lot", "Numero_chargement", "Chargement/Dechargement", "Client", "Adresse livraison", "Status")
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

                        """, (nouveau_chargement.date_debut, nouveau_chargement.date_fin,
                              nouveau_chargement.id_lot, nouveau_chargement.numero_chargement,
                              nouveau_chargement.chargement_dechargement.value, nouveau_chargement.client,
                              nouveau_chargement.adresse_livraison,
                              nouveau_chargement.status.value))
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def get_last_chargement() -> int:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" SELECT MAX(C."Numero_chargement") FROM public."Chargement" C
                           WHERE CAST(C."Numero_chargement" as Text) LIKE '3%'
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows[0][0]
    
    def is_chargement_present(id_lot:int) -> bool:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT C."ID_Lot"
                            FROM public."Chargement" as C 
                            WHERE C."ID_Lot" = '{id_lot}'
                        """)
        rows = cursor.fetchall()
        if len(rows) != 0:
            dbconnection.close()
            return True
        else:
            dbconnection.close()
            return False
        
    def get_all_open_chargement():
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f"""SELECT C."Numero_chargement", 
                                  C."Date_debut", 
                                  C."Date_fin", 
                                  C."Chargement/Dechargement",
                                  L."Lot"
                            FROM public."Chargement" C
                            LEFT JOIN public."Lot" L
                            ON C."ID_Lot" = L."ID"
                            WHERE C."Status" = '{ChargementStatus.OUVERT.value}'
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
    
    def get_id_from_numero(numero_chargement: int) -> int:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT C."ID" FROM public."Chargement" C
                           WHERE C."Numero_chargement" = {numero_chargement}
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows[0][0]

if __name__ == "__main__":
    print(Chargement.get_id_from_numero(3003))