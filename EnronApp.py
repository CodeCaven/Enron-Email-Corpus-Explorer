import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainGUI import Ui_EnronEmailCorpus
from EnronDB import EnronDB
from EnronGraph import EnronGraph
from GraphGUI import GraphWindow
from TableGUI import TableWindow
from EnronResults import EnronResults

class EnronApp(Ui_EnronEmailCorpus):
    """The main control class for the application"""

    def __init__(self, dialog, graph, database):
        """Constructor
        Input: a dialog window, graph instance and database instance"""
        Ui_EnronEmailCorpus.__init__(self)
        self.setupUi(dialog)
        self.enrondb = database
        self.enronGraph = graph
        self.view = 1
        self.message_check = False
        self.all_users()

        # Binds to functions
        self.graphButton.clicked.connect(self.display_graph)
        self.pushButton.clicked.connect(self.all_users)
        self.searchButtonSubject.clicked.connect(lambda:self.search(self.searchButtonSubject))
        self.searchButtonMessage.clicked.connect(lambda: self.search(self.searchButtonMessage))
        self.tableWidget.cellClicked.connect(self.cell_clicked)
        self.pushButtonOutDegree.clicked.connect(lambda:self.display_table(self.pushButtonOutDegree))
        self.pushButtonInDegree.clicked.connect(lambda:self.display_table(self.pushButtonInDegree))
        self.pushButtonCloseness.clicked.connect(lambda: self.display_table(self.pushButtonCloseness))
        self.pushButtonBetween.clicked.connect(lambda: self.display_table(self.pushButtonBetween))
        self.rankingpushButton.clicked.connect(lambda: self.display_table(self.rankingpushButton))
        self.pushButtonEigen.clicked.connect(lambda: self.display_table(self.pushButtonEigen))
        self.pushButtonWordCloud.clicked.connect(self.display_cloud)

    def get_emails(self, row):
        """Gets the emails of a user by email address
        Input: cell row number"""
        self.emails = self.enrondb.get_user_messages_by_email(self.employees[row][2])

        # display in main view window
        if len(self.emails) > 0:
            self.tableWidget.setRowCount(len(self.emails))
            self.tableWidget.setColumnCount(len(self.emails[0]))

            for i, row in enumerate(self.emails):
                for j, col in enumerate(row):
                    if j <= len(self.emails[0]) - 1:
                        item = QtWidgets.QTableWidgetItem(col)
                        self.tableWidget.setItem(i, j, item)
        else:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("No Results Found"))

        # table data
        self.tableWidget.setHorizontalHeaderLabels(["Sender", "Receiver", "Date", "Time", "Email Subject"])
        self.tableWidget.resizeColumnsToContents()
        self.resultslengthlabel.clear()
        self.resultslengthlabel.setText("Search Results " + str(len(self.emails)))
        self.view = 1

    def all_users(self):
        """Gets all the Enron employees"""

        # diaplay in main view window if not already in it
        if self.view:
            self.employees = self.enrondb.get_employees()
            self.tableWidget.setRowCount(len(self.employees))
            self.tableWidget.setColumnCount(len(self.employees[0]))

            for i, row in enumerate(self.employees):
                for j, col in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(col)
                    self.tableWidget.setItem(i, j, item)

            self.tableWidget.setHorizontalHeaderLabels(["First Name", "Last Name", "Email Address"])

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.resultslengthlabel.clear()
            self.view = 0

    def display_graph(self):
        """Display social network graph"""
        graph_window = GraphWindow(self.enronGraph, None, True)
        graph_window.show()

    def cell_clicked(self, row):
        """Logic control function determines what is in view window by view variable
        Input: cell row number"""
        if not self.view:
            self.get_emails(row)
            self.view = 1
        else:
            self.get_message(row)

    def get_message(self, row):
        """Gets a message and populates the message display
        Input: cell row number"""
        self.message_check = True
        self.message_id = self.emails[row][5]
        self.message = self.enrondb.get_message_by_rid(self.message_id)

        # FROM
        self.textEditFrom.clear()
        self.textEditFrom.insertPlainText(self.message[0][0])

        # TO
        self.textEditTo.clear()
        self.textEditTo.insertPlainText(self.message[0][1])

        # SUBJECT
        self.textEditSubject.clear()
        self.textEditSubject.insertPlainText(self.message[0][3])

        # MESSAGE
        self.textEditMessage.clear()
        self.textEditMessage.insertPlainText(self.message[0][6])

        # DATE
        self.labelDateTime.clear()
        self.labelDateTime.setText(str(self.message[0][4]))

        # TIME
        self.labelDateTime_2.clear()
        self.labelDateTime_2.setText(str(self.message[0][5]))

        # TYPE CC,BCC,TO
        self.labelType_2.clear()
        self.labelType_2.setText(self.message[0][2])

    def display_table(self, b):
        """Logic control for metric tables
        Input: button clicked"""

        #start = time.time()
        button = b.text()
        if button == "Out Degree":
            self.enronGraph.out_degree()
            self.out_table = TableWindow(self.enronGraph.out_degree_results, "Out Degree")
            self.out_table.show()
        elif button == "In Degree":
            self.enronGraph.in_degree()
            self.in_table = TableWindow(self.enronGraph.in_degree_results, "In Degree")
            self.in_table.show()
        elif button == "Closeness":
            self.enronGraph.closeness_centrality()
            self.close_table = TableWindow(self.enronGraph.closeness_results, "Closeness")
            self.close_table.show()
        elif button == "Betweenness":
            self.enronGraph.brandes_betweenness()
            self.between_table = TableWindow(self.enronGraph.betweenness_results, "Betweenness")
            self.between_table.show()
        elif button == "Main Actors":
            self.enronGraph.all_ranking_metrics()
            self.eigen_table = TableWindow(self.enronGraph.ranking_results, "Main Actors")
            self.eigen_table.show()
        elif button == "Eigenvector":
            self.enronGraph.eigen_centrality()
            self.eigen_table = TableWindow(self.enronGraph.eigen_results, "Eigenvector")
            self.eigen_table.show()
        else:
            print("WTF?????")
            pass

        # left in timing logic for testing to show example use
        #end = time.time()
        #print(button + " " + str(end-start))

    def search(self, button):
        """Performs a NLP search and displays results to main view window"
        Input: button clicked"""

        # get search results
        search_text = self.searchtextEdit.toPlainText()
        if button.text() == "MESSAGE":
            self.emails = self.enrondb.full_text_search_message(search_text)
        else:
            self.emails = self.enrondb.full_text_search_subject(search_text)

        # display search results
        if len(self.emails) > 0:
            self.tableWidget.setRowCount(len(self.emails))
            self.tableWidget.setColumnCount(len(self.emails[0]))

            for i, row in enumerate(self.emails):
                for j, col in enumerate(row):
                    if j <= len(self.emails[0]) - 1:
                        item = QtWidgets.QTableWidgetItem(col)
                        self.tableWidget.setItem(i, j, item)
        else:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("No Results Found"))

        self.tableWidget.setHorizontalHeaderLabels(["Sender", "Receiver", "Date", "Time", "Email Subject"])
        self.tableWidget.resizeColumnsToContents()

        self.resultslengthlabel.clear()
        self.resultslengthlabel.setText("Search Results " + str(len(self.emails)))
        self.view = 1

    def display_cloud(self):
        """Displays the message tag cloud if a message is in the fields"""
        if self.message_check:
            cloud_window = GraphWindow(None, self.message[0][6], False)
            cloud_window.show()


if __name__ == '__main__':

    # scripting logic to run the app from command line
    # eg. python EnronApp.py root abcd1234 db run

    # create app and databasee instance
    app = QtWidgets.QApplication(sys.argv)
    session = EnronDB(sys.argv[1], sys.argv[2], sys.argv[3])

    # check args for results or run app
    if len(sys.argv) == 5:
        window = QtWidgets.QMainWindow()
        if sys.argv[4] == 'run':
            print("Please wait while the data is loaded...this may take a couple of minutes")
            #app_graph = TestGraph(50, 600)
            app_graph = EnronGraph(session)
            prog = EnronApp(window, app_graph, session)

            window.show()
            sys.exit(app.exec_())
        elif sys.argv[4] == 'results':
            print("Generating results this will take a few minutes")
            res = EnronResults(session)
        else:
            print("Not a valid command, please use run or results")
    else:
        print("Incorrect number of inputs, please refer to run instructions")




