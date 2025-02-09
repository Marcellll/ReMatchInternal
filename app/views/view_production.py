import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Production:
    def __init__(self, parent_frame):
        """
        Initialize the Production view.
        :param parent_frame: The frame where the Production overview will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange the widgets for the Production view.
        """
        # Frame 1: Details of the current choosen batch
        self.frame1 = ctk.CTkFrame(self.parent_frame)
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = ctk.CTkLabel(self.frame1, text="Information Production", padx=1, pady=1)
        frame1_info_label.grid(row=0, column=0)