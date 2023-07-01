import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="Project Management System",
            themename="journal",
            size=(700, 600),
            resizable=(True, False),
        )
        # configure grid layout (2x1)
        # ============ create top frames ============
        top_frame = ttk.Frame(master=self,height=50 , bootstyle="secondary")
        top_frame.pack(side="top" , fill="x" ,anchor="center")
        ttk.Label(top_frame,text= "Project Management System" ,borderwidth=2, bootstyle="inverse-secondary").pack(side="top")
        left_frame = ttk.Frame(master=self,width=150 , bootstyle="info")
        left_frame.pack(side="left" , fill="y" ,anchor="w")
        self.right_frame = ttk.Frame(master=self, bootstyle="light")
        self.right_frame.pack( fill="both" ,expand=True ,side="right")
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()