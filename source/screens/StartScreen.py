from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit


class BackgroundWidget(QWidget):
    def __init__(self, image_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_path = image_path
        self.pixmap = QPixmap(self.image_path)

    def paint_event(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)


class StartScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela Inicial do Aplicativo")
        self.setGeometry(100, 100, 360, 640)

        self.central_widget = BackgroundWidget("../assets/taylor.jpg")
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.title = QLabel("Bem-vindo ao Meu Aplicativo", self)
        self.title.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        self.layout.addWidget(self.title)

        self.textField = QLineEdit(self)
        self.textField.setPlaceholderText("Digite algo aqui...")
        self.layout.addWidget(self.textField)

        self.button = QPushButton("Clique Aqui", self)
        self.button.clicked.connect(self.button_clicked)
        self.layout.addWidget(self.button)

        self.central_widget.setLayout(self.layout)

    def button_clicked(self):
        texto = self.textField.text()
        self.title.setText(f"Você digitou: {texto}")
