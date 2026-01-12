from PyQt6.QtWidgets import QStatusBar, QLabel


class IDEStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Creates a label showing application responsiveness 
        self.status_label = QLabel("Ready")
        self.addWidget(self.status_label)
