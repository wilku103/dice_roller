from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_DicePage(QWidget):
    def __init__(self, *args, **kwargs):
        """
        Initialize the DicePage class.
        """
        super().__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
        """
        Set up the DicePage UI.
        """
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dice_box = QGridLayout()
        self.dice_box.setObjectName("dice_box")
        self.verticalLayout.addLayout(self.dice_box)
        spacerItem = QSpacerItem(
            20,
            40,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.interface_box = QHBoxLayout()
        self.interface_box.setObjectName("interface_box")

        self.num_dice = QSpinBox(parent=self)
        self.num_dice.setMinimum(1)
        self.num_dice.setMaximum(200)
        self.num_dice.setObjectName("num_dice")

        self.interface_box.addWidget(self.num_dice)

        self.label = QLabel(parent=self)
        self.label.setObjectName("label")
        self.interface_box.addWidget(self.label)

        self.roll_btn = QPushButton(parent=self)
        self.roll_btn.setObjectName("roll_btn")

        self.statistics_btn = QPushButton(parent=self)
        self.statistics_btn.setObjectName("statistics_btn")

        self.save_btn = QPushButton(parent=self)
        self.save_btn.setObjectName("save_btn")

        self.interface_box.addWidget(self.roll_btn)
        self.interface_box.addWidget(self.save_btn)
        self.interface_box.addWidget(self.statistics_btn)
        self.verticalLayout.addLayout(self.interface_box)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi()

    def retranslateUi(self):
        """
        Set the text for the UI elements.
        """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "dice"))
        self.roll_btn.setText(_translate("MainWindow", "Roll"))
        self.statistics_btn.setText(_translate("MainWindow", "Statistics"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
