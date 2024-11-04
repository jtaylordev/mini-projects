# folder.py

from file_system_object import FileSystemObject

class Folder(FileSystemObject):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.__children = []  # Private attribute

    def add_child(self, child):
        self.__children.append(child)
        child._parent = self  # Set the parent of the child

    def remove_child(self, name):
        for child in self.__children:
            if child.get_name() == name:
                self.__children.remove(child)
                child._parent = None
                return True
        return False

    def get_child(self, name):
        for child in self.__children:
            if child.get_name() == name:
                return child
        return None

    def list_children(self):
        return [child.get_name() for child in self.__children]

    def get_children(self):
        return self.__children.copy()  # Return a copy to prevent external modification
