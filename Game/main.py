from ui import Game

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)

def gameMain():
    app = QApplication(sys.argv)
    game = Game()
    game.showGame(4, "test case")
    sys.exit(app.exec_())

if __name__ == '__main__':
    gameMain()