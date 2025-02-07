import tkinter as tk
from tkinter import ttk

class Settings:
    def __init__(self, parent_frame):
        """
        Initialize the Settings view.
        :param parent_frame: The frame where the Settings view will be displayed.
        """
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange the widgets for the Settings view.
        """
        # Frame 1: Details of the current choosen batch
        self.frame1 = tk.Frame(self.parent_frame, bg="lightgray")
        self.frame1.grid(row=0, column=0, sticky="nwse", padx=2, pady=2)

        # Everything that goes into the first frame
        frame1_info_label = tk.Label(self.frame1, text="Information Settings", font=("Verdana",16), padx=1, pady=1)
        frame1_info_label.grid(row=0, column=0)