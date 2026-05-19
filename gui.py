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
        self.root.geometry("1100x700")
        self.root.config(bg="#2D2D2D")

        # Variables
        self.data = []
        self.is_sorting = False  # Anti-double click check
        
        # 1. Canvas Frame
        self.canvas = tk.Canvas(self.root, width=1060, height=450, bg="#1E1E1E", highlightthickness=0)
        self.canvas.pack(pady=10)

        # 2. Control Panel Frame
        self.control_frame = tk.Frame(self.root, bg="#2D2D2D")
        self.control_frame.pack(pady=10, fill=tk.X, padx=20)

        self._build_controls()
        self._build_legend()
        self.generate_array()

    def _build_controls(self):
        # Dropdown menu lel Algorithms
        tk.Label(self.control_frame, text="Algorithm:", fg="white", bg="#2D2D2D", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        self.algo_menu = ttk.Combobox(self.control_frame, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"], state="readonly", width=14)
        self.algo_menu.pack(side=tk.LEFT, padx=5)
        self.algo_menu.set("Quick Sort")

        # Slider lel Array Size (Features mn code 2)
        tk.Label(self.control_frame, text="Size:", fg="white", bg="#2D2D2D", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        self.size_slider = tk.Scale(self.control_frame, from_=10, to=120, orient=tk.HORIZONTAL, bg="#2D2D2D", fg="white", highlightthickness=0, width=10, length=120)
        self.size_slider.pack(side=tk.LEFT, padx=5)
        self.size_slider.set(60)

        # Slider lel Speed / Delay
        tk.Label(self.control_frame, text="Delay (s):", fg="white", bg="#2D2D2D", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        self.speed_slider = tk.Scale(self.control_frame, from_=0.001, to=0.5, resolution=0.001, orient=tk.HORIZONTAL, bg="#2D2D2D", fg="white", highlightthickness=0, width=10, length=120)
        self.speed_slider.pack(side=tk.LEFT, padx=5)
        self.speed_slider.set(0.02)

        # Buttons (Custom Padding & Colors)
        self.btn_gen = tk.Button(self.control_frame, text="Generate", command=self.generate_array, bg="#4A4A4A", fg="white", font=("Arial", 10, "bold"), relief=tk.FLAT, width=10)
        self.btn_gen.pack(side=tk.LEFT, padx=10)

        self.btn_start = tk.Button(self.control_frame, text="START", command=self.start_sorting, bg="#27AE60", fg="white", font=("Arial", 10, "bold"), relief=tk.FLAT, width=10)
        self.btn_start.pack(side=tk.LEFT, padx=5)

    def _build_legend(self):
        """ Legend Framework mn code 2 3ashan t-bayan ma3na el alwan """
        legend_frame = tk.Frame(self.root, bg="#2D2D2D")
        legend_frame.pack(pady=5)

        tk.Label(legend_frame, text="■ Unsorted / Context", fg="#3498DB", bg="#2D2D2D", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=15)
        tk.Label(legend_frame, text="■ Active Comparison", fg="#F1C40F", bg="#2D2D2D", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=15)
        tk.Label(legend_frame, text="■ Swap / Current Target", fg="#E74C3C", bg="#2D2D2D", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=15)
        tk.Label(legend_frame, text="■ Sorted Block", fg="#2ECC71", bg="#2D2D2D", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=15)

    def generate_array(self):
        size = self.size_slider.get()
        # Generate generic numbers inside the dynamic scale range
        self.data = [random.randint(10, 430) for _ in range(size)]
        self.update_screen(self.data)
        self._toggle_buttons(state=tk.NORMAL)

    def update_screen(self, current_array, color_map=None):
        self.canvas.delete("all")
        c_height = 450
        c_width = 1060
        bar_width = c_width / len(current_array)
        
        # Safe Normalization check line to prevent division by zero
        max_val = max(current_array) if len(current_array) > 0 else 1
        
        for i, val in enumerate(current_array):
            # Normalization algorithm implementation from code 2
            normalized_height = (val / max_val) * 420
            
            x0 = i * bar_width + 2
            y0 = c_height - normalized_height
            x1 = (i + 1) * bar_width
            y1 = c_height
            
            color = "#3498DB" # Default Blue
            if color_map and i in color_map:
                if color_map[i] == "red": color = "#E74C3C"
                elif color_map[i] == "yellow": color = "#F1C40F"
                elif color_map[i] == "green": color = "#2ECC71"
                elif color_map[i] == "purple": color = "#9B59B6"
                
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        
        self.root.update_idletasks()

    def _toggle_buttons(self, state):
        self.btn_gen.config(state=state)
        self.btn_start.config(state=state)
        self.size_slider.config(state=state)

    def start_sorting(self):
        if self.is_sorting:
            return
        self.is_sorting = True
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
        self.is_sorting = False