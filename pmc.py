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
        top_frame = ttk.Frame(master=self,height=400, bootstyle="secondary")
        top_frame.pack(side="top" , fill="x" ,anchor="center" )
        main_menu = {"Project":  1,
                     "Supplier":   1,
                     "Customer":  1,
                     "Reports":  1,
                     }
        for btn_name , btn_func in main_menu.items():
            ttk.Button(top_frame,text=btn_name ).pack(side="left")
        self.secondary_menu = ttk.Frame(master=self, bootstyle="info")
        self.secondary_menu.pack(side="top" , fill="x" ,anchor="w")
        frame=ttk.Frame(self.secondary_menu, bootstyle="info"); frame.pack()
        # ============ Create body frame ============
        self.body_frame = ttk.Frame(master=self, bootstyle="light")
        self.body_frame.pack( fill="both" ,expand=True)
        page = NewPage(self,self.secondary_menu,self.body_frame)
        menu = {"New Project":      1,
                "Edit Project":     1,
                "Delete Project":   1,
                }
        page.create_secondary_menu(menu)
        page.create_body("Add New Project")
##############################################################################################################

class NewPage():
    def __init__(self,main_window,secondary_menu,body_frame):
        self.main_window = main_window
        self.secondary_menu = secondary_menu
        self.body_frame = body_frame
    ###############        ###############        ###############        ###############
    def create_body(self , title="No Title"):
        self.body_frame.destroy()
        self.body_frame = ttk.Frame(master=self.main_window)
        self.body_frame.pack( fill="both" ,expand=True)
        ttk.Label(self.body_frame,font="Times 25 bold" ,text=title ).pack(pady=6)

    ###############        ###############        ###############        ###############
    def create_secondary_menu(self , menu):
        self.secondary_menu.destroy()
        self.secondary_menu = ttk.Frame(master=self.main_window, bootstyle="info")
        self.secondary_menu.pack(side="top" , fill="x" ,anchor="w")
        frame=ttk.Frame(self.secondary_menu, bootstyle="info"); frame.pack()
        for btn_name , btn_func in menu.items():
            ttk.Button(frame,text=btn_name , bootstyle="info").pack(side="left")
##############################################################################################################

if __name__ == "__main__":
    app = App()
    app.mainloop()