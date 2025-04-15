from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel
from PySide6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-page App")
        self.setGeometry(100, 100, 600, 400)

        # Создаем QStackedWidget
        self.stacked_widget = QStackedWidget(self)

        # Страницы
        self.page1 = self.create_main_menu_page()
        self.page2 = self.create_settings_page()
        self.page3 = self.create_search_page()

        # Добавляем страницы в QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # Кнопки для навигации
        self.nav_buttons = self.create_navigation_buttons()

        # Размещение кнопок и стека виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.nav_buttons)
        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)

    def create_main_menu_page(self):
        # Страница главного меню
        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Главное меню"))
        page.setLayout(layout)
        return page

    def create_settings_page(self):
        # Страница настроек
        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Настройки"))
        page.setLayout(layout)
        return page

    def create_search_page(self):
        # Страница поиска
        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Поиск"))
        page.setLayout(layout)
        return page

    def create_navigation_buttons(self):
        # Кнопки для переключения страниц
        widget = QWidget()
        button_layout = QVBoxLayout()

        # Кнопка для главного меню
        button_main_menu = QPushButton("Главное меню")
        button_main_menu.clicked.connect(self.show_main_menu)
        button_layout.addWidget(button_main_menu)

        # Кнопка для настроек
        button_settings = QPushButton("Настройки")
        button_settings.clicked.connect(self.show_settings)
        button_layout.addWidget(button_settings)

        # Кнопка для поиска
        button_search = QPushButton("Поиск")
        button_search.clicked.connect(self.show_search)
        button_layout.addWidget(button_search)

        widget.setLayout(button_layout)
        return widget

    def show_main_menu(self):
        # Переключить на главную страницу
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_settings(self):
        # Переключить на страницу настроек
        self.stacked_widget.setCurrentWidget(self.page2)

    def show_search(self):
        # Переключить на страницу поиска
        self.stacked_widget.setCurrentWidget(self.page3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())