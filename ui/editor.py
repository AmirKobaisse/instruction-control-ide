from PyQt6.QtWidgets import QTextEdit


class CodeEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Start typing your code here...")
        self.setStyleSheet("""
            QTextEdit {
                font-family: Consolas;
                font-size: 14px;
            }
        """)
