class WriteDot:
    def __init__(
        self, d: "bool", start: "int", a: "list of list", f: "filename"
    ) -> "None":

        print("In graph", f)
        file_writer = open(f, "w")
        file_writer.write("digraph g {\n")
        file_writer.write("edge [dir=none, color=red]\n")
        visited_pairs = set()
        output_adj_list = [a[i] for i in range(start,len(a))]
        label_str = f"label = \"{output_adj_list}\""
        for node in range(start, len(a)):
            for neighbor in a[node]:
                if (node, neighbor) not in visited_pairs:
                    visited_pairs.add((node, neighbor))
                    visited_pairs.add((neighbor, node))
                    file_writer.write("\t" + str(node) + "->" + str(neighbor) + ";\n")
            # label_str += str(a[node]) + " "
        file_writer.write(f"\t{label_str}\n")
        file_writer.write("}\n")
        file_writer.close()




class Write2Dot:
    def __init__(
        self,
        d: "bool",
        start: "int",
        a: "list of list",
        ans: "list of list",
        f: "filename",
    ) -> "None":
        print("out graph", f)
        self.file_writer = open(f, "w")
        self._write_graph_start(self.file_writer)
        if ans != []:
            self._write_cluster(self.file_writer, ans[0], "RED")
            self._write_cluster(self.file_writer, ans[1], "BLUE")
            self._write_edges(self.file_writer, ans, a)
            self._write_label(self.file_writer, ans)
        self._write_graph_end(self.file_writer)
        self.file_writer.close()
    
    
    def _write_graph_start(self, file_writer):
        """
        graph g {
	        overlap=false; splines=true
	        edge [style=dotted, weight=10, len=.2]
        """
        file_writer.write("graph g {\n")
        file_writer.write("\toverlap=false; splines=true\n")
        file_writer.write("\tedge [style=dotted, weight=10, len=.2]\n")
        pass

    def _write_cluster(self, file_writer, cluster, color):
        """
        subgraph cluster_RED {
            RED [pos="-1,0!", color=red]
            0 -- RED
            2 -- RED
        }
        """
        file_writer.write(f"\tsubgraph cluster_{color} {{\n")
        file_writer.write(f"\t\t{color} [pos=\"-1,0!\", color={color.lower()}]\n")
        for node in cluster:
            file_writer.write(f"\t\t{node} -- {color}\n")
        file_writer.write("\t}\n")
        pass

    def _write_edges(self, file_writer, ans, adj_list):
        """
        edge [style="", weight=1, len=1]
        0--1
        0--3
        1--2
        2--3
        """
        file_writer.write("\tedge [style=\"\", weight=1, len=1]\n")
        visited_pairs = set()
        for cluster in ans:
            for node in cluster:
                for neighbor in adj_list[node]:
                        if (node, neighbor) not in visited_pairs:
                            visited_pairs.add((node, neighbor))
                            visited_pairs.add((neighbor, node))
                            file_writer.write(f"\t{node}--{neighbor}\n")
        pass

    def _write_label(self, file_writer, ans):
        # label= "[0, 2][1, 3]"
        label_str = f"label = \"{ans}\""
        file_writer.write(f"\t{label_str}\n")
        pass

    def _write_graph_end(self, file_writer):
        file_writer.write("}\n")
        pass


############################################################
# Exam.py 
# 
###########################################################

############################################################
#  All imports here
###########################################################
class Exam:
    def __init__(
        self,
        num: "int",
        d: "bool",
        start: "int",
        a: "list of list",
        ans: "list of list",
        work: "list of size 1",
        show: "bool",
    ):
        self._num = num
        self._dir = d
        self._start = start
        self._a = a
        self._ans = ans
        self._work = work
        self._show = show
        ## You can have your data structure here
        

        ## Nothing can be changed below
        if self._show:
            # CHANGE THIS. MUST post all pdf in Canavs as a ZIP file
            # DO NOT UPLOAD DOT FILES
            outputDir = "/Users/avaneesh/GRAD/INFO6205-PSA/EndTerm/s1/"
            f = outputDir + str(self._num) + "in.dot"
            e = WriteDot(self._dir, self._start, self._a, f)
        self._alg()  # Everything happens in _alg
        if self._show:
            f = outputDir + str(self._num) + "out.dot"
            e = Write2Dot(self._dir, self._start, self._a, self._ans, f)

    ############################################################
    #  Write your code below
    ###########################################################
    def _alg(self) -> "None":
        print(self._a)

        #TODO: Handle case for start=1
        num_nodes = len(self._a)
        is_partionable = True
        visited = set()
        is_red = [False] * len(self._a)
        queue = []

        for i in range(len(self._a)):
            if i in visited:
                continue

            queue = []
            queue.append(i)
            visited.add(i)

            while queue and is_partionable:
                node = queue.pop(0)
                for neighbor in self._a[node]:
                    if neighbor in visited:
                        if is_red[neighbor] == is_red[node]:
                            is_partionable = False
                            break
                    else:
                        is_red[neighbor] = not is_red[node]
                        queue.append(neighbor)
                        visited.add(neighbor)
        if is_partionable:
            output = [[i  for i in range(num_nodes) if is_red[i] == True], [i for i in range(num_nodes) if is_red[i] == False]]
            for group in output: self._ans.append(group)
            print(output)
        else:
            output = []
            print("Not Partionable")
            print(output)    
