from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction


class IDEMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main menus for the application
        file_menu = QMenu("File", self)
        edit_menu = QMenu("Edit", self)
        run_menu = QMenu("Run", self)

        # Add actions
        file_menu.addAction(QAction("New File", self))
        file_menu.addAction(QAction("Open File", self))
        file_menu.addAction(QAction("Save", self))

        # Add the menus to the menu bar so they appear at the top of the window
        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(run_menu)
