from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.MAX_GRID_COLS = 10
        self.rolls = {}

        self.setupUi(self)

        self.dice_page.roll_btn.clicked.connect(self.roll_dice)

        self.show()

    def roll_dice(self):
        amount = self.dice_page.num_dice.value()
        sides = self.dice_page.dice_sides.value()

        # remove all widgets from self.dice_box
        while self.dice_page.dice_box.count():
            item = self.dice_page.dice_box.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
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

            self.dice_page.dice_box.addWidget(
                dice, row, col, Qt.AlignmentFlag.AlignCenter
            )


def main():
    app = QApplication([])

    # needed to prevent garbage collection of the main window
    _window = MainWindow()

    app.exec()


if __name__ == "__main__":
    main()
