from database_handler import return_dbconnection
from enum import Enum
import datetime

class StatusOF(Enum):
    CREE= "Crée"
    PLANIFIE = "Planifié"
    TERMINE = "Terminé"

class OrdreFabrication:
    """
    A generic model class representing the "Ordre_fabrication" table in a database.
    Attributes:
        ID (int): Primary key, stored as bigint.
        ID_Lot (int): Foreign key to the Lot table, stored as bigint.
        Date_debut (date): Date of beginning the batch, stored as date.
        Date_fin (date): Date of finishing, stored as date.
        Status_OF (StatusOF): Status of the fabrication order, stored as str.
        Ordre_planification (int): Internal number to know in which order they will be processed, sotred as int.
    """

    def __init__(self,
                 id: int = None,
                 id_lot: int = None,
                 date_debut: datetime.date = None,
                 date_fin: datetime.date = None,
                 status_OF: StatusOF = None,
                ):
        """
        Initialize a new OrdreFabrication instance.

        Args:
            description (str): The description of the terrain (default: None).
            adresse (str): The address of the terrain (default: None).
            id (int): The unique identifier for the terrain (default: None).
        """
        self.id = id
        self.lot = id_lot
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.status_OF = status_OF

    def is_ordre_fabrication_present(id_lot:int) -> bool:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT OF."ID_Lot"
                            FROM public."Ordre_fabrication" as OF 
                            WHERE OF."ID_Lot" = '{id_lot}'
                        """)
        rows = cursor.fetchall()
        if len(rows) != 0:
            dbconnection.close()
            return True
        else:
            dbconnection.close()
            return False
        
    def insert_new_ordre_fabrication(id_nouveau_lot: int, date_debut: datetime.date = None, date_fin: datetime.date = None):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" INSERT INTO public."Ordre_fabrication" 
                            ("ID_Lot", "Date_debut", "Date_fin", "Status_OF")
                            VALUES (%s, %s, %s, %s)
                        """, (id_nouveau_lot, date_debut, date_fin, StatusOF.CREE.value))
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def update_status_ordre(nouveau_status: StatusOF, id_lot: int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" UPDATE public."Ordre_fabrication" 
                            SET "Status_OF" = '{nouveau_status.value}'
                            WHERE "ID_Lot"={id_lot}
                        """)
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def update_date(date_debut: datetime.date, date_fin: datetime.date, id_lot: int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" UPDATE public."Ordre_fabrication" 
                            SET "Date_debut" = '{date_debut}',
                                "Date_fin" = '{date_fin}'
                            WHERE "ID_Lot"={id_lot}
                        """)
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def get_ordre_fabrication(status_of: StatusOF = None):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT L."Lot",
                                    A."Description_article",
                                    OF."Status_OF",
                                    OF."Date_debut",
                                    OF."Date_fin",
                                    L."Description"
                            FROM public."Ordre_fabrication" as OF
                            LEFT JOIN public."Lot" L
                                ON OF."ID_Lot" = L."ID"
                            LEFT JOIN public."Article" A
                                ON L."ID_Article" = A."ID"
                            WHERE OF."Status_OF" like '{status_of.value if status_of != None else "" }%'
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
    
    def get_open_ordre_fabrication():
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT L."Lot",
                                    A."Description_article",
                                    OF."Status_OF",
                                    OF."Date_debut",
                                    OF."Date_fin",
                                    L."Description",
                                    OF."ID"
                            FROM public."Ordre_fabrication" as OF
                            LEFT JOIN public."Lot" L
                                ON OF."ID_Lot" = L."ID"
                            LEFT JOIN public."Article" A
                                ON L."ID_Article" = A."ID"
                            WHERE OF."Status_OF" = '{StatusOF.PLANIFIE.value}'
                            ORDER BY OF."Date_debut" ASC
                        """) 
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
    
    def get_batch_to_work_on():
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT L."Lot",
                                    A."Description_article",
                                    OF."Status_OF",
                                    OF."Date_debut",
                                    OF."Date_fin",
                                    L."Description"
                            FROM public."Ordre_fabrication" OF
                            LEFT JOIN public."Lot" L
                            ON L."ID" = OF."ID_Lot" 
                            LEFT JOIN public."Article" A
                            ON L."ID_Article" = A."ID"
                            WHERE OF."Status_OF" <> '{StatusOF.PLANIFIE.value}'
                            ORDER BY L."Lot" DESC
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
        
if __name__=="__main__":
    print(OrdreFabrication.get_open_ordre_fabrication())