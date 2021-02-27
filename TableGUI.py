import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class TableWindow(QtWidgets.QTableWidget):
    """Pop-up table window class for metric display"""

    def __init__(self, results, type):
        """Constructor
        Input: metric results and type"""
        QtWidgets.QTableWidget.__init__(self)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.setFont(font)
        self.results = results
        self.setRowCount(len(self.results))
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Employer", "Score"])
        self.type = type
        self.setWindowTitle(self.type + " Centrality")
        self.direction = True
        self.set_table()

    def set_table(self):
        """Set and display the table"""

        # order and put in a list
        self.display_data = []
        for key, value in sorted(self.results.iteritems(), key=lambda (k, v): (v, k), reverse=self.direction):
            self.display_data.append((key, value))

        # populate and display
        for i, row in enumerate(self.display_data):
            for j, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(col))
                self.setItem(i, j, item)


