from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QFont, QTextCursor
from .redirector import Redirector

_OUTPUT_FONT = QFont('Consolas')
_OUTPUT_FONT.setPointSize(12)

_SOURCE_FONT = QFont('Consolas')
_SOURCE_FONT.setPointSize(16)


class SourceArea(QTextEdit):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setFont(_SOURCE_FONT)


class OutputArea(QTextEdit):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setFont(_OUTPUT_FONT)
        self.setReadOnly(True)

    def insertPlainText(self, text: str) -> None:
        super().insertPlainText(text)
        self.moveCursor(QTextCursor.End)


class Editor(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.resize(800, 600)
        self._init_areas()

    def _init_areas(self):
        self._layout = QVBoxLayout()
        self._source_area = SourceArea(self)
        self._output_area = OutputArea(self)
        self._layout.addWidget(self._source_area)
        self._layout.addWidget(QLabel('Output'))
        self._layout.addWidget(self._output_area)
        self.setLayout(self._layout)

    @property
    def stdout(self):
        return Redirector(self._write_stdout_output)

    @property
    def code(self):
        return self._source_area.toPlainText()

    def _write_stdout_output(self, s: str):
        self._output_area.insertPlainText(s)

    def clear_output(self):
        self._output_area.clear()
