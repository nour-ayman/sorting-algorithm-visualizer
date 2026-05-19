import tkinter as tk
from tkinter import ttk
import random
from algorithms import bubble_sort_visual, selection_sort_visual, insertion_sort_visual, merge_sort_visual, quick_sort_visual

#====================================================================
# Haneen's Task: GUI Design and Integration
#====================================================================

class SortingVisualizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry("900x600")
        self.root.config(bg="#2D2D2D")

        # Variables
        self.data = []
        
        # 1. Canvas Frame
        self.canvas = tk.Canvas(self.root, width=880, height=400, bg="#1E1E1E", highlightthickness=0)
        self.canvas.pack(pady=10)

        # 2. Control Panel Frame
        self.control_frame = tk.Frame(self.root, bg="#2D2D2D")
        self.control_frame.pack(pady=10, fill=tk.X, padx=20)

        self._build_controls()
        self.generate_array()

    def _build_controls(self):
        # Dropdown menu lel Algorithms
        tk.Label(self.control_frame, text="Algorithm:", fg="white", bg="#2D2D2D", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.algo_menu = ttk.Combobox(self.control_frame, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"], state="readonly", width=15)
        self.algo_menu.pack(side=tk.LEFT, padx=5)
        self.algo_menu.set("Quick Sort")

        # Slider lel Speed / Delay
        tk.Label(self.control_frame, text="Delay (s):", fg="white", bg="#2D2D2D", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.speed_slider = tk.Scale(self.control_frame, from_=0.001, to=0.5, resolution=0.001, orient=tk.HORIZONTAL, bg="#2D2D2D", fg="white", highlightthickness=0, width=10)
        self.speed_slider.pack(side=tk.LEFT, padx=5)
        self.speed_slider.set(0.05)

        # Buttons
        self.btn_gen = tk.Button(self.control_frame, text="Generate Array", command=self.generate_array, bg="#4A4A4A", fg="white", font=("Arial", 11, "bold"), relief=tk.FLAT)
        self.btn_gen.pack(side=tk.LEFT, padx=15)

        self.btn_start = tk.Button(self.control_frame, text="START", command=self.start_sorting, bg="#27AE60", fg="white", font=("Arial", 11, "bold"), relief=tk.FLAT)
        self.btn_start.pack(side=tk.LEFT, padx=5)

    def generate_array(self):
        """ Ben-generate array random we n-resmha """
        # 80 bars widths mtzabateen m3a el Canvas size
        self.data = [random.randint(10, 380) for _ in range(80)]
        self.update_screen(self.data)
        self._toggle_buttons(state=tk.NORMAL)

    def update_screen(self, current_array, color_map=None):
        """ El function elly b-redraw el Canvas """
        self.canvas.delete("all")
        c_height = 400
        c_width = 880
        bar_width = c_width / len(current_array)
        
        for i, val in enumerate(current_array):
            x0 = i * bar_width
            y0 = c_height - val
            x1 = (i + 1) * bar_width
            y1 = c_height
            
            color = "#3498DB" # Default Blue
            if color_map and i in color_map:
                if color_map[i] == "red": color = "#E74C3C"      # Pivot / Hard target
                elif color_map[i] == "yellow": color = "#F1C40F"  # Comparing
                elif color_map[i] == "green": color = "#2ECC71"   # Sorted / Swapped
                elif color_map[i] == "purple": color = "#9B59B6"  # Range context
                
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#1E1E1E")
        
        self.root.update_idletasks()

    def _toggle_buttons(self, state):
        """ 3ashan el user may-doossh generate f-nos el sorting """
        self.btn_gen.config(state=state)
        self.btn_start.config(state=state)

    def start_sorting(self):
        self._toggle_buttons(state=tk.DISABLED)
        algo = self.algo_menu.get()
        delay = self.speed_slider.get()

        if algo == "Bubble Sort":
            bubble_sort_visual(self.data, self.update_screen, delay)
        elif algo == "Selection Sort":
            selection_sort_visual(self.data, self.update_screen, delay)
        elif algo == "Insertion Sort":
            insertion_sort_visual(self.data, self.update_screen, delay)
        elif algo == "Merge Sort":
            merge_sort_visual(self.data, self.update_screen, delay)
        elif algo == "Quick Sort":
            quick_sort_visual(self.data, self.update_screen, delay)
            
        self._toggle_buttons(state=tk.NORMAL)