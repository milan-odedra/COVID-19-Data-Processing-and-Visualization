import tkinter as tk
import os
from PIL import Image, ImageTk

def button_click(button_label):
    print("Button", button_label, "pressed")

# Create a window
window = tk.Tk()
window.geometry("400x300")
window.title("Covid GUI")
window.configure(bg='#F8F8FF')

# Earth image
globe = Image.open("Icons/earth.png")
globe = globe.resize((25, 25))
globeIMG = ImageTk.PhotoImage(globe)

# Graph image
graph = Image.open("Icons/wave-graph.png")
graph = graph.resize((25, 25))
graphIMG = ImageTk.PhotoImage(graph)

# Statistics image
statc = Image.open("Icons/statistics.png")
statc = statc.resize((25, 25))
pstatIMG = ImageTk.PhotoImage(statc)

# Statistics image
statp = Image.open("Icons/pie-chart.png")
statp = statp.resize((25, 25))
cstatIMG = ImageTk.PhotoImage(statp)

# specify the path to the Python file you want to run
mapPath = "Code/Heatmap.py"


# Create buttons
button_a = tk.Button(window, font=('Arial', 16), bg='#F5F5F5', fg='#4B4B4B',text="Covid World heat-map ",image=globeIMG, compound=tk.RIGHT, command=lambda: os.system(f"python {mapPath}"))
button_b = tk.Button(window, font=('Arial', 16), bg='#F5F5F5', fg='#4B4B4B',text="Covid Graph - UK vs World ",image=graphIMG,compound=tk.RIGHT,command=lambda: button_click("B"))
button_c = tk.Button(window, font=('Arial', 16), bg='#F5F5F5', fg='#4B4B4B',text="Personal Covid Statistics ", image=pstatIMG, compound=tk.RIGHT, command=lambda: button_click("C"))
button_d = tk.Button(window, font=('Arial', 16), bg='#F5F5F5', fg='#4B4B4B',text="Country Covid Statistics ", image=cstatIMG, compound=tk.RIGHT, command=lambda: button_click("D"))
#button_e = tk.Button(window, font=('Arial', 16), bg='#F5F5F5', fg='#4B4B4B',text="E", command=lambda: button_click("E"))

# Add buttons to window
button_a.pack(pady=10)
button_b.pack(pady=10)
button_c.pack(pady=10)
button_d.pack(pady=10)
#button_e.pack(pady=10)

# Start the event loop
window.mainloop()
