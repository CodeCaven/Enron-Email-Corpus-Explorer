import nltk
from nltk.metrics import BigramAssocMeasures
from EnronGraph import EnronGraph

class EnronResults:

    """Class to output a full results set for the project
    Output: enron_results.txt"""

    def __init__(self, database):
        """Constructor
        Input: valid enron db"""
        self.enrondb = database
        self.graph = EnronGraph(database)
        self.actors = []
        self.filename = "enron_results.txt"
        self.run()

    def get_actors(self):
        """Get all the top ranked actors"""
        self.graph.all_ranking_metrics()
        count = 1
        for key, value in sorted(self.graph.ranking_results.iteritems(), key=lambda (k, v): (v, k), reverse=True):
            self.actors.append(key)
            if count == 10:
                break
            count += 1

    def write_metric(self, metric):
        """Write to file the input metric results"""
        if metric == "IN-DEGREE":
            results = self.graph.in_degree_results
        elif metric == "OUT-DEGREE":
            results = self.graph.out_degree_results
        elif metric == "CLOSENESS":
            results = self.graph.closeness_results
        elif metric == "BETWEENNESS":
            results = self.graph.betweenness_results
        elif metric == "RANKING":
            results = self.graph.ranking_results
        elif metric == "EIGENVECTOR":
            results = self.graph.eigen_results
        else:
            return False

        f = open(self.filename, 'w')
        f.write("\n")
        f.write(metric + "\n")

        for key, value in sorted(results.iteritems(), key=lambda (k, v): (v, k), reverse=True):
            f.write(key + " " + str(value) + "\n")

        f.write("\n")
        f.close()

    def write_actors(self):
        """Write to file the top actors"""
        f = open(self.filename, 'a')
        f.write("****TOP 10 ACTORS****\n")
        for actor in self.actors:
            f.write(actor + "\n")
        f.write("\n")
        f.close()

    def get_tokens(self, actor):
        """Get tokens for NLP"""
        name = actor.split()

        results = self.enrondb.get_message_body_by_name(name[0], name[1])
        tokens = []
        for result in results:
            words = result[0].split()
            for word in words:
                new_word = word.lower()
                if len(new_word) < 15:
                    tokens.append(new_word)

        return tokens

    def write_keywords(self, tokens, actor, f):
        """NLP using n-grams for collocations"""
        # code here due to Russel (references in report)
        N = 15
        finder = nltk.BigramCollocationFinder.from_words(tokens)
        finder.apply_freq_filter(2)
        finder.apply_word_filter(lambda w: w in nltk.corpus.stopwords.words('english'))
        scorer = BigramAssocMeasures.jaccard
        collocations = finder.nbest(scorer, N)

        f.write(actor + "\n")
        for collocation in collocations:
            c = ' '.join(collocation)
            f.write(c + "\n")
        f.write("\n")

    def write_all_actors_keyword(self):
        """Write keywords from NLP to file"""
        f = open(self.filename, 'a')
        f.write("****KEYWORDS BY TOP ACTORS****\n")
        for actor in self.actors:
            tokens = self.get_tokens(actor)
            self.write_keywords(tokens, actor, f)
        f.close()

    def run(self):
        """Logic function to create the file"""
        self.get_actors()
        self.write_actors()
        f = open(self.filename, 'a')
        f.write("***METRICS*** \n")
        f.close()
        self.write_metric("IN-DEGREE")
        self.write_metric("OUT-DEGREE")
        self.write_metric("CLOSENESS")
        self.write_metric("BETWEENNESS")
        self.write_metric("EIGENVECTOR")
        self.write_metric("RANKING")
        self.write_all_actors_keyword()


