# -*- coding: utf-8 -*-
import sys
from quakes.LatestQuakes import LatestQuakes
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Son Depremler'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 768
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        q = LatestQuakes()
        c = 0

        self.tableWidget = QTableWidget()
        self.tableWidget.setVerticalHeaderLabels(('Row 1', 'Row 2', 'Row 3'))
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 160)

        for quake in q.work():
            self.tableWidget.setItem(c, 0, QTableWidgetItem(quake["text"]))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(quake["name"]))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(quake["time"]))
            self.tableWidget.setItem(c, 3, QTableWidgetItem(quake["hours"]))
            self.tableWidget.setItem(c, 4, QTableWidgetItem(quake["deep"]))
            self.tableWidget.setItem(c, 5, QTableWidgetItem(quake["longitude"][0]))
            self.tableWidget.setItem(c, 6, QTableWidgetItem(quake["latitude"][0]))
            c = c + 1

        self.tableWidget.move(0, 0)
        # table selection change
        # self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

