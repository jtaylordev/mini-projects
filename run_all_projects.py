import subprocess 
import os 
from library_management_system.src import *
from library_management_system.src.library_system import LibrarySystem

PROJECTS = [ 
    "file_management_system", 
    "inventory_management", 
    "library_management_system", 
    "maze_solver", 
    "sorting_visualizer", 
    "weather_data_dashboard" 
] 
 
def run_project(project): 
    project_main_file = os.path.join(project, "src", "main.py") 
    if os.path.exists(project_main_file): 
        print(f"\nRunning {project}...\n") 
        subprocess.run(["python", project_main_file]) 
    else: 
        print(f"\nNo main.py found for {project}\n") 

def run_library_management_system():
    library = LibrarySystem()
    library.books.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.books.add_book("1984", "George Orwell")
    library.books.add_book("To Kill a Mockingbird", "Harper Lee")
    library.books.display_books()

if __name__ == "__main__": 
    run_library_management_system()
