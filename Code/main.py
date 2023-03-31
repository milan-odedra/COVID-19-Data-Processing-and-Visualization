import customtkinter
from PIL import Image
import os
import pandas as pd
 

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.title("Homepage for Team 6's Covid-19 Analysis")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Earth image
        globe = Image.open("Icons/earth.png")
        globe = globe.resize((25, 25))
        globeIMG = customtkinter.CTkImage(globe)

        # Graph image
        graph = Image.open("Icons/wave-graph.png")
        graph = graph.resize((25, 25))
        graphIMG = customtkinter.CTkImage(graph)

        # Statistics image
        statc = Image.open("Icons/statistics.png")
        statc = statc.resize((25, 25))
        pstatIMG = customtkinter.CTkImage(statc)

        # Statistics image
        statp = Image.open("Icons/pie-chart.png")
        statp = statp.resize((25, 25))
        cstatIMG = customtkinter.CTkImage(statp)

        # Specify the path to the Python file you want to run
        mapPath = "Code/heatmap.py"
        WHOpath = "Code/lineGraph.py"

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.sidebar_frame_A = customtkinter.CTkButton(self.sidebar_frame,text="Everybody look at this amazing GUI! It deserves 100%")
        self.sidebar_frame_A.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_frame_B = customtkinter.CTkButton(self.sidebar_frame, text="Yep, this is a 100% no doubt")
        self.sidebar_frame_B.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_frame_C = customtkinter.CTkButton(self.sidebar_frame, text="I don't really like this")
        self.sidebar_frame_C.grid(row=3, column=0, padx=20, pady=10)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Team 6 Data Analysis", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Dataframe for textbox
        dframe = pd.read_csv('Data\\country_wise_latest.csv', sep=",").iloc[:,:3]

        # Create Textbox
        self.Textbox = customtkinter.CTkTextbox(self, width=250)
        self.Textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        

        # Create checkbox and switch frame
        self.function_buttons_grid = customtkinter.CTkFrame(self)
        self.function_buttons_grid.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.sidebar_label = customtkinter.CTkLabel(self.function_buttons_grid,text="Our functionalities", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_label.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_A = customtkinter.CTkButton(self.function_buttons_grid,text="Covid World heat-map ",image=globeIMG, compound=customtkinter.RIGHT, command=lambda: os.system(f"python {mapPath}"))
        self.sidebar_button_A.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_B = customtkinter.CTkButton(self.function_buttons_grid, text="Covid Graph - UK vs World ",image=graphIMG,compound=customtkinter.RIGHT,command=lambda: os.system(f"python {WHOpath}"))
        self.sidebar_button_B.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_C = customtkinter.CTkButton(self.function_buttons_grid, text="Personal Covid Statistics ", image=pstatIMG, compound=customtkinter.RIGHT,command=lambda: self.button_click("B"))
        self.sidebar_button_C.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_D = customtkinter.CTkButton(self.function_buttons_grid, text="Country Covid Statistics ", image=cstatIMG, compound=customtkinter.RIGHT,command=lambda: self.button_click("C"))
        self.sidebar_button_D.grid(row=5, column=0, padx=20, pady=10)

        # Set default values
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")
        self.sidebar_frame_C.configure(state="disabled")
        self.Textbox.insert("0.0", text=f"This is out data. Feel free to scroll through \n {dframe.to_string()}")
       

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def button_click(self,button_label):
        print("Button", button_label, "pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()