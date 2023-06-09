import ttkbootstrap as ttk

class NewPage():
    def __init__(self,main_window):
        self.main_window = main_window
        self.secondary_menu = None
        self.body_frame = None
    ###############        ###############        ###############        ###############
    def create_secondary_menu(self , menu):
        if isinstance(self.secondary_menu, ttk.Frame):
            self.secondary_menu.destroy()
        self.secondary_menu = ttk.Frame(master=self.main_window, bootstyle="info")
        self.secondary_menu.pack(side="top" , fill="x" ,anchor="w")
        frame=ttk.Frame(self.secondary_menu, bootstyle="info"); frame.pack(side="top")
        for btn_name , btn_func in menu.items():
            ttk.Button(frame,text=btn_name, command=btn_func , bootstyle="info").pack(side="left")
    ###############        ###############        ###############        ###############
    def create_body(self , title="No Title"):
        if isinstance(self.body_frame, ttk.Frame):
            self.body_frame.destroy()
        self.body_frame = ttk.Frame(master=self.main_window)
        self.body_frame.pack( fill="both" ,expand=True)
        ttk.Label(self.body_frame,font="Times 25 bold" ,text=title ).pack(pady=6)
    ###############        ###############        ###############        ###############
    def get_frames(self ):
        return self.secondary_menu , self.body_frame
##############################################################################################################