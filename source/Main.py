import sys

from PyQt5.QtWidgets import QApplication

from source.screens.StartScreen import StartScreen

from DataBase import DataBase

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = StartScreen()
    janela.show()

    banco = DataBase("../data/database.db")
    if banco.connect():
        banco.consult_data()
        banco.disconnect()

    sys.exit(app.exec_())
