import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_StatisticsPage(QWidget):
    def __init__(self, rolls: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rolls = rolls if rolls is not None else {}
        self.setupUi()

    def setupUi(self):
        self.main_layout = QVBoxLayout(self)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.canvas)

        self.axes = {}
        self.axes["freq"] = self.figure.add_subplot(221)
        self.axes["avg"] = self.figure.add_subplot(222)
        self.axes["luck"] = self.figure.add_subplot(223)
        self.axes["parity"] = self.figure.add_subplot(224)

        self.rolls_btn = QPushButton("Rolling", self)
        self.reset_btn = QPushButton("Reset rolls", self)

        self.interface_box = QHBoxLayout()
        self.interface_box.addWidget(self.reset_btn)
        self.interface_box.addWidget(self.rolls_btn)
        self.main_layout.addLayout(self.interface_box)

    def update_freq_ax(self):
        ax = self.axes["freq"]

        counts, _ = np.histogram(self.rolls, bins=np.arange(1, 8) - 0.5)
        frequencies = counts / len(self.rolls)

        ax.bar(
            range(1, 7),
            frequencies,
            label="Zaobserwowane",
        )
        ax.axhline(1 / 6, color="red", linestyle="--", label="Teoretyczne")
        ax.set_title("Częstotliwości")
        ax.set_xlabel("Wartość")
        ax.set_ylabel("Częstotliwość")
        ax.set_xticks(range(1, 7))
        ax.legend()

    def update_average_ax(self):
        ax = self.axes["avg"]
        avg = np.cumsum(self.rolls) / np.arange(1, len(self.rolls) + 1)

        ax.plot(
            np.arange(1, len(self.rolls) + 1),
            avg,
            label="Średnia",
        )
        ax.axhline(
            7 / 2, color="red", linestyle="--", label=f"Wartość Oczekiwana: {7 / 2}"
        )

        ax.set_xlabel("Liczba rzutów")
        ax.set_title("Średnia")
        ax.set_ylabel("Wartość")
        ax.legend()

    def update_luck_ax(self):
        ax = self.axes["luck"]
        luck = {
            "high": len([x for x in self.rolls if x >= 4]) / len(self.rolls),
            "low": len([x for x in self.rolls if x <= 3]) / len(self.rolls),
        }

        ax.bar(
            ["Wysokie", "Niskie"],
            luck.values(),
            label="Zaobserwowane",
        )
        ax.axhline(0.5, color="red", linestyle="--", label="Teoretyczne")

        ax.set_title("Częstotliwość wysokich i niskich rzutów")
        ax.set_ylabel("Częstotliwość")
        ax.legend()

    def update_parity_ax(self):
        ax = self.axes["parity"]

        parity = {
            "even": len([x for x in self.rolls if x % 2 == 1]) / len(self.rolls),
            "odd": len([x for x in self.rolls if x % 2 == 0]) / len(self.rolls),
        }

        ax.bar(
            ["Parzyste", "Nieparzyste"],
            parity.values(),
            label="Zaobserwowane",
        )
        ax.axhline(0.5, color="red", linestyle="--", label="Teoretyczne")

        ax.set_title("Częstotliwość parzystych i nieparzystych rzutów")
        ax.set_ylabel("Częstotliwość")
        ax.legend()

    def showEvent(self, _):
        for ax in self.axes.values():
            ax.clear()

        self.update_freq_ax()
        self.update_average_ax()
        self.update_luck_ax()
        self.update_parity_ax()

        self.figure.tight_layout()

        self.label.setText(f"Na podstawie {len(self.rolls)} rzutów")

        self.canvas.draw()
