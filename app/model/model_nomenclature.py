from app.model.database_handler import return_dbconnection

class Nomenclature:
    """
    A generic model class representing the "Nomenclature" table in a database.
    Attributes:
        ID (int): Primary key, stored as bigint.
        ID_Article (int): Foreign key to the article table, stored as bigint.
        ID_Nomenclature (int): BOM number refering to the article table, stored as bigint.
    """

    def __init__(self,
                 id: int = None,
                 id_article: int = None,
                 id_nomenclature: int = None,
                ):
        """
        Initialize a new Nomenclature instance.

        Args:
            id (int): the primary key of the table (default: None).
            id_article (str): The article the bom refers to (default: None).
            id_nomenclature (int): The articles that are attached to main article (default: None).
        """
        self.id = id
        self.id_article = id_article
        self.id_nomenclature = id_nomenclature

    def get_nomenclature(id_article: int):
        """
        Returns the bom for a specific article under the following format:
        (id_article, description_article, bom_article_number, bom_article_description)

        Args:
            id_article (str): The article the bom refers to.
        """
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" select N."ID_Article",
                                A."Description_article",
                                AN."Numero_article",
                                AN."Description_article"
                                FROM public."Nomenclature" N
                                LEFT JOIN public."Article" A
                                ON N."ID_Article" = A."ID"
                                LEFT JOIN public."Article" AN
                                ON N."ID_Nomenclature" = AN."ID"
                                WHERE N."ID_Article" = {id_article}
                            """)
        rows = cursor.fetchall()
        dbconnection.close()
        return rows
    
    def insert_new_nomenclature(id_article: int, id_nomenclature: int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(""" INSERT INTO public."Nomenclature" 
                            ("ID_Article", "ID_Nomenclature")
                            VALUES (%s, %s)
                        """, (id_article, id_nomenclature))
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def delete_nomenclature(id_article: int, id_nomenclature: int):
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" DELETE FROM public."Nomenclature"
                            WHERE "ID_Article" = {id_article} AND 
                            "ID_Nomenclature" = {id_nomenclature}

                        """)
        dbconnection.commit()
        cursor.close()
        dbconnection.close()

    def is_article_present(id_article: int, id_nomenclature: int) -> bool:
        dbconnection = return_dbconnection()
        cursor = dbconnection.cursor()
        cursor.execute(f""" SELECT "ID" FROM public."Nomenclature"
                            WHERE "ID_Article" = {id_article} AND "ID_Nomenclature" = {id_nomenclature}   
                            """)
        rows = cursor.fetchall()
        if len(rows) != 0:
            dbconnection.close()
            return True
        else:
            dbconnection.close()
            return False

if __name__ == "__main__":
    pass
