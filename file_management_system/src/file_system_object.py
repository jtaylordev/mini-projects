# filesystem_object.py

class FileSystemObject:
    def __init__(self, name, parent=None):
        self._name = name  # Protected attribute
        self._parent = parent  # Protected attribute

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_parent(self):
        return self._parent

    def get_path(self):
        path = []
        current = self
        while current is not None:
            path.insert(0, current.get_name())
            current = current.get_parent()
        return '/' + '/'.join(path[1:])  # Exclude the root's name for a clean path
