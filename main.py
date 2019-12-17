# coding=utf-8
import sys
import os
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def request():
    con = sqlite3.connect(resource_path('coffee.sqlite'))
    cur = con.cursor()
    ask = '''SELECT * FROM coffees'''
    result = cur.execute(ask).fetchall()
    con.close()
    return result


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path('main.ui'), self)
        self.result.setColumnCount(7)
        self.result.setWordWrap(True)
        names = ['id', 'Название', 'Степень обжарки', 'В зернах?', 'Описание вкуса', 'цена (руб/кг)',
                 'Объем упаковки (грамм)']
        self.result.setHorizontalHeaderLabels(names)
        self.result.resizeColumnsToContents()
        cof = request()
        self.result.setRowCount(len(cof))
        for i in range(len(cof)):
            self.result.setItem(i, 0, QTableWidgetItem(str(cof[i][0])))
            self.result.setItem(i, 1, QTableWidgetItem(str(cof[i][1])))
            self.result.setItem(i, 2, QTableWidgetItem(str(cof[i][2])))
            is_core = 'Да' if int(cof[i][3]) else 'Нет'
            self.result.setItem(i, 3, QTableWidgetItem(is_core))
            self.result.setItem(i, 4, QTableWidgetItem(str(cof[i][4])))
            self.result.setItem(i, 5, QTableWidgetItem(str(cof[i][5])))
            self.result.setItem(i, 6, QTableWidgetItem(str(cof[i][6])))
        self.result.resizeColumnsToContents()
        self.result.resizeRowsToContents()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())