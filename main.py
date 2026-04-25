from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel
from random import randint

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Dice roller")
        self.setGeometry(100, 100, 800, 600)

        roll_button = QPushButton("Roll", clicked=self.roll_dice)
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.dice_box = QHBoxLayout()
        mainLayout.addLayout(self.dice_box)

        interfaceLayout = QHBoxLayout()
        self.num_dice = QSpinBox(value=1)
        self.dice_sides = QSpinBox(value=6)
        interfaceLayout.addWidget(self.num_dice)
        interfaceLayout.addWidget(self.dice_sides)
        interfaceLayout.addWidget(roll_button)
        mainLayout.addLayout(interfaceLayout)


        self.show()


    def roll_dice(self):
        amount = self.num_dice.value()
        sides = self.dice_sides.value()

        #remove all widgets from self.dice_box
        for i in reversed(range(self.dice_box.count())):
            widget = self.dice_box.itemAt(i).widget()
            widget.setParent(None)
            widget.deleteLater()

        for i in range(amount):
            dice = QLabel()
            dice.setText(str(randint(1, sides)))
            self.dice_box.addWidget(dice)


def main():
    app = QApplication([])

    window = MainWindow()

    app.exec()


if __name__ == '__main__':
    main()