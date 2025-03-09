from app.views.view_message_erreur import MessageErreur
from app.model.model_chargement import Chargement, ChargementDechargement
from app.model.model_camion import Camion
from app.model.model_lot import Lot

class ControllerChargement:
    def __init__(self, view):
        self.view = view

    def get_all_chargement():
        return Chargement.get_all_open_chargement()
    
    def get_new_chargement():
        last_chargement = Chargement.get_all_open_chargement()
        if type(last_chargement) == int:
            return last_chargement + 1
        else:
            return 3000
    
    def create_new_chargement(numero_chargement, date_debut, date_fin, nombre_camion, lot, window):
        if date_debut == "" or date_fin == "":
            MessageErreur("La date de début et/ou de fin doit être renseigné")
            return
        
        id_lot = Lot.get_id_from_lot(lot)[0][0]        
        new_chargement = Chargement(date_debut=date_debut, date_fin=date_fin,
                                    id_lot=id_lot, numero_chargement=numero_chargement,
                                    chargement_dechargement=ChargementDechargement.Dechargement)
        Chargement.insert_new_chargement(nouveau_chargement=new_chargement)
        id_chargement = Chargement.get_id_from_numero(numero_chargement)
        for i in range(nombre_camion):
            new_camion = Camion(id_chargement=id_chargement, description=f"{i+1}/{nombre_camion}")
            Camion.insert_new_camion(new_camion=new_camion)
        window.destroy()

    def get_all_camion(numero_chargement: int):
        id_chargement = Chargement.get_id_from_numero(numero_chargement)
        return Camion.get_all_camion(id_chargement)
    
    def create_new_camion(numero_chargement: int, description: str):
        if description == "" or description == None:
            MessageErreur("Vous n'avez pas donné de description au nouveau camion")
            return
        try:
            id_chargement = Chargement.get_id_from_numero(numero_chargement)
        except:
            MessageErreur("Double-cliquez sur un chargement pour ajouter un camion")
            return

        new_camion = Camion(id_chargement=id_chargement, description=description)
        Camion.insert_new_camion(new_camion=new_camion)