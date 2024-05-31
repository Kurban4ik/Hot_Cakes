import sqlite3
import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from dbFunctions.muslim import db_absolyte_way


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('manage_app.ui', self)
        self.show()
        con = sqlite3.connect(db_absolyte_way)
        cur = con.cursor()

        cur.execute(f'''SELECT name, last_ip FROM All_Workers''')

        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        for i in cur:
            item = QtGui.QStandardItem(str(i[0]) + ' ' + str(i[1]))
            model.appendRow(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())