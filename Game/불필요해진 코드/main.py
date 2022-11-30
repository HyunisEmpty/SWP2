from ui import Game

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)


def gameMain():
    food = 10
    day = 1
    app = QApplication(sys.argv)
    game = Game()
    game.showGame(food, day, "first_start")
    sys.exit(app.exec_())

def Yes():
    return True


if __name__ == '__main__':
    gameMain()