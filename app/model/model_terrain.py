from app.model.database_handler import return_dbconnection

class Terrain:
    """
    A generic model class representing the "Terrain" table in a database.
    Attributes:
        Description (str): Description of the terrain, stored as text.
        Adresse (str): Address of the terrain, stored as text.
        Code_Postal (int): ZIP code of the terrain, stored as int.
        Ville (str): Village of the terrain, stored as text.
        Pays (str): Country of the terrain, stored as text.
        Lot (int): Batch of the terrain, stored as integer.
        Superficie (int): Surface of the terrain, stored as integer.
        Kg/m2 (float): Density of the terrains material, stored as real.
        HauteurFibre (int): Height of the terrains fibers, stored as integer.
        TypeRemplissage (str): Material type in the terrain, stored as text.
        CoucheSouplesse (bool): Presence of underterrain, stored as boolean.
        ID (int): Primary key, stored as bigint.
    """

    def __init__(self,
                description: str = None,
                adresse: str = None,
                code_postal: int = None,
                ville: str = None,
                pays: str = None,
                lot: int = None,
                superficie: int = None,
                kgm2: float = None,
                hauteur_fibre: int = None,
                type_remplissage: str = None,
                couche_souplesse: bool = False,
                id: int = None,):
        """
        Initialize a new Terrain instance.

        Args:
            description (str): The description of the terrain (default: None).
            adresse (str): The address of the terrain (default: None).
            id (int): The unique identifier for the terrain (default: None).
        """
        self.description = description
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays
        self.lot = lot
        self.superficie = superficie
        self.kgm2 = kgm2
        self.hauteur_fibre = hauteur_fibre
        self.type_remplissage = type_remplissage
        self.couche_souplesse = couche_souplesse
        self.id = id

    def __repr__(self):
        """
        String representation of the Terrain object for debugging and logging.
        """
        return f"""<Terrain(id={self.id}, 
                description='{self.description}', 
                adresse='{self.adresse}',
                code postal = '{self.code_postal}',
                ville = '{self.ville}',
                pays = '{self.pays}',
                lot = '{self.lot}',
                superficie = '{self.superficie}',
                kg/m2 = '{self.kgm2}',
                hauteur fibre = '{self.hauteur_fibre}',
                type de remplissage = '{self.type_remplissage}',
                couche de souplesse = '{self.couche_souplesse}'>"""
    
    def get_terrain(ID = None):
        #TODO: add the ID to the sql function
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" SELECT P."Lot", P."ID_Article_Terrain", 
		                            P."Status", P."Date_début", 
		                            P."Date_fin", T."Description", 
		                            T."Ville", T."Pays" 
                            FROM public."Planification" P
                            LEFT JOIN public."Terrain" T
                            ON P."ID_Terrain" = T."ID"
                        """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows

    
if __name__ == "__main__":
    dbconnection = return_dbconnection()
    print(Terrain.get_terrain(dbconnection))