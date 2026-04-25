from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.MAX_GRID_COLS = 10

        self.setupUi(self)

        self.rolls = {}

        self.roll_btn.clicked.connect(self.roll_dice)

        self.show()

    def roll_dice(self):
        amount = self.num_dice.value()
        sides = self.dice_sides.value()

        # remove all widgets from self.dice_box
        for i in reversed(range(self.dice_box.count())):
            widget = self.dice_box.itemAt(i).widget()
            widget.setParent(None)
            widget.deleteLater()

        for i in range(amount):
            rolled = randint(1, sides)
            if sides not in self.rolls:
                self.rolls[sides] = []
            self.rolls[sides].append(rolled)
            dice = QLabel(str(rolled))
            dice.setMaximumSize(50, 50)
            dice.setStyleSheet("border: 2px solid gray; padding: 5px;")

            row = i // self.MAX_GRID_COLS
            col = i % self.MAX_GRID_COLS

            self.dice_box.addWidget(dice, row, col, Qt.AlignmentFlag.AlignCenter)


def main():
    app = QApplication([])

    window = MainWindow()

    app.exec()


if __name__ == '__main__':
    main()
