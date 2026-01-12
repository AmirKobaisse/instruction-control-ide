from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QSplitter
)
from PyQt6.QtCore import Qt

from ui.editor import CodeEditor
from ui.file_tree import FileTree
from ui.menu_bar import IDEMenuBar
from ui.status_bar import IDEStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instruction Control IDE")
        self.resize(1200, 800)

        self._setup_ui()

    def _setup_ui(self):
        # Menu bar
        self.setMenuBar(IDEMenuBar(self))

        # Status bar
        self.setStatusBar(IDEStatusBar(self))

        # Central layout
        central_widget = QWidget()
        layout = QHBoxLayout()

        splitter = QSplitter(Qt.Orientation.Horizontal)

        self.file_tree = FileTree()
        self.editor = CodeEditor()

        splitter.addWidget(self.file_tree)
        splitter.addWidget(self.editor)
        splitter.setSizes([250, 950])

        layout.addWidget(splitter)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
