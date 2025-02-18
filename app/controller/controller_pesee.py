import tkinter as tk
from tkcalendar import *
from app.model.model_lot import Lot
from app.model.model_article_par_lot import ArticleParLot
from app.model.model_article import Article
from app.model.model_ordre_fabrication import OrdreFabrication
from app.model.model_pesee import Pesee
from app.views.view_message_erreur import MessageErreur
from utils.print_module import create_production_label
import threading
from enum import Enum
import time
import socket
import datetime

#Balance de production
#P - Imprimer le poids affiché (stable ou instable).
#IP - Imprimer immédiatement le poids affiché (stable ou instable).
#CP - Imprimer le poids en continu.
#SP - Imprimer le poids quand il est stable.
#Un espace est nécessaire dans chaque commande. Veuillez y prêter attention lors de la saisie des commandes.
# 12.0    kg ? Instable
# 68.5    kg Stable

# Scale configuration
#SCALE_IP = '192.168.1.182'
#SCALE_PORT = 9761  # Default port for Ohaus scales, check your manual


class Balance(Enum):
    BALANCE_1 = "192.168.1.181"
    BALANCE_2 = "192.168.1.183"
    BALANCE_3 = "192.168.1.180"
    BALANCE_4 = "192.168.1.184"
    BALANCE_5 = "192.168.1.182"

class ControllerPesee:
    def __init__(self, view, data_queue):
        self.view = view
        self.data_queue = data_queue

    def start_scales(self):
        for balance in [(balances.name, balances.value) for balances in Balance]:
            threading.Thread(target=self.read_scale, args=(balance[0], balance[1]),
                             daemon=True, name=balance[0]).start()
            
    def read_scale(self, scale_name, scale_ip):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((scale_ip, 9761)) 
            while True:
                data = s.recv(1024).decode('utf-8').strip().split()
                if len(data) > 2 and data[2] == '?':
                    self.data_queue.put((scale_name, int(float(data[0])), "Unstable"))
                    #print(self.data_queue.get())
                else:
                    self.data_queue.put((scale_name, int(float(data[0])), "Stable"))
                    #print(self.data_queue.get())
                time.sleep(0.5)

    def get_open_ordre_fabrication():
        return OrdreFabrication.get_open_ordre_fabrication()
    
    def get_article_par_lot(numero_lot):
        if numero_lot == "" or numero_lot == None:
            MessageErreur("Choissisez un lot pour choisir un article")
        id_lot = Lot.get_id_from_lot(numero_lot)[0][0]
        return ArticleParLot.get_article_par_lot(id_lot)
    

    def get_balance_name_list():
        return [member.name for member in Balance]
    
    def get_balance_ip_from_name(balance: str):
        return getattr(Balance, balance).value
    
    def save_pesee(self, lot: str, article: str,  poids: int, stability: str):
        if stability == "Unstable":
            MessageErreur("Balance instable attendez quelques instants")
            return
        if lot == "" or article == "" or poids == 0:
            MessageErreur("Lot, article ou poids pas renseigné")
            return
        Pesee.insert_new_pesee(OrdreFabrication.get_ordre_fabrication(id_lot = Lot.get_id_from_lot(lot)[0][0]),
                               Article.get_id_article_from_description(article),
                               poids)
        last_pesee = Pesee.get_last_pesee()
        create_production_label(datetime=datetime.datetime.combine(last_pesee[0][4], last_pesee[0][5]).strftime("%d/%m/%Y %H:%M"),
                                lot=last_pesee[0][0],
                                article_description=last_pesee[0][1],
                                poids=last_pesee[0][2],
                                numero_pesee=last_pesee[0][3])
    
