class WriteDot:
    def __init__(
        self, d: "bool", start: "int", a: "list of list", f: "filename"
    ) -> "None":

        print("In graph", f)
        print("ZERO Marks will be given if you don't write code here")


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
        print("ZERO marks will be given if you don't write code here")

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
            outputDir = "C:\\scratch\\outputs\\exam\\"
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
        print("remove this line and write")
        print("ZERO marks will be given if you don't write code")
        print(self._a)