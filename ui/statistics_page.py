from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class Ui_StatisticsPage(QWidget):
    def __init__(self, rolls: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rolls = rolls if rolls is not None else {}
        self.setupUi()

    def setupUi(self):
        self.main_layout = QVBoxLayout(self)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        self.main_layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)

        self.rolls_btn = QPushButton("Rolling", self)

    def showEvent(self, _):
        self.ax.clear()
        max_value = max(list(self.rolls)) if self.rolls else 0
        counts_total = [0] * max_value
        for sides, rolls in self.rolls.items():
            for roll in rolls:
                counts_total[roll - 1] += 1

        print(counts_total)
        self.ax.bar(
            range(1, max_value + 1),
            counts_total,
            label=f"Total rolls: {sum(counts_total)}",
        )
        self.ax.legend()
        self.canvas.draw()
