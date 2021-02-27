from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import networkx as nx
from wordcloud import WordCloud

class GraphWindow(QDialog):
    """Pop-up graph window for message cloud and network graph"""

    def __init__(self, graph, text, setting, parent=None):
        """Constructor
        Input:"""
        super(GraphWindow, self).__init__(parent)

        self.graph = graph
        self.text = text

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # draw the graph or cloud
        if setting:
            self.draw_graph()
        else:
            self.draw_cloud()


    def draw_graph(self):
        """Draw the network graph"""
        pos = nx.spring_layout(self.graph.G, scale=2)
        nx.draw_networkx_nodes(self.graph.G, pos, node_size=30)
        nx.draw_networkx_edges(self.graph.G, pos, arrows=False)
        self.canvas.draw()

    def draw_cloud(self):
        """Draw the message cloud"""
        wordcloud = WordCloud(
            relative_scaling=1.0,
            stopwords={'to', 'of'}
        ).generate(self.text)
        plt.imshow(wordcloud)
        plt.axis("off")
        self.canvas.draw()