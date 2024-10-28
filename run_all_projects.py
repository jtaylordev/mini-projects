import subprocess 
import os 
 
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
 
if __name__ == "__main__": 
    for project in PROJECTS: 
        run_project(project) 
