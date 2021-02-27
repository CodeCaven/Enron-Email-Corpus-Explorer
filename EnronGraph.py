import networkx as nx

class EnronGraph:
    """The graph class for the Enron social network graph"""
    def __init__(self, database):
        self.G = nx.DiGraph()
        self.db = database
        self.out_degree_results = {}
        self.in_degree_results = {}
        self.closeness_results = {}
        self.betweenness_results = {}
        self.ranking_results = {}
        self.eigen_results = {}
        self.add_nodes()
        self.add_edges()
        self.update_graph()

    def add_nodes(self):
        """Creates a node for each employee for the graph"""
        nodes = self.db.get_employees()
        for node in nodes:
            self.G.add_node(node[2], fname=node[0], lname=node[1])

    def add_edges(self):
        """Creates an edge for every message between nodes and counts weight"""
        edge_data = self.db.get_edge_data()
        for data in edge_data:

            if self.is_node(data[0]) and self.is_node(data[1]):
                try:
                    new_weight = self.G[data[0]][data[1]]['weight'] + 1
                    self.G.add_edge(data[0], data[1], weight=new_weight)
                except KeyError:
                    self.G.add_edge(data[0], data[1], weight=1)

    def update_graph(self):
        """Updates the graph by removing edges or nodes according to settings"""
        EDGE_WEIGHT = 5
        for edge in self.G.edges(data=True):
            try:
                self.edge_colour(self.G[edge[0]][edge[1]])
                if self.G[edge[0]][edge[1]]['weight'] < EDGE_WEIGHT or self.G[edge[1]][edge[0]]['weight'] < EDGE_WEIGHT:

                    self.G.remove_edge(edge[0], edge[1])
                    self.G.remove_edge(edge[1], edge[0])
                    if edge[0] == edge[1]: # BUG: remove emails sent to self not working
                        self.G.remove_edge(edge[0], edge[1])
                        self.G.remove_edge(edge[1], edge[0])

            except:
                pass

        # removes single nodes
        for node in self.G.nodes():
            if len(self.G[node]) == 0:
                self.G.remove_node(node)

    def is_node(self, node):
        """Determines if a node is in the graph
        Input: node to check"""
        for email in self.G.nodes():
            if email == node:
                return True
        return False

    # METRICS
    def out_degree(self):
        """Determine the normalised out degree of every node and store"""

        # check for cached results
        if len(self.out_degree_results) > 0:
            return True

        # determine out degree by length of nodes as graphy is an adjacency list
        normal = float(self.G.number_of_nodes()) - 1
        for node in self.G.nodes(data=True):
            name = str(node[1]['fname'] + " " + node[1]['lname'])
            self.out_degree_results[name] = round(len(self.G[node[0]])/normal, 5)
        return True

    def in_degree(self):
        """Determine the in degree of every node in the graph O(N*E) and store"""
        if len(self.in_degree_results) > 0:
            return True

        normal = float(self.G.number_of_nodes()) - 1
        for node in self.G.nodes():
            for edge in self.G[node]:
                try:
                    self.in_degree_results[edge] += 1
                except KeyError:
                    self.in_degree_results[edge] = 1

        self.in_degree_results = self.rename_nodes("IN")
        self.noramlize(normal, self.in_degree_results)
        return True

    def closeness_centrality(self):
        """Determine the normalised closeness centrality of each node"""

        if len(self.closeness_results) > 0:
            return True

        # SETTINGS: normalized and 1 greater paths, eliminates 2 nodes
        for node in self.G.nodes(data=True):
            distances = self.breadth_first_search(node[0])
            closeness = self.closeness_sum(distances)
            if closeness[1] > 1: # at least one path
                name = str(node[1]['fname'] + " " + node[1]['lname'])
                self.closeness_results[name] = round(float(closeness[1])/float(closeness[0]), 5)
        return True

    def breadth_first_search(self, root):
        """Implementation of BFS
        Time: O(N+E) Space:O(N)"""
        Q = [root]
        checked = {}
        dist = {}
        for node in self.G.nodes():
            checked[node] = False
            dist[node] = -1

        dist[root] = 0
        checked[root] = True

        while len(Q) != 0:
            current = Q[0]
            del Q[0]

            for edge in self.G[current]:
                if not checked[edge]:
                    dist[edge] = dist[current] + 1
                    Q.append(edge)
                    checked[edge] = True
        return dist

    def closeness_sum(self, dist_dict):
        """Used by closeness centrality, returns sum of input dict and a count"""
        total = 0
        count = 0
        for dist in dist_dict:
            degree = dist_dict[dist]
            if degree > 0:
                total += degree
                count += 1
        return total, count

    def ranking_metric(self, metric):
        """Calculates and accumulates a ranking score"""
        if metric == "CLOSE":
            dir = True
            self.closeness_centrality()
            results = self.closeness_results
        elif metric == "IN":
            dir = True
            self.in_degree()
            results = self.in_degree_results
        elif metric == "BETWEEN":
            dir = True
            self.brandes_betweenness()
            results = self.betweenness_results
        elif metric == "OUT":
            dir = True
            self.out_degree()
            results = self.out_degree_results
        elif metric == "EIGEN":
            dir = True
            self.eigen_centrality()
            results = self.eigen_results
        else:
            return False

        # order the metric results
        data = []
        for key, value in sorted(results.iteritems(), key=lambda (k, v): (v, k), reverse=dir):
            data.append((key, value))


        score = 10
        for node in data:
            try:
                self.ranking_results[node[0]] += score
            except KeyError:
                self.ranking_results[node[0]] = score
            score -= 1

            if score == 0:
                break

    def all_ranking_metrics(self):
        """Calls ranking_metric() for every metric"""
        if len(self.ranking_results) > 0:
            return True

        self.ranking_metric("CLOSE")
        self.ranking_metric("IN")
        self.ranking_metric("OUT")
        self.ranking_metric("BETWEEN")
        self.ranking_metric("EIGEN")
        return True

    def rename_nodes(self, metric):
        """Rename the nodes for display"""
        if metric == "CLOSE":
            results = self.closeness_results
        elif metric == "IN":
            results = self.in_degree_results
        elif metric == "BETWEEN":
            results = self.betweenness_results
        elif metric == "OUT":
            results = self.out_degree_results
        elif metric == "EIGEN":
            results = self.eigen_results
        else:
            return False

        # rename nodes for display
        for key in results:
            for node in self.G.nodes(data=True):
                if key == node[0]:
                    new_key = node[1]['fname'] + " " + node[1]['lname']
                    results[new_key] = results[key]
                    del results[key]
                    break

        return results

    def brandes_betweenness(self):
        """Brandes betweenness centrality algorithm, see report for complexities and references"""
        if len(self.betweenness_results) > 0:
            return True

        for node in self.G.nodes():
            self.betweenness_results[node] = 0

        for s in self.G.nodes():

            # set up
            S = []
            Q = []
            P = {}
            sigma = {}
            d = {}
            for node in self.G.nodes():
                P[node] = []
                sigma[node] = 0
                d[node] = -1

            d[s] = 0
            sigma[s] = 1
            Q.append(s)
            while len(Q) != 0:
                v = Q[0]
                del Q[0]
                S.append(v)

                for w in self.G[v]:
                    # seen first time
                    if d[w] < 0:
                        Q.append(w)
                        d[w] = d[v] + 1

                    # shortest path to w via v
                    if d[w] == d[v] + 1:
                        sigma[w] = sigma[w] + sigma[v]
                        P[w].append(v)

            # S has nodes in non decreasing order
            delta = {}
            for node in self.G.nodes():
                delta[node] = 0

            while len(S) > 0:
                w = S.pop()
                for v in P[w]:
                    term1 = sigma[v]/sigma[w]
                    term2 = 1 + delta[w]
                    delta[v] = delta[v] + term1*term2

                if w != s:
                    self.betweenness_results[w] = self.betweenness_results[w] + delta[w]

        self.betweenness_results = self.rename_nodes("BETWEEN")
        n = float(self.G.number_of_nodes())
        normal = (n - 1.0) * (n - 2.0)
        self.noramlize(normal, self.betweenness_results)
        return True

    def noramlize(self, normal, results):
        """Normalise a results set by input normal
        Input: normal and results set"""
        for node in results:
            results[node] = round(results[node]/normal, 5)
        return True

    def eigen_centrality(self):
        """Implementation of the Eigenvector Centrality
        NOTE: still in test mode, just run out of time!

        Set to return NetworkX implementation"""
        if len(self.eigen_results) > 0:
            return True

       # power iteration algorithm
        """
        v = {}
        for node in self.G.nodes():
            v[node] = 1

        for i in range(10000):
            w = {}
            for node in self.G.nodes():
                w[node] = 0

            for nodei in self.G.nodes():
                for nodej in self.G[nodei]:
                    w[nodej] = w[nodej] + v[nodei]

            v = w

        total = self.get_sum(v)
        for node in v:
            v[node] = v[node]/total

        print("ME")
        print(v)
        print("\n")
        print("NETWORKX")
        """
        self.eigen_results = nx.eigenvector_centrality(self.G)
        self.eigen_results = self.rename_nodes('EIGEN')
        return True
        #print(['%s %0.2f' % (node, centrality[node]) for node in centrality])

    # DEVELOPMENT
    def print_nodes(self):
        for node in self.G.nodes(data=True):
            print(node)

    def print_edges(self):
        for edge in self.G.edges(data=True):
            print(edge)

    def print_results(self, metric):
        if metric == "IN":
            results = self.in_degree_results
        elif metric == "OUT":
            results = self.out_degree_results
        elif metric == "CLOSE":
            results = self.closeness_results
        elif metric == "BETWEEN":
            results = self.betweenness_results
        elif metric == "ALL":
            results = self.ranking_results
        else:
            return False

        for key in results:
            print(key, results[key])
        print(results)

    def print_sorted_results(self, metric):
        if metric == "IN":
            results = self.in_degree_results
        elif metric == "OUT":
            results = self.out_degree_results
        elif metric == "CLOSE":
            results = self.closeness_results
        elif metric == "BETWEEN":
            results = self.betweenness_results
        elif metric == "ALL":
            results = self.ranking_results
        else:
            return False

        for key, value in sorted(results.iteritems(), key=lambda (k, v): (v, k), reverse=True):
            print "%s: %s" % (key, value)


