from PyQt6 import QtCore, QtWidgets


class Ui_DicePage(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dice_box = QtWidgets.QGridLayout()
        self.dice_box.setObjectName("dice_box")
        self.verticalLayout.addLayout(self.dice_box)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.interface_box = QtWidgets.QHBoxLayout()
        self.interface_box.setObjectName("interface_box")
        self.num_dice = QtWidgets.QSpinBox(parent=self)
        self.num_dice.setMinimum(1)
        self.num_dice.setObjectName("num_dice")
        self.interface_box.addWidget(self.num_dice)
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setObjectName("label")
        self.interface_box.addWidget(self.label)
        self.dice_sides = QtWidgets.QSpinBox(parent=self)
        self.dice_sides.setMinimum(1)
        self.dice_sides.setProperty("value", 6)
        self.dice_sides.setObjectName("dice_sides")
        self.interface_box.addWidget(self.dice_sides)
        self.label_2 = QtWidgets.QLabel(parent=self)
        self.label_2.setObjectName("label_2")
        self.interface_box.addWidget(self.label_2)
        self.roll_btn = QtWidgets.QPushButton(parent=self)
        self.roll_btn.setObjectName("roll_btn")
        self.statistics_btn = QtWidgets.QPushButton(parent=self)
        self.statistics_btn.setObjectName("statistics_btn")
        self.interface_box.addWidget(self.roll_btn)
        self.interface_box.addWidget(self.statistics_btn)
        self.verticalLayout.addLayout(self.interface_box)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "dice"))
        self.label_2.setText(_translate("MainWindow", "sided"))
        self.roll_btn.setText(_translate("MainWindow", "Roll"))
        self.statistics_btn.setText(_translate("MainWindow", "Statistics"))
