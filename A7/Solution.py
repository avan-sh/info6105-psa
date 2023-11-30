############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2022
###########################################################

############################################################
# All imports
###########################################################
import heapq
from typing import List, Tuple
############################################################
# NOTHING CAN BE CHANGED in Solution
###########################################################
class Solution:
    def __init__(self,a:'list of runtime', num_races: 'list of size 1', r:'list of 3 best students', show:'bool'):
        self.N = 25 # Number of students
        self.S = 3 # First 3 winners
        self.T = 5 # Number of tracks

        self._a = a # List of run time (Given)
        self._num_races = num_races ; # MUST fill number of races conducted
        self._r = r #Find first 3 students (Must fill)
        self._show = show # Must print how you conducted races is _show is True
        ## All action happens in class Alg
        a = Alg(self,show)

    def fill_rank(self, student_number:'int', rank:'int'):
        assert(student_number >= 0 and student_number <= self.N)
        assert(rank >= 0 and rank <= self.S-1)
        self._r[rank] = student_number

    def update_num_races(self, n:'int'):
        self._num_races[0] = self._num_races[0] + n

    def get_student_runtime(self,student_number:'int')->'int':
        assert(student_number >= 0 and student_number <= self.N)
        return self._a[student_number]

############################################################
# You will write code in class Alg
# YOU CAN HAVE ANY NUMBER OF CLASSES 
###########################################################
class RaceOfFive: # Represents a heap object that conducts a race of 5 or less
    def __init__(self, vals: List[Tuple], prev_race_num: int, show=False) -> None:
        assert len(vals) <= 5
        self._h = []
        
        for value in vals:
            heapq.heappush(self._h, value)

        race_num = prev_race_num +1
        if show:
            print(f"For Race num:{race_num}")
            print(f"  Conduct Race between students: {[v[1] for v in vals]}")
        pass

    def get_top(self):
        return self._h[0]
    
    def pop_top(self):
        return heapq.heappop(self._h)

class Alg:
    def __init__(self,s:'Solution',show:'bool'):
        self._s = s
        self._show = show
        ## YOU CAN HAVE ANY NUMBER OF PRIVATE VARIABLES
        self._race_count = 0
        
        ## All happens in _race
        self._race()
        

    ############################################################
    # WRITE YOUR CODE BELOW
    # YOU CAN HAVE ANY NUMBER OF CLASSES AND PRIVATE FUNCTION
    # if self._show = True MUST SHOW ALL RACES
    ###########################################################
    def _increment_race_numbers(self):
        self._race_count += 1
        self._s.update_num_races(1)
        pass


    def _race(self):
        base_races = [] 
        # store tuples of top_runtime, top_runtime_index,race
        race_num = 1

        for i in range(5):
            runtime_index = [(self._s.get_student_runtime(ind), ind) for ind in range(5*i, 5*(i+1))]
            race = RaceOfFive(runtime_index, prev_race_num=self._race_count, show=self._show)
            self._increment_race_numbers()
            top_runtime, top_runtime_index = race.get_top()
            base_races.append((top_runtime, top_runtime_index,  race))
        
        race_of_best_from_each = RaceOfFive(base_races, race_num, show=self._show)
        self._increment_race_numbers()
        

        _, global_top_ind, top_race = race_of_best_from_each.pop_top()
        if self._show:
            print(f"Winner for the whole group is winner of Race number 6 who is student num{global_top_ind}")
        
        # get second & third race as 
        _, _, second_top_race = race_of_best_from_each.pop_top()
        _, _, third_top_race = race_of_best_from_each.pop_top()

        final_race_vals = []
        top_race.pop_top()
        top_race_second = top_race.pop_top()
        final_race_vals.append(top_race_second)
        top_race_third = top_race.pop_top()
        final_race_vals.append(top_race_third)
        
        second_best_of_best = second_top_race.pop_top()
        final_race_vals.append(second_best_of_best)

        second_best_of_races_runnerup = second_top_race.pop_top()
        final_race_vals.append(second_best_of_races_runnerup)

        third_best_of_best = third_top_race.pop_top()
        final_race_vals.append(third_best_of_best)

        final_race = RaceOfFive(final_race_vals, race_num, show=self._show)
        self._increment_race_numbers()
        
        _, global_runnerup_ind = final_race.pop_top()
        _, global_third_ind = final_race.pop_top()

        self._s.fill_rank(global_top_ind, 0)
        self._s.fill_rank(global_runnerup_ind, 1)
        self._s.fill_rank(global_third_ind, 2)
        if self._show:
            print(f"RunnerUp for the whole group is winner of Race number 7 who is student num{global_runnerup_ind}")
            print(f"Third for the whole group is RunnerUp of Race number 7 who is student num{global_runnerup_ind}")




