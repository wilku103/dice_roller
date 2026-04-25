from PyQt6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Dice roller")

        self.show()

def main():
    app = QApplication([])

    window = MainWindow()

    app.exec()


if __name__ == '__main__':
    main()