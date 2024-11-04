# file.py

from file_system_object import FileSystemObject

class File(FileSystemObject):
    def __init__(self, name, parent=None, content=""):
        super().__init__(name, parent)
        self.__content = content  # Private attribute

    def read(self):
        return self.__content

    def write(self, data):
        self.__content = data

    def get_size(self):
        return len(self.__content)
