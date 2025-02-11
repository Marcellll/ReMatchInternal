from customtkinter import CTk
from app.model.model_ordre_fabrication import OrdreFabrication

class ControllerPlanification:
    def __init__(self, view):
        self.view = view

    def get_ordered_batches():
        return OrdreFabrication.get_open_ordre_fabrication()