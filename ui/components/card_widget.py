from io import BytesIO

from PIL import Image
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class MovieCardWidget(QWidget):
    def __init__(self, title: str, image_data: bytes):
        super().__init__()
        layout = QVBoxLayout(self)

        self.title_label = QLabel(title)

        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_label = QLabel()
        pixmap = self.bytes_to_pixmap(image_data)
        image_label.setPixmap(pixmap.scaled(200, 300))

        layout.addWidget(image_label)
        layout.addWidget(self.title_label)

    def bytes_to_pixmap(self, data: bytes) -> QPixmap:
        image = Image.open(BytesIO(data))
        image = image.convert('RGBA')
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        return pixmap
