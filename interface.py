import requests
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QFrame, QGridLayout, QScrollArea, \
    QHBoxLayout, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QWidget()
        self.page = QMainPage()
        layout = QVBoxLayout(self)
        layout.addWidget(self.page)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class QCard(QFrame):
    """Кастомный виджет карточки проекта"""

    def __init__(self, name: str, attrs: str, img_link: str = 'https://statichdrezka.ac/i/2024/12/22'
                                                              '/l6bae6a0d936dlc91j33o.jpg'):
        super().__init__()

        # Описание настроек класса
        self.img_link = img_link
        self.setFixedSize(200, 350)
        self.layout = QVBoxLayout(self)
        self.setObjectName('QCard')

        # Описание параметров

        # Описание параметров изображения проекта
        self.byteArray = requests.get(img_link).content
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(QByteArray(self.byteArray))
        self.img = QLabel()
        self.img.setPixmap(self.pixmap)
        self.img.setScaledContents(True)
        self.img.setFixedSize(177, 256)
        self.img.setObjectName('img')

        # Описание настроек поля имени класса
        self.name = QLabel(name)
        self.name.setObjectName('name')

        # Описание настроек аттрибутов класса (год, жанр, страна)
        self.attrs = QLabel(attrs)
        self.attrs.setObjectName('attrs')

        self.layout.addWidget(self.img)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.attrs)
        self.setLayout(self.layout)

    def was_clicked(self):
        pass

    def was(self):
        # Курсор мыши наведён на карточку
        pass

class QHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        self.settings_btn = QPushButton('Настройки')
        self.layout.addWidget(self.settings_btn)

        self.searchbar = QLineEdit('Поиск')
        self.layout.addWidget(self.searchbar)

        self.continue_watching_btn = QPushButton('Досмотреть')
        self.layout.addWidget(self.continue_watching_btn)

        self.profile_btn = QPushButton('Профиль')
        self.layout.addWidget(self.profile_btn)

        self.setLayout(self.layout)

class QScroller(QScrollArea):
    def __init__(self, widgets):
        super().__init__()

        self.container = QWidget()
        self.layout = QGridLayout()

        self.addWidgets(widgets)

        self.container.setLayout(self.layout)
        self.setWidget(self.container)

    def addWidgets(self, widgets: list[QWidget]):
        row = 1
        column = 1
        for widget in widgets:
            self.layout.addWidget(widget, row, column)
            if column == 4:
                row += 1
                column = 0
            column += 1

class QGenres(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()


class QMainPage(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        # "шапка" экрана
        header = QHeader()

        # скроллер (ему необходим внутренний контейнер)
        self.scroller = QScroller([QCard('1', '1'), QCard('1', '2'), QCard('1', '3'), QCard('1', '4'), QCard('2', '1')])
        main_layout.addWidget(header)
        main_layout.addWidget(self.scroller)

        self.setLayout(main_layout)


app = QApplication([])

with open('style.qss', 'r') as f:
    style = f.read()
    app.setStyleSheet(style)

window = MainWindow()
window.show()

app.exec()
