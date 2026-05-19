import tkinter as tk
from gui import SortingVisualizerGUI

def main():
    root = tk.Tk()
    app = SortingVisualizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()