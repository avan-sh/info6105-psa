
class Graph:
    ##GRAPH DATA STRUCTURE
    def __init__(self):
        self._g = None  # networkx graph

    ############################################################
    # All Public routines. YOU SHOULD ONLY CALL THESE ROUTINES
    ###########################################################
    def is_directed_graph(self) -> "bool":
        if self._g.is_directed():
            return True
        return False

    def is_undirected_graph(self) -> "bool":
        return not (self._g.is_directed_graph())

    def is_weighted_graph(self) -> "bool":
        return nx.is_weighted(self._g)

    def get_graph_type(self) -> "GraphType":
        weighted = self.is_weighted_graph()
        if self.is_directed_graph():
            if weighted:
                return GraphType.WEIGHTED_DIRECTED
            else:
                return GraphType.DIRECTED
        if weighted:
            return GraphType.WEIGHTED_UNDIRECTED
        return GraphType.UNDIRECTED

    def get_graph_type_as_string(self) -> "string":
        t = self.get_graph_type()
        if t == GraphType.UNDIRECTED:
            return "UNDIRECTED GRAPH"
        if t == GraphType.DIRECTED:
            return "DIRECTED GRAPH"
        if t == GraphType.WEIGHTED_UNDIRECTED:
            return "WEIGHTED_UNDIRECTED GRAPH"
        if t == GraphType.WEIGHTED_DIRECTED:
            return "WEIGHTED_DIRECTED GRAPH"
        return "NONE"

    def get_node_name(self, n: "node") -> "string":
        return str(n)

    def get_edge_weight(self, f: "node1", t: "node2") -> "weight as a float":
        w = 0
        if self.is_weighted_graph():
            w = self._g.edges[f, t]["weight"]
        return w

    def get_numV(self) -> "int":
        l = self._g.number_of_nodes()
        return l

    def get_numE(self) -> "int":
        l = self._g.number_of_edges()
        return l

    def fanouts_of_node(self, n: "node") -> "list of nodes":
        if self.is_directed_graph():
            a = list(self._g.successors(n))
        else:
            a = self._g.adj[n]
        return a

    def fanins_of_node(self, n: "node") -> "list of nodes":
        assert self.is_directed_graph()
        a = list(self._g.predecessors(n))
        return a

    def num_fanout(self, n: "node") -> "int":
        a = self.fanouts_of_node(n)
        s = len(a)
        return s

    def num_fanin(self, n: "node") -> "int":
        a = self.fanins_of_node(n)
        s = len(a)
        return s

    def list_of_nodes(self) -> "list of nodes":
        l = list(self._g.nodes())
        return l

    def has_node(self, name_of_the_node: "string") -> "bool":
        l = list(self._g.nodes())
        for n in l:
            if n == name_of_the_node:
                return True
        return False

    def dump(self, name):
        print("------------", name, "------------ ")
        s = self.get_graph_type_as_string()

        print(s)
        print("Num Vertices =", self.get_numV())
        print("Num Edges    =", self.get_numE())
        nodes = self.list_of_nodes()
        for n in nodes:
            print(n, "Fanouts: ", end="")
            fanouts_of_n = self.fanouts_of_node(n)
            f = len(fanouts_of_n)
            if f == 0:
                print("NONE")
            else:
                j = 0
                for nf in fanouts_of_n:
                    if j < f - 1:
                        print(nf, ",", sep="", end="")
                    else:
                        print(nf)
                    j = j + 1
            if self.is_directed_graph():
                print(n, "Fanins: ", end="")
                fanins_of_n = self.fanins_of_node(n)
                f = len(fanins_of_n)
                if f == 0:
                    print("NONE")
                else:
                    j = 0
                    for nf in fanins_of_n:
                        if j < f - 1:
                            print(nf, ",", sep="", end="")
                        else:
                            print(nf)
                        j = j + 1

    ##########################################################
    # Nothing can be changed
    # TIME: THETA(V + E)
    # SPACE: THETA(V)
    ##########################################################
    def assert_dfs_passed(self, has_loop: "bool", dfs_order: "list of nodes"):
        t = self.get_graph_type()
        if (t == GraphType.UNDIRECTED) or (t == GraphType.WEIGHTED_UNDIRECTED):
            return
        if has_loop == False:
            set_of_visited_nodes = set()
            for n in dfs_order:
                ## Go on fanins of node
                fanins_of_n = self.fanins_of_node(n)
                for nf in fanins_of_n:
                    must_be_there = nf in set_of_visited_nodes  # find in THETA(1)
                    assert must_be_there
                set_of_visited_nodes.add(n)  # add in THETA(1)
            # All nodes must be visited
            assert len(set_of_visited_nodes) == self.get_numV()
            print("DFS ASSERT PASSED")

    ############################################################
    # All Private routines. YOU SHOULD NOT CALL THESE ROUTINES
    ###########################################################

    ############################################################
    ## All the routines written by students
    ##########################################################
    def build_graph(self, f: "file name", d: "bool"):
        b = GraphBuilder(self, f, d)  # d True means directed. False means undirected

    def write_dot(self, f):
        b = GraphDot(self, f)

    def show_dot_file(self, filename: "string"):
        with open(filename) as f:
            dot_graph = f.read()
        return dot_graph

    def dfs_using_time_stamp(
        self,
        gname: "string",
        dfs_order: "list of nodes",
        has_loop: "List of size 1 Boolean",
        work: "list of size 1",
        dfs_dot_output_file: "Traversal file name",
    ):

        b = GraphDfsUsingTimeStamp(
            self, gname, dfs_order, has_loop, work, dfs_dot_output_file
        )

    def Dijkstra(
        self,
        gname: "string",
        start_city: "String",
        cost: "list of cost",  # Caller will Fill. cost from start city to all other city.If not reachable -1
        work: "list of size 1",
        dijkstra_traversal_dot_output_file: "Traversal file name",
        show: "bool",
    ):
        b = GraphDijkstra(
            self,
            gname,
            start_city,
            cost,
            work,
            dijkstra_traversal_dot_output_file,
            show,
        )
