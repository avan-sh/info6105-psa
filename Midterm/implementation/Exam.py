############################################################
# Exam.py 
# 
###########################################################

############################################################
#  All imports here
###########################################################

############################################################
#  class  Alg
###########################################################    
class Alg():
    def __init__(self,a:'python list',ans:'python list',maxv:'list of size 1',work:'list of size 1',show:'bool'):
        self._a = a
        self._ans = ans
        self._maxv = maxv
        self._work = work
        self._show = show
        ## You can have your data structure here
        
        ## Nothing can be changed below
        self._exam() #Everything happens in _exam
        check_result(self._a,self._ans,self._maxv[0]) #your answer is checked here

    ############################################################
    #          Nothing can be changed in _exam
    ########################################################### 
    def _exam(self):
        self._alg()
        check_result(self._a,self._ans,self._maxv[0]) #your answer is checked here

    ############################################################
    #          WRITE CODE BELOW
    #  Populate self._maxv and self._work 
    #  if self._show is True, show steps of the algorithm
    ########################################################### 
    def _alg(self):
        print("WRITE CODE HERE. REMOVE THIS LINE")
        

############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################  

############################################################
#  class  Solution
# Nothing can be changed in Solution
###########################################################    
class Solution():
    def XXX(self, nums:'Python list') -> 'int':
        #Nothing can be changedhere
        ans = []
        maxv = [0]
        work = [0]
        t = Alg(nums,ans,maxv,work,False)
        check_result(nums,ans,maxv[0])
        return maxv[0]

############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################  
def check_result(a:'Python list',ans:'Python List',amax:'int'):
    x = sorted(ans)
    t = 0
    for e in x:
        t = t + a[e]
    assert(t == amax)
    # assert you did not break the rule
    lx = len(x)
    for i in range(0,lx-1,2):
        pos1 = x[i]
        pos2 = x[i +1]
        assert(pos2 >= (pos1+1))
 