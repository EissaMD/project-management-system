from .NewPage import NewPage
import ttkbootstrap as ttk
from .EntriesFrame import EntriesFrame


class ProjectPage(NewPage):
        def __init__(self,main_window):
                super().__init__(main_window)
                menu = {"Add New Project"   :self.new_project_frame,
                        "Edit Project"      :self.edit_project_frame,
                        "Delete Project"    :self.delete_project_frame,
                        }
                self.create_secondary_menu(menu)
                self.new_project_frame()
        ###############        ###############        ###############        ###############
        def new_project_frame(self):
                self.create_body("New Project")
        ###############        ###############        ###############        ###############
        def edit_project_frame(self):
                self.create_body("Edit Project")
        ###############        ###############        ###############        ###############    
        def delete_project_frame(self):
                self.create_body("Delete Project")

##############################################################################################################