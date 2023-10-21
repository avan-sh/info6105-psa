############################################################
# L0322.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################
from typing import List
from time import process_time 


class Solution:
    ## YOU CANNOT CHANGE THIS INTERFACE
    ## LEETCODE INTERFACE
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## YOU CANNOT CHANGE ANYTHING IN THIS PROCEDURE
        work = [0]
        changes = [] #If change cannot be given, you must put -1 in changes[0]
        show = False
        p = L0322(coins,amount,changes,work,show)
        num_change = len(changes)
        if (num_change == 1):
            if (changes[0] == -1):
                num_change = -1
        return num_change

class L0322:
    def __init__(self, coins: List[int], amount:'int', changes:'list of int', work:'List of size 1',show:'boolean'):
        #NOTHING CAN BE CHANGED
        self._d = coins
        self._n = amount
        self._ans = changes
        self._work = work
        self._show = show
        # YOU MUST GENERATE V table and k table
        self._v = [] 
        self._k = []
        # You can have any number of data structures here
        # MUST WRITE TWO ROUTINES
        self._alg()
        self._get_solution() 

    def _increment_work(self):
        self._work[0] = self._work[0] + 1


    ############################################################
    # WRITE CODE BELOW
    ###########################################################

    ############################################################
    # TIME (n * k ) = O(n)
    # SPACE O(n)
    ############################################################
    def _alg(self):
        print("WRITE CODE")
        # self._v  # Array of least number of coins for val
        # self._k  #Val of highest val'd coin to start giving
        # Array _v, _k gives the best values & highest coin
        # This is the memoized output updated as calculated
        self._v, self._k = [None] * (self._n+1), [None] * (self._n+1)
        self._v[0], self._k[0] = 0, 0
        total_amount = self._n
        for i in range(1,total_amount+1):
            # print(i)
            vals = []
            for coin_val in self._d:
                pending_val = i - coin_val
                self._increment_work()
                if pending_val<0:
                    continue #skip if pending_val is -ve
                # print(f"pending_val: {pending_val}, coin_val: {coin_val}")
                least_coin_pending_val = self._v[pending_val]
                if least_coin_pending_val==-1:
                    continue #skip if pending_val can't be achieved
                total_coin = least_coin_pending_val + 1
                vals.append((total_coin, coin_val))
            if len(vals)==0: 
                self._v[i] = -1
                self._k[i] = 0
                continue # if 
            else:
                # get the best valued ordered pair
                best_val = min(vals, key=lambda x: x[0])
                # print(f"least coins for {i}: {best_val[0]} starting with coin_val {best_val[1]}")
                self._v[i] = best_val[0] #total_coin
                self._k[i] = best_val[1] #coin_val
            
            # print(f"least_coins: {self._v}")
            # print(f"coin_val: {self._k}")


    ############################################################
    # NOTHING CAN BE CHANGED IN THIS ROUTINE BELOW
    ###########################################################
    def _get_solution(self):
        if (self._show):
            a = []
            for i in range(self._n + 1):
                a.append(i)
            print(a)
            print(self._v)
            print(self._k)
        if (self._n < 1000):
            for i in range(self._n + 1):
                if (self._show):
                    print("minimum change for",i,"cents can be achieved using",self._v[i],"coins.")
                self._get_solution1(i)
        else:
            self._get_solution1(self._n)
            
    ############################################################
    # TIME O(n)
    # SPACE THETA(1)
    # How will you give change for p cents
    # WRITE CODE BELOW
    ############################################################
    def _get_solution1(self,p:'int'):
        # print("WRITE CODE")
        remain, given = p, 0
        i = 1
        while remain!=0:
            start_coin = self._k[remain]
            if start_coin==0:
                #only add when getting printing for original value
                if p==self._n:self._ans.append(-1)
                break
            given += start_coin
            remain += -start_coin
            print(f"{i} : Give coin {start_coin} . So far you have given= {given} .Remaining to give {remain}")
            #only add when getting printing for original value
            if p==self._n:self._ans.append(start_coin)
            # 1 : Give coin 1 . So far you have given= 1 .Remaining to give 46
            # import time
            # time.sleep(0.1)
        
