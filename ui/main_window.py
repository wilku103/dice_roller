from PyQt6 import QtCore
from PyQt6.QtWidgets import QStackedWidget

from ui.dice_page import Ui_DicePage
from ui.statistics_page import Ui_StatisticsPage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QStackedWidget()
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.dice_page = Ui_DicePage()
        self.statistics_page = Ui_StatisticsPage(MainWindow.rolls)

        self.dice_page.statistics_btn.clicked.connect(
            lambda: self.centralwidget.setCurrentWidget(self.statistics_page)
        )
        self.statistics_page.rolls_btn.clicked.connect(
            lambda: self.centralwidget.setCurrentWidget(self.dice_page)
        )
        self.centralwidget.addWidget(self.dice_page)
        self.centralwidget.addWidget(self.statistics_page)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dice roller"))
