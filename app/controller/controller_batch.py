import tkinter as tk
from tkinter import ttk
from app.model.model_terrain import Terrain

class ControllerBatch:
    def __init__(self, view):
        self.view = view

    def populate_all_batchs(treeview: ttk.Treeview):
        all_terrain = Terrain.get_terrain()        
        for item in all_terrain:
             treeview.insert("", "end", values=item)
