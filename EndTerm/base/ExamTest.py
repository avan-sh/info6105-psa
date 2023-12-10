############################################################
# ExamTest.py 
# Test Bench for Exam
# 
###########################################################

############################################################
#  NOTHING CAN BE CHANGED IN THIS FILE
########################################################### 

############################################################
#  All imports here
###########################################################
import sys # For getting Python Version
#from Exam import *

############################################################
#  class  ExamTest
###########################################################
class ExamTest:
    def __init__(self):
        self._n = 0
        self._simple()
        self._hidden()

    def _test1(self, directed: "bool", start: "int", a: "list of list", eans: "bool"):
        ans = []  # list of list
        work = [0]
        show = True
        self._n += 1
        print("----------PROBLEM", self._n, "----------------------")
        e = Exam(self._n, directed, start, a, ans, work, show)
        
    def _simple(self):
        directed = False
        start = 0
        eans = True
        a = [[1, 3], [0, 2], [1, 3], [0, 2]]  # list of list
        self._test1(directed, start, a, eans)

    def _hidden(self):
        print("I will run hidden tests after you submit and make you suffer")
        print("You may get much less than 80. So go to PLAN B")
       


 ############################################################
# MAIN
###########################################################    
def main():
    print("Input is Undirected graph with NO Self loop or  NO parallel edges")
    print(
        "The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them"
    )
    t = ExamTest()
    print("MY NAME AS SHOWN ON CANVAS iS : FILL")
    print("Time  complexity OF MY CODE is : FILL")
    print("Space complexity OF MY CODE is : FILL")
    print("NOTE REAL TEST BENCH WILL BE POSTED AFTER EXAM.")
    print("RUN ON YOUR OWN TO SEE WHERE YOU STAND.")
    print("EXAM ENDS. Cannot post more than once in Canvas")

############################################################
# start up
###########################################################
if (__name__  == '__main__'):
    main()
