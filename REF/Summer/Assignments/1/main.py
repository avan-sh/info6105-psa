

import Int as IntFile

Int = IntFile.Int
############################################################
# Inttest.py 
# Test Bench for Int
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################

############################################################
#  NOTHING CAN BE CHANGED IN THIS FILE
########################################################### 

############################################################
#  All imports here
###########################################################
import sys
from typing import List # For getting Python Version
#from Int import *

############################################################
#  class  Int test
###########################################################    

class Inttest():
    def __init__(self):
        pass


        
    def data_structure(self):
        print("------------Testing data_structure-----------------")
        a = Int()
        print(a)
        a = Int(100)
        print(a)
        a = Int(-100)
        print(a)
        n = -10098765456786542342222
        a = Int(n)
        print(a)
        ans = [1,0,0,9,8,7,6,5,4,5,6,7,8,6,5,4,2,3,4,2,2,2,2]  
        d = len(a)
        d1 = len(ans) 
        if (d != d1):
            print("Number of digits is ", d1," Your answer is", d)
        assert(d == d1)
        print("--------------- data_structure Passed --------------- ")

    def access(self):
        print("------------Testing access -----------------")
        n = -10098765456786542342222
        a = Int(n)
        print(a)
        ans = [1,0,0,9,8,7,6,5,4,5,6,7,8,6,5,4,2,3,4,2,2,2,2]  
        d = len(a)
        d1 = len(ans) 
        if (d != d1):
            print("Number of digits is ", d1," Your answer is", d)
        assert(d == d1)
        for i in range(d):
            e = a[i]
            e1 = ans[i]
            if (e != e1):
                print("a[",i,"] = ",e1, "But your answer is",e)
            assert(e == e1)
        a[0] = 5 ;
        print(a)
        n = a.int()
        n1 = -50098765456786542342222
        if (n != n1):
            print("Correct ans=",n1,"But your answer is",n)
        assert(n == n1)
        print("--------------- access Passed --------------- ")

    def arithmetic(self):
        print("------------Testing arithmetic-----------------")
        q = [0, 5, -91, 1086, 1235657786899879757575175157511571, -12356577868998797575789107815]
        s = len(q)
        print("---------------  Testing +  --------------- ")
        for i in range(s):
            m = q[i]
            a = Int(m)
            print("a = ",end="")
            print(a)
            n = q[s-1-i]
            b = Int(n)
            print("b = ",end="")
            print(b)
       
            mn = m + n
            c = a + b 
            print("c = ",end="")
            print(c)
            vc = c.int()
            if (vc != mn):
                print("Expected value is: ", mn, "But your answer is", vc) ;
                assert(0)

        print("--------------- + Passed --------------- ")

        print("---------------  Testing -  --------------- ")
        for i in range(s):
            m = q[i]
            a = Int(m)
            print("a = ",end="")
            print(a)
            n = q[s-1-i]
            b = Int(n)
            print("b = ",end="")
            print(b)
       
            mn = m - n
            c = a - b 
            print("c = ",end="")
            print(c)
            vc = c.int()
            if (vc != mn):
                print("Expected value is: ", mn, "But your answer is", vc) 
                assert(0)

        print("--------------- - Passed --------------- ")

       
        print("--------------- arithmetic Passed --------------- ")

    def relational(self):
        print("-------------Testing arithmetic-----------------")
        q1 = [0, 3, 2, -3, -2, 5, 5, -5,-5, -91, 1086, 1235657786899879757575175157511571, -12356577868998797575789107815,-12356577868998797575789107815]
        q2 = [-1,2, 3,  2,  3, 5, -5, 5, -5, 91, 1085, 1235657786899879757575175157511570, -12356577868998797575789207815,-12356577868998797575789107815]
        s = len(q1)
        print("---------------  Testing <  --------------- ")
        for i in range(s):
            m = q1[i]
            a = Int(m)
            print("a = ",end="")
            print(a)
            n = q2[i]
            b = Int(n)
            print("b = ",end="")
            print(b)    
            mn = m < n
            c = (a < b) 
            assert(c == 0 or c == 1)
            print("is a < b",c)     
            if (c != mn):
                print("Expected value is: ", mn, "But your answer is", c) 
                assert(0)
        print("--------------- < Passed --------------- ")

        print("---------------  Testing >  --------------- ")
        for i in range(s):
            m = q1[i]
            a = Int(m)
            print("a = ",end="")
            print(a)
            n = q2[i]
            b = Int(n)
            print("b = ",end="")
            print(b)
            mn = (m > n)
            c = (a > b)
            assert(c == 0 or c == 1)
            print("is a > b",c)          
            if (c != mn):
                print("Expected value is: ", mn, "But your answer is", c) 
                assert(0)
        print("--------------- < Passed --------------- ")

        print("---------------  Testing ==  --------------- ")
        for i in range(s):
            m = q1[i]
            a = Int(m)
            print("a = ",end="")
            print(a)
            n = q2[i]
            b = Int(n)
            print("b = ",end="")
            print(b)
            mn = (m == n)
            c = (a == b)
            assert(c == 0 or c == 1)
            print("is a == b",c)          
            if (c != mn):
                print("Expected value is: ", mn, "But your answer is", c) 
                assert(0)
        print("--------------- == Passed --------------- ")

        print("---------------  Testing !=  --------------- ")
        for i in range(s):
            m = q1[i]
            a = Int(m)
            print("a = ",end="")
            print(a)
            n = q2[i]
            b = Int(n)
            print("b = ",end="")
            print(b)
            mn = (m != n)
            c = (a != b)
            assert(c == 0 or c == 1)
            print("is a != b",c)          
            if (c != mn):
                print("Expected value is: ", mn, "But your answer is", c) 
                assert(0)
        print("--------------- != Passed --------------- ")

############################################################
# MAIN
###########################################################    
def main():
    print("Basic Int test starts")
    print(sys.version)
    t = Inttest()
    t.data_structure()
    t.access() 
    t.arithmetic() 
    t.relational() 
    print("Basic Int test Ends")



############################################################
# start up
###########################################################
if (__name__  == '__main__'):
    main()