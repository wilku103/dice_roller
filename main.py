from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Initialize the MainWindow and connect functional UI signals
        """
        super().__init__(*args, **kwargs)

        self.MAX_GRID_COLS = 10
        self.rolls = []

        self.setupUi(self)

        # Connect UI controls to their handlers
        self.dice_page.roll_btn.clicked.connect(self.roll_dice)
        self.dice_page.save_btn.clicked.connect(self.save_rolls)
        self.statistics_page.reset_btn.clicked.connect(self.reset)

        self.show()

    def roll_dice(self):
        """
        Roll the configured number of six-sided dice and display results.

        Reads the number of dice from the dice page UI, clears any previously
        displayed dice widgets, generates random results for six-sided dice
        (1..6), appends them to the session `rolls` list, and lays out
        QLabel widgets in a grid on the dice page to show each result.
        """
        amount = self.dice_page.num_dice.value()

        # remove all widgets from self.dice_box
        while self.dice_page.dice_box.count():
            item = self.dice_page.dice_box.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        for i in range(amount):
            rolled = randint(1, 6)
            self.rolls.append(rolled)

            dice = QLabel(str(rolled))
            dice.setMaximumSize(50, 50)
            dice.setStyleSheet("border: 2px solid gray; padding: 5px;")

            row = i // self.MAX_GRID_COLS
            col = i % self.MAX_GRID_COLS

            self.dice_page.dice_box.addWidget(
                dice, row, col, Qt.AlignmentFlag.AlignCenter
            )

    def reset(self):
        """
        Clear all recorded rolls and refresh the statistics page.

        This method clears the in-memory list of rolls and triggers an update
        of the statistics page so the UI reflects the cleared state.
        """
        self.rolls.clear()
        self.statistics_page.showEvent(None)  # update the page

    def save_rolls(self):
        """
        Save recorded rolls to a text file.

        Each roll is written on its own line. The file is created or
        overwritten in the current working directory.
        """
        with open("rolls.txt", "w") as file:
            for roll in self.rolls:
                file.write(str(roll) + "\n")


def main():
    """
    Start the Qt application and show the main window.
    """
    app = QApplication([])

    # needed to prevent garbage collection of the main window
    _window = MainWindow()

    app.exec()


if __name__ == "__main__":
    main()
