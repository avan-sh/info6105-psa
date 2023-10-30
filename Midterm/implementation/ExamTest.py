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
from Exam import *


############################################################
#  class  test factorial
###########################################################    
class Test_exam():
    def __init__(self):
        self._test_simple()
        self._test_hidden()

    def _test1(self,a:'list', e:'int')->'void':
        ans = []
        maxv = [0]
        work = [0]
        Alg(a,ans,maxv,work,True)
        assert(maxv[0] == e)
        

    def _test_simple(self):
        a = [1,2,4]
        self._test1(a,5)
        a =  [1,2,3,4,5,6,7,8,9,10]
        self._test1(a,30)
        a = [1,2,3,1]
        self._test1(a,4)
        a = [2,7,9,3,1]
        self._test1(a,12)

        a = [2, 7, 1, 8, 4]
        self._test1(a, 15)

    def _test_hidden(self):
        print("TEST PASSED- Do you belive???.")
        print("I will run hidden tests after you submit and I will make you suffer")
        print("Build some test cases and make sure you are right")

############################################################
# MAIN
###########################################################    
def main():
    t = Test_exam()
    print("MY NAME AS SHOWN ON CANVAS iS : FILL") 
    print("Time  complexity OF MY CODE is : FILL") 
    print("Space complexity OF MY CODE is : FILL") ;
    print("NOTE REAL TEST BENCH WILL BE POSTED AFTER EXAM.") 
    print("RUN ON YOUR OWN TO SEE WHERE YOU STAND.") 
    print("EXAM ENDS. Cannot post more than once in Canvas");

############################################################
# start up
###########################################################
if (__name__  == '__main__'):
    main()
