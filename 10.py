import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon


class MyStatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyStat")
        self.setGeometry(100, 100, 1200, 700)

        # Общий стиль
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                color: #333;
            }
            QFrame#card {
                border-radius: 10px;
                color: white;
            }
            QFrame#block {
                border: 1px solid #ccc;
                border-radius: 8px;
                background: #fff;
            }
            QPushButton#menuButton {
                background: transparent;
                border: none;
                padding: 10px;
            }
            QPushButton#menuButton:hover {
                background: #d0d0d0;
                border-radius: 8px;
            }
        """)

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(15)

        # --- Боковое меню только с иконками ---
        side_menu = QVBoxLayout()
        side_menu.setSpacing(15)
        side_menu.setAlignment(Qt.AlignTop)

        menu_icons = [
            "home.png",
            "tasks.png",
            "calendar.png",
            "grades.png",
            "stats.png",
            "settings.png"
        ]

        for icon_file in menu_icons:
            button = QPushButton()
            button.setObjectName("menuButton")
            button.setIcon(QIcon(f"icons/{icon_file}"))
            button.setIconSize(QSize(32, 32))
            button.setFixedSize(60, 60)  # квадратные кнопки
            side_menu.addWidget(button, alignment=Qt.AlignHCenter)

        side_menu_frame = QFrame()
        side_menu_frame.setLayout(side_menu)
        side_menu_frame.setFixedWidth(80)

        # --- Основное содержимое ---
        content_layout = QVBoxLayout()
        content_layout.setSpacing(20)

        # --- Карточки сверху ---
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(15)

        card1 = QFrame()
        card1.setObjectName("card")
        card1.setStyleSheet("background-color: MediumSlateBlue;")
        card1.setFixedHeight(100)
        card1_layout = QVBoxLayout()
        card1_layout.setSpacing(2)
        label_value1 = QLabel("2")
        label_value1.setFont(QFont("Arial", 18, QFont.Bold))
        label_value1.setAlignment(Qt.AlignCenter)
        label_title1 = QLabel("Задания к выполнению")
        label_title1.setFont(QFont("Arial", 10))
        label_title1.setAlignment(Qt.AlignCenter)
        card1_layout.addWidget(label_value1)
        card1_layout.addWidget(label_title1)
        card1.setLayout(card1_layout)

        card2 = QFrame()
        card2.setObjectName("card")
        card2.setStyleSheet("background-color: Red;")
        card2.setFixedHeight(100)
        card2_layout = QVBoxLayout()
        card2_layout.setSpacing(2)
        label_value2 = QLabel("0/2")
        label_value2.setFont(QFont("Arial", 18, QFont.Bold))
        label_value2.setAlignment(Qt.AlignCenter)
        label_title2 = QLabel("Задания просрочено")
        label_title2.setFont(QFont("Arial", 10))
        label_title2.setAlignment(Qt.AlignCenter)
        card2_layout.addWidget(label_value2)
        card2_layout.addWidget(label_title2)
        card2.setLayout(card2_layout)

        cards_layout.addWidget(card1, 1)
        cards_layout.addWidget(card2, 1)
        content_layout.addLayout(cards_layout)

        # --- Блоки с данными ---
                # --- Блоки с данными ---
        grid = QGridLayout()
        grid.setSpacing(15)

        def create_block(title, content):
            block = QFrame()
            block.setObjectName("block")

            layout = QVBoxLayout()
            layout.setContentsMargins(8, 6, 8, 6)   # компактные отступы
            layout.setSpacing(4)

            header = QLabel(title)
            header.setFont(QFont("Consolas", 10, QFont.Bold))  # шрифт меньше
            header.setFixedHeight(20)                         # низкий заголовок
            header.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            body = QLabel(content)
            body.setAlignment(Qt.AlignTop | Qt.AlignLeft)

            layout.addWidget(header)
            layout.addWidget(body)
            block.setLayout(layout)

            return block

        block1 = create_block("Средний балл", "Здесь будет график 📊")
        block2 = create_block("Оценки", "Сентябрь: 12, 12, 12...\nАвгуст: 12, 12, 12...")
        block3 = create_block("Посещаемость", "100% посещение\n0% пропуск\n0% опоздание")
        block4 = create_block("Расписание", "Понедельник: Математика, Английский\nВторник: История, Физика")

        grid.addWidget(block1, 0, 0)
        grid.addWidget(block4, 0, 1)
        grid.addWidget(block2, 1, 0)
        grid.addWidget(block3, 1, 1)

        content_layout.addLayout(grid)

        

        # --- Финальная сборка ---
        main_layout.addWidget(side_menu_frame, 0)
        main_layout.addLayout(content_layout, 1)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyStatApp()
    window.show()
    sys.exit(app.exec_())




