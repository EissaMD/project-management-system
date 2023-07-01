import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self):
        super().__init__(
            title="Project Management System",
            themename="journal",
            size=(700, 600),
            resizable=(True, False),
        )
        # ============ create top menu ============
        top_frame = ttk.Frame(master=self,height=400 , bootstyle="secondary")
        top_frame.pack(side="top" , fill="x" ,anchor="center")
        main_menu = {"Project":  1,
                     "Supplier":   1,
                     "Customer":  1,
                     "Reports":  1,
                     }
        for btn_name , btn_func in main_menu.items():
            ttk.Button(top_frame,text=btn_name).pack(side="left")
        self.secondary_menu = ttk.Frame(master=self, bootstyle="info")
        self.secondary_menu.pack(side="top" , fill="x" ,anchor="w")
        frame=ttk.Frame(self.secondary_menu, bootstyle="info"); frame.pack()
        ttk.Button(frame,text="btn_name" , bootstyle="info").pack(side="left" , padx=1,anchor="e")
        ttk.Button(frame,text="btn_name" , bootstyle="info").pack(side="left" , padx=1,anchor="e")
        # ============ Create body frame ============
        self.body_frame = ttk.Frame(master=self, bootstyle="light")
        self.body_frame.pack( fill="both" ,expand=True)

        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()