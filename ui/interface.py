from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

import main_page
from utils import theme_manager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        main_widget = QWidget()
        window_layout = QVBoxLayout(self)

        self.page = main_page.QMainPage()
        window_layout.addWidget(self.page)

        main_widget.setLayout(window_layout)
        self.setCentralWidget(main_widget)


app = QApplication([])
app.setStyleSheet(theme_manager.load_stylesheet('user_theme'))

window = MainWindow()
window.show()

app.exec()
