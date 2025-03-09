from app.model.database_handler import return_dbconnection
from enum import Enum
import datetime

class CamionPoids(Enum):
    ENTREE = 1
    SORTIE = 2
    NET = 3

class Camion:
    """
    A generic model class representing the "Camion" table in a database.
    Attributes:
    """

    def __init__(self,
                 id: int = None,
                 date_entree: datetime.date = None,
                 heure_entree: datetime.time = None,
                 poids_in: int = 0,
                 date_sortie: datetime.date = None,
                 heure_sortie: datetime.time = None,
                 poids_out: int = 0,
                 id_chargement: int = None,
                 poids_net: int = 0,
                 description: str = "",
                ):
        """
        Initialize a new Lot instance.

        Args:
            description (str): The description of the terrain (default: None).
            adresse (str): The address of the terrain (default: None).
            id (int): The unique identifier for the terrain (default: None).
        """

        self.id = id,
        self.date_entree = date_entree
        self.heure_entree = heure_entree
        self.poids_in = poids_in
        self.date_sortie = date_sortie
        self.heure_sortie = heure_sortie
        self.poids_out = poids_out
        self.id_chargement = id_chargement
        self.poids_net = poids_net
        self.description = description

    def insert_new_camion(new_camion: 'Camion'):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" INSERT INTO public."Camion" 
                            ("Date_entree", "Heure_entree", "Poids_in",
                             "Date_sortie", "Heure_sortie", "Poids_out",
                             "ID_Chargement", "Poids_net", "Description")
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)

                        """, (new_camion.date_entree, new_camion.heure_entree,
                              new_camion.poids_in, new_camion.date_sortie,
                              new_camion.heure_sortie, new_camion.poids_out,
                              new_camion.id_chargement, new_camion.poids_net,
                              new_camion.description))
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def update_poids(id_camion:int, poids: int, type: CamionPoids, numero_interne: int = 0):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        match type:
            case CamionPoids.ENTREE:
                cursor.execute(f""" UPDATE public."Camion" 
                                    SET "Date_entree" = '{datetime.datetime.now().strftime("%d/%m/%Y")}',
                                        "Heure_entree" = '{datetime.datetime.now().strftime("%H:%M:%S")}',
                                        "Poids_in" = '{poids}',
                                        "Numero_interne" = {numero_interne}
                                    WHERE "ID" = {id_camion}
                                """)
                dbconnection.commit()
                cursor.close()
                dbconnection.close()
            case CamionPoids.SORTIE:
                cursor.execute(f""" UPDATE public."Camion" 
                                    SET "Date_sortie" = '{datetime.datetime.now().strftime("%d/%m/%Y")}',
                                        "Heure_sortie" = '{datetime.datetime.now().strftime("%H:%M:%S")}',
                                        "Poids_out" = '{poids}'
                                    WHERE "ID" = {id_camion}
                                """)
                dbconnection.commit()
                cursor.close()
                dbconnection.close()
                Camion.update_poids(id_camion, poids, CamionPoids.NET)
            case CamionPoids.NET:
                cursor.execute(f""" UPDATE public."Camion" 
                                    SET "Poids_net" = '{Camion.get_net_weight(id_camion)}'
                                    WHERE "ID" = {id_camion}
                                """)
                dbconnection.commit()
                cursor.close()
                dbconnection.close()

    def get_net_weight(id_camion:int) -> int:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT ABS(C."Poids_out" - C."Poids_in") 
                            FROM public."Camion" C
                            WHERE C."ID" = {id_camion}
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows[0][0]
    
    def get_all_camion(id_chargement:int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT C."Description",
                                    C."Date_entree",
                                    C."Heure_entree",
                                    C."Date_sortie",
                                    C."Heure_sortie",
                                    C."Poids_in",
                                    C."Poids_out",
                                    C."Numero_interne"
                            FROM public."Camion" C
                            WHERE C."ID_Chargement" = {id_chargement}
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows

if __name__ == "__main__":
    pass
    #new_camion = Camion(id_chargement=4, description="1/1")
    #Camion.insert_new_camion(new_camion=new_camion)
    #Camion.update_poids(2, 25000, CamionPoids.SORTIE)