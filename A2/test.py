############################################################
# L0088Test.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#           NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from typing import List
from Util import *
from time import process_time 
from L0088 import *
import logging

import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',)

logger = logging.getLogger(__name__)
class L0088Test():
    def __init__(self):
        self._show = True 
        self._k = 0 ;
        self._u = Util()
        self._testBench()

    #Private  function
    def _testBench(self):
        self._tests()
        self._testn()
        print("ALL TESTS PASSED")

    #Private sunction
    def _test1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if (self._show):
            self._k = self._k + 1             
            print("-------------PROBLEM",self._k,"---------------")
            self._u.print_index(m+n)
            self._u.print_list(nums1)
            self._u.print_index(n)
            self._u.print_list(nums2)
        
        work1 = [0] ;
        nums11 = nums1.copy()
        t1_start = process_time() 
        b = L0088(nums11,m,nums2,n,work1,"nlogntime_1space")
        t1_stop = process_time() 
        d1 = t1_stop - t1_start
        self._u.assert_ascending(nums11)
        
        work2 = [0] ;
        nums12 = nums1.copy()
        t1_start = process_time() 
        b = L0088(nums12,m,nums2,n,work2,"ntime_nspace")
        t1_stop = process_time() 
        d2 = t1_stop - t1_start
        self._u.assert_ascending(nums12)
           
        work = [0] ;
        t1_start = process_time() 
        b = L0088(nums1,m,nums2,n,work,"ntime_1space")
        t1_stop = process_time() 
        d = t1_stop - t1_start 
        self._u.assert_ascending(nums1)

        if (self._show):
            print("------------- ANS ---------------")
            self._u.print_index(m+n)
            self._u.print_list(nums1)
        print("nlogntime_1space: work =", work1[0] , "CPU time in sec =",d1)
        print("ntime_nspace:     work =", work2[0] , "CPU time in sec =",d2)
        print("ntime_1space:     work =", work[0] , "CPU time in sec =",d)
        
        assert(nums11 == nums12)
        assert(nums11 == nums1)

    #Private sunction
    def _tests(self):
        self._show = True
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        self._test1(nums1,m,nums2,n)

        nums1 = [1,2,2,100,0,0,0]
        m = 4
        nums2 = [2,4,5]
        n = 3
        self._test1(nums1,m,nums2,n)

        nums1 = [2]
        m = 1
        nums2 = []
        n = 0
        self._test1(nums1,m,nums2,n)

        nums1 = [1,2]
        m = 2
        nums2 = []
        n = 0
        self._test1(nums1,m,nums2,n)

        nums1 = [1,2,0,0]
        m = 2
        nums2 = [1,2]
        n = 2
        self._test1(nums1,m,nums2,n)

        nums1 = [1,2,0,0]
        m = 2
        nums2 = [3,4]
        n = 2
        self._test1(nums1,m,nums2,n)

        nums1 = [3,4,0,0]
        m = 2
        nums2 = [1,2]
        n = 2
        self._test1(nums1,m,nums2,n)

        nums1 = [1,3,0,0]
        m = 2
        nums2 = [2,4]
        n = 2
        self._test1(nums1,m,nums2,n)

        nums1 = [2,4,0,0]
        m = 2
        nums2 = [1,2]
        n = 2
        self._test1(nums1,m,nums2,n)

        nums1 = [4,5,6,0,0,0]
        m = 3
        nums2 = [1,2,3]
        n = 3
        self._test1(nums1,m,nums2,n)


    #Private sunction
    def _testn(self):
        self._show = False
        N = 10
        M = N//100
        K = 10000
        for i in range(0,N):
            s = i + K
            print("Random tests on Array of size",s)
            nums1 = self._u.generate_random_number(s*2,False,1,N)
            nums1.sort()
            m = s
            nums2 = self._u.generate_random_number(s,False,1,N)
            n = s
            nums2.sort()
            self._test1(nums1,m,nums2,n)
        print("ALL ", N, "random tests passed")

 ############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
    print("Testing L0088Test Starts")
    s = L0088Test()
    print("Testing L0088Test ENDS")

############################################################
# Real main
###########################################################
if (__name__  == '__main__'):
    main()
  