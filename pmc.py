import ttkbootstrap as ttk
from ui import *

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
        self.secondary_menu = ttk.Frame(master=self, bootstyle="info")
        self.secondary_menu.pack(side="top" , fill="x" ,anchor="w")
        frame=ttk.Frame(self.secondary_menu, bootstyle="info"); frame.pack()
        # ============ Create body frame ============
        self.body_frame = ttk.Frame(master=self, bootstyle="light")
        self.body_frame.pack( fill="both" ,expand=True)
        
        main_menu = {"Project"  :   ProjectPage,
                     "Supplier" :   ProjectPage,
                     "Customer" :   ProjectPage,
                     "Reports"  :   ProjectPage,
                     }
        for btn_name , page_class in main_menu.items():
            ttk.Button(top_frame,text=btn_name ,command=lambda: self.main_menu_btn(page_class)).pack(side="left")
        self.main_menu_btn(ProjectPage)
    def main_menu_btn(self,page_class):
        # initialize the page class
        page = page_class(self,self.secondary_menu , self.body_frame)
        # get secondary_menu and body frame so it can be destroyed later
        self.secondary_menu , self.body_frame = page.get_frames()
##############################################################################################################

if __name__ == "__main__":
    app = App()
    app.mainloop()