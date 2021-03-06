from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EnronEmailCorpus(object):

    """Main Window Created by: PyQt5 UI code generator 5.6 no changes made"""
    def setupUi(self, EnronEmailCorpus):
        EnronEmailCorpus.setObjectName("EnronEmailCorpus")
        EnronEmailCorpus.resize(973, 838)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        EnronEmailCorpus.setFont(font)
        EnronEmailCorpus.setStyleSheet("\n"
"\n"
"font: 8pt \"MV Boli\";\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(EnronEmailCorpus)
        self.centralwidget.setObjectName("centralwidget")
        self.HeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeadingLabel.setGeometry(QtCore.QRect(290, 0, 421, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HeadingLabel.setFont(font)
        self.HeadingLabel.setStyleSheet("font: 26pt \"MV Boli\";\n"
"text-shadow: 2px 2px;")
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.graphButton = QtWidgets.QPushButton(self.centralwidget)
        self.graphButton.setGeometry(QtCore.QRect(730, 140, 131, 31))
        self.graphButton.setStyleSheet("background-color:rgb(190, 230, 255);")
        self.graphButton.setObjectName("graphButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 100, 461, 191))
        self.tableWidget.setStyleSheet("border-width: 1px;\n"
"\n"
"border-radius: 3%;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 100, 131, 31))
        self.pushButton.setStyleSheet("background-color:rgb(190, 230, 255);")
        self.pushButton.setObjectName("pushButton")
        self.textEditFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditFrom.setGeometry(QtCore.QRect(220, 380, 551, 31))
        self.textEditFrom.setStyleSheet("border-width: 2px;\n"
"border-style: solid;\n"
"border-radius: 5%;")
        self.textEditFrom.setObjectName("textEditFrom")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEditTo = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditTo.setGeometry(QtCore.QRect(220, 420, 551, 31))
        self.textEditTo.setStyleSheet("border-width: 2px;\n"
"border-style: solid;\n"
"border-radius: 5%;")
        self.textEditTo.setObjectName("textEditTo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEditSubject = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSubject.setGeometry(QtCore.QRect(220, 460, 551, 31))
        self.textEditSubject.setStyleSheet("border-width: 2px;\n"
"border-style: solid;\n"
"border-radius: 5%;")
        self.textEditSubject.setObjectName("textEditSubject")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 460, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEditMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditMessage.setGeometry(QtCore.QRect(220, 510, 551, 191))
        self.textEditMessage.setStyleSheet("border-width: 2px;\n"
"border-style: solid;\n"
"border-radius: 5%;")
        self.textEditMessage.setObjectName("textEditMessage")
        self.labelDateTime = QtWidgets.QLabel(self.centralwidget)
        self.labelDateTime.setGeometry(QtCore.QRect(220, 340, 131, 16))
        self.labelDateTime.setText("")
        self.labelDateTime.setObjectName("labelDateTime")
        self.labelType = QtWidgets.QLabel(self.centralwidget)
        self.labelType.setGeometry(QtCore.QRect(690, 430, 61, 20))
        self.labelType.setText("")
        self.labelType.setObjectName("labelType")
        self.labelType_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelType_2.setGeometry(QtCore.QRect(700, 350, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelType_2.setFont(font)
        self.labelType_2.setText("")
        self.labelType_2.setObjectName("labelType_2")
        self.pushButtonOutDegree = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOutDegree.setGeometry(QtCore.QRect(170, 140, 81, 31))
        self.pushButtonOutDegree.setStyleSheet("background-color:rgb(85, 170, 127);")
        self.pushButtonOutDegree.setObjectName("pushButtonOutDegree")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 70, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButtonInDegree = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInDegree.setGeometry(QtCore.QRect(170, 100, 81, 31))
        self.pushButtonInDegree.setStyleSheet("background-color:rgb(85, 170, 127);")
        self.pushButtonInDegree.setObjectName("pushButtonInDegree")
        self.pushButtonCloseness = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCloseness.setGeometry(QtCore.QRect(170, 180, 81, 31))
        self.pushButtonCloseness.setStyleSheet("background-color:rgb(85, 170, 127);")
        self.pushButtonCloseness.setObjectName("pushButtonCloseness")
        self.pushButtonBetween = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBetween.setGeometry(QtCore.QRect(170, 220, 81, 31))
        self.pushButtonBetween.setStyleSheet("background-color:rgb(85, 170, 127);")
        self.pushButtonBetween.setObjectName("pushButtonBetween")
        self.rankingpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rankingpushButton.setGeometry(QtCore.QRect(730, 180, 131, 31))
        self.rankingpushButton.setStyleSheet("background-color:rgb(190, 230, 255);")
        self.rankingpushButton.setObjectName("rankingpushButton")
        self.searchtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.searchtextEdit.setGeometry(QtCore.QRect(360, 50, 251, 31))
        self.searchtextEdit.setStyleSheet("border-width: 2px;\n"
"border-style: solid;\n"
"border-radius: 5%;")
        self.searchtextEdit.setObjectName("searchtextEdit")
        self.searchButtonMessage = QtWidgets.QPushButton(self.centralwidget)
        self.searchButtonMessage.setGeometry(QtCore.QRect(630, 50, 91, 31))
        self.searchButtonMessage.setStyleSheet("background-color:rgba(255, 18, 10, 210);")
        self.searchButtonMessage.setDefault(False)
        self.searchButtonMessage.setObjectName("searchButtonMessage")
        self.resultslengthlabel = QtWidgets.QLabel(self.centralwidget)
        self.resultslengthlabel.setGeometry(QtCore.QRect(440, 310, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resultslengthlabel.setFont(font)
        self.resultslengthlabel.setText("")
        self.resultslengthlabel.setObjectName("resultslengthlabel")
        self.searchButtonSubject = QtWidgets.QPushButton(self.centralwidget)
        self.searchButtonSubject.setGeometry(QtCore.QRect(260, 50, 81, 31))
        self.searchButtonSubject.setStyleSheet("background-color:rgba(255, 18, 10, 210);")
        self.searchButtonSubject.setDefault(False)
        self.searchButtonSubject.setObjectName("searchButtonSubject")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 340, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 360, 47, 13))
        self.label_7.setObjectName("label_7")
        self.labelDateTime_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelDateTime_2.setGeometry(QtCore.QRect(220, 360, 131, 16))
        self.labelDateTime_2.setText("")
        self.labelDateTime_2.setObjectName("labelDateTime_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 350, 47, 16))
        self.label_8.setObjectName("label_8")
        self.pushButtonEigen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEigen.setGeometry(QtCore.QRect(170, 260, 81, 31))
        self.pushButtonEigen.setStyleSheet("background-color:rgb(85, 170, 127);")
        self.pushButtonEigen.setObjectName("pushButtonEigen")
        self.pushButtonWordCloud = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonWordCloud.setGeometry(QtCore.QRect(430, 710, 131, 23))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonWordCloud.setFont(font)
        self.pushButtonWordCloud.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButtonWordCloud.setObjectName("pushButtonWordCloud")
        EnronEmailCorpus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EnronEmailCorpus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 22))
        self.menubar.setObjectName("menubar")
        EnronEmailCorpus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EnronEmailCorpus)
        self.statusbar.setObjectName("statusbar")
        EnronEmailCorpus.setStatusBar(self.statusbar)

        self.retranslateUi(EnronEmailCorpus)
        QtCore.QMetaObject.connectSlotsByName(EnronEmailCorpus)

    def retranslateUi(self, EnronEmailCorpus):
        _translate = QtCore.QCoreApplication.translate
        EnronEmailCorpus.setWindowTitle(_translate("EnronEmailCorpus", "MainWindow"))
        self.HeadingLabel.setText(_translate("EnronEmailCorpus", "ENRON EMAIL CORPUS"))
        self.graphButton.setText(_translate("EnronEmailCorpus", "Social Network Graph"))
        self.pushButton.setText(_translate("EnronEmailCorpus", "SeeAllEnronStaff"))
        self.label.setText(_translate("EnronEmailCorpus", "FROM:"))
        self.label_2.setText(_translate("EnronEmailCorpus", "TO:"))
        self.label_3.setText(_translate("EnronEmailCorpus", "SUBJECT:"))
        self.pushButtonOutDegree.setText(_translate("EnronEmailCorpus", "Out Degree"))
        self.label_4.setText(_translate("EnronEmailCorpus", "METRICS"))
        self.pushButtonInDegree.setText(_translate("EnronEmailCorpus", "In Degree"))
        self.pushButtonCloseness.setText(_translate("EnronEmailCorpus", "Closeness"))
        self.pushButtonBetween.setText(_translate("EnronEmailCorpus", "Betweenness"))
        self.rankingpushButton.setText(_translate("EnronEmailCorpus", "Main Actors"))
        self.searchButtonMessage.setText(_translate("EnronEmailCorpus", "MESSAGE"))
        self.searchButtonSubject.setText(_translate("EnronEmailCorpus", "SUBJECT"))
        self.label_6.setText(_translate("EnronEmailCorpus", "DATE:"))
        self.label_7.setText(_translate("EnronEmailCorpus", "TIME:"))
        self.label_8.setText(_translate("EnronEmailCorpus", "TYPE:"))
        self.pushButtonEigen.setText(_translate("EnronEmailCorpus", "Eigenvector"))
        self.pushButtonWordCloud.setText(_translate("EnronEmailCorpus", "Generate Word Cloud"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnronEmailCorpus = QtWidgets.QMainWindow()
    ui = Ui_EnronEmailCorpus()
    ui.setupUi(EnronEmailCorpus)
    EnronEmailCorpus.show()
    sys.exit(app.exec_())

