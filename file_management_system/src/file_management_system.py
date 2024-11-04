# file_management_system.py

import pickle
from folder import Folder
from file import File

class FileManagementSystem:
    def __init__(self):
        self.root = Folder('root')
        self.current_folder = self.root

    def change_directory(self, folder_name):
        if folder_name == '..':
            if self.current_folder.get_parent() is not None:
                self.current_folder = self.current_folder.get_parent()
            else:
                print("Already at the root directory.")
        else:
            folder = self.current_folder.get_child(folder_name)
            if isinstance(folder, Folder):
                self.current_folder = folder
            else:
                print(f"Folder '{folder_name}' not found.")

    def create_file(self, name, content=""):
        if self.current_folder.get_child(name):
            print(f"An item named '{name}' already exists.")
            return
        new_file = File(name, self.current_folder, content)
        self.current_folder.add_child(new_file)
        print(f"File '{name}' created.")

    def create_folder(self, name):
        if self.current_folder.get_child(name):
            print(f"An item named '{name}' already exists.")
            return
        new_folder = Folder(name, self.current_folder)
        self.current_folder.add_child(new_folder)
        print(f"Folder '{name}' created.")

    def remove_item(self, name):
        if self.current_folder.remove_child(name):
            print(f"Item '{name}' removed.")
        else:
            print(f"Item '{name}' not found.")

    def list_directory(self):
        children = self.current_folder.list_children()
        if children:
            for child in children:
                print(child)
        else:
            print("Directory is empty.")

    def list_all(self, folder=None, indent=0):
        if folder is None:
            folder = self.current_folder
        print('  ' * indent + folder.get_name() + '/')
        for child in folder.get_children():
            if isinstance(child, Folder):
                self.list_all(child, indent + 1)
            else:
                print('  ' * (indent + 1) + child.get_name())

    def save_file_system(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.root, f)
        print(f"File system saved to '{filename}'.")

    def load_file_system(self, filename):
        with open(filename, 'rb') as f:
            self.root = pickle.load(f)
            self.current_folder = self.root
        print(f"File system loaded from '{filename}'.")

    def get_current_path(self):
        return self.current_folder.get_path()
