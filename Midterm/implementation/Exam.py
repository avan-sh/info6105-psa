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
        self._max_score = [None] * len(a) #store tuples of max_val if the current value is not picked & picked
        self._prev_choice = [None] * len(a) # store tuples of prev_choice if the current value is not picked & picked
        # second element(index 0) of each tuple in _prev_choice is always zero
        
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
    def _increment_work(self):
        self._work[0] = self._work[0] + 1
    
    def _alg(self):
        print("\n----------------------------\n")
        print(f"Calculating for {self._a}") if self._show else None
        num_elements  = len(self._a)
        if num_elements == 0:
            self._maxv[0] = 0 # no elements no max
            self._increment_work()
            return
        elif num_elements == 1:
            self._maxv[0] = self._a[0]
            self._ans.append(0) # only one element, so pick it
            self._increment_work()
            print(f"added the only element present as max, ") if self._show else None
            print(f"max_sum: {self._maxv[0]}, max_indices: {self._ans}") if self._show else None
            return
        elif num_elements == 2:
            self._increment_work()
            if self._a[0] > self._a[1]:
                self._maxv[0] = self._a[0]
                self._ans.append(0)
            else:
                self._maxv[0] = self._a[1]
                self._ans.append(1)
            print(f"added max of 2 elements as max, ") if self._show else None
            print(f"max_sum: {self._maxv[0]}, max_indices: {self._ans}") if self._show else None
            return

        # print("WRITE CODE HERE. REMOVE THIS LINE")
        self._max_score[0] = (0,self._a[0]) # if not picked =0, if picked=val
        self._prev_choice[0] = (0, 0) # index 0 doesn't matter
        print(f"   val {self._a[0]} at ind 0, if curr not selected (max:{0} select_prev:{False}), if selected:(max {self._a[0]})") if self._show else None

        # populate max_score and prev_choice
        for i in range(1, num_elements):
            curr_val = self._a[i]
            prev_max_possibilities = self._max_score[i-1]
            # if current not picked, pick max of prev possibilities and the index of max of prev_possibilities
            if prev_max_possibilities[0] > prev_max_possibilities[1]:
                not_picked_max = prev_max_possibilities[0]
                prev_picked = 0
            else: 
                not_picked_max = prev_max_possibilities[1]
                prev_picked = 1
            # if current is picked, pick prev_max_possibilities index 0 (prev not picked) + curr_val
            picked_max = prev_max_possibilities[0] + curr_val
            print(f"   val {curr_val} at ind {i}, if curr not selected (max:{not_picked_max} select_prev:{bool(prev_picked)}) , if selected:(max {picked_max})") if self._show else None
            self._max_score[i] = (not_picked_max, picked_max)
            self._prev_choice[i] = (prev_picked, 0)

        max_val = max(self._max_score[num_elements-1])
        self._maxv[0] = max_val

        # populate indices
        picked_indices = [0] * num_elements
        last_element_vals = self._max_score[num_elements-1]
        prev_ind_picked_flag = 1 if last_element_vals[1] > last_element_vals[0] else 0
        curr_index = num_elements - 1
        while curr_index >= 0:
            element_picked_flag = prev_ind_picked_flag
            picked_indices[curr_index] = element_picked_flag
            prev_choices = self._prev_choice[curr_index]
            prev_ind_picked_flag = prev_choices[element_picked_flag]
            # print(f"adding element {self._a[curr_index]} to picked_indices: ", element_picked_flag) if self._show else None
            curr_index -= 1
            
        
        # populate self._ans
        for i in range(num_elements):
            if picked_indices[i] == 1:
                self._ans.append(i)

        # print vals for debugging:
        if self._show:
            for i in range(num_elements):
                print("i: ", self._a[i], "self._max_score[i]: ", self._max_score[i], "self._prev_choice[i]: ", self._prev_choice[i])
            print("self._ans: ", self._ans)
            print("self._maxv: ", self._maxv)


############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################  

############################################################
#  class  Solution
# Nothing can be changed in Solution
###########################################################    
class Solution():
    def rob(self, nums:'Python list') -> 'int':
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
