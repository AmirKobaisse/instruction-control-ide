from PyQt6.QtWidgets import QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir


class FileTree(QTreeView):
    def __init__(self):
        super().__init__()

        # Create a model that will show the files and folders
        self.model = QFileSystemModel()
        # Set the starting folder to the current folder where the program runs
        self.model.setRootPath(QDir.currentPath())

        # Connect the model to the tree view so it can display files
        self.setModel(self.model)
        # Set the root of the tree to the current folder
        self.setRootIndex(self.model.index(QDir.currentPath()))
        # Hide the column headers because we only need to see the file names
        self.setHeaderHidden(True)
