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
        self.page = None
        main_menu = {"Project"  :   ProjectPage,
                     "Supplier" :   ProjectPage,
                     "Customer" :   ProjectPage,
                     "Reports"  :   ProjectPage,
                     }
        for btn_name , page_class in main_menu.items():
            ttk.Button(top_frame,text=btn_name ,command=lambda: self.main_menu_btn(page_class)).pack(side="left")
        self.main_menu_btn(ProjectPage)
    def main_menu_btn(self,page_class):
        if self.page is not None:
            self.page.secondary_menu.destroy()
            self.page.body_frame.destroy()
        # initialize the page class
        self.page = page_class(self)
##############################################################################################################

if __name__ == "__main__":
    app = App()
    app.mainloop()