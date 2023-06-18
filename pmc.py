import ttkbootstrap as ttk


class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="Project Management System",
            themename="flatly",
            size=(900, 700),
            resizable=(True, False),
        )

        
        
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()