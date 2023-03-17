import tkinter as tk
import os
from PIL import Image, ImageTk

def button_click(button_label):
    print("Button", button_label, "pressed")

# Create a window
window = tk.Tk()
window.geometry("800x800")
window.title("Covid GUI")

# Earth image
globe = Image.open("Icons/earth.png")
globe = globe.resize((20, 20))
globeIMG = ImageTk.PhotoImage(globe)

# Earth image
graph = Image.open("Icons/wave-graph.png")
graph = graph.resize((20, 20))
graphIMG = ImageTk.PhotoImage(graph)

# specify the path to the Python file you want to run
mapPath = "Code/visual.py"


# Create buttons
button_a = tk.Button(window, text="Covid World heat-map",image=globeIMG, compound=tk.RIGHT, command=lambda: os.system(f"python {mapPath}"))
button_b = tk.Button(window, text="Covid KPIs - UK vs World",image=graphIMG,compound=tk.RIGHT,command=lambda: button_click("B"))
button_c = tk.Button(window, text="C", command=lambda: button_click("C"))
button_d = tk.Button(window, text="D", command=lambda: button_click("D"))
button_e = tk.Button(window, text="E", command=lambda: button_click("E"))

# Add buttons to window
button_a.pack(side="left", padx=20)
button_b.pack(side="left", padx=20)
button_c.pack(side="left", padx=20)
button_d.pack(side="left", padx=20)
button_e.pack(side="left", padx=20)

# Start the event loop
window.mainloop()
