############################################################
# Prime.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################

############################################################
#           NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from Solution import *
from time import process_time 

class Prime():
    def __init__(self):
        self._testBench()

    def _nsquare(self, n:'int',prime_number_list:'list')->'int':
        s = Solution(n,prime_number_list)
        ans = s.nsquare()    # Function to implement
        return ans

    def _up_to_prime(self, n:'int',prime_number_list:'list')->'int':
        s = Solution(n,prime_number_list)
        ans = s.up_to_prime()    # Function to implement
        return ans

    def _sieve_of_eratosthenes(self, n:'int',prime_number_list:'list')->'int':
        s = Solution(n,prime_number_list)
        ans = s.sieve_of_eratosthenes()    # Function to implement
        return ans
    
    def _testBench(self):
        self._tests()
        print("ALL TESTS PASSED")

    def _print(self,s:'String',n:'int',ans:'int',steps:'int',num_prime:'int', d:'float'):
        print("---------------",s, " Method-----------------------")    
        assert(num_prime == ans)
        print(n, " has ", num_prime, " Prime. Took", steps, " steps to compute")
        print("Total CPU time in sec =",d)
        

    def _test1(self,n:'int',ans:'int'):
        max = 1000000
        if (n < max):
            print("-------------", n , "-------------------------")
            t1_start = process_time()
            n_prime_number_list = []
            workn = self._nsquare(n,n_prime_number_list)
            t1_stop = process_time() 
            d = t1_stop - t1_start; 
            self._print("n*SquareRoot(n)",n,ans,workn,len(n_prime_number_list),d)
        else:
            print("-------------", n , " cannot compute using n^2 method -------------")

        t1_start = process_time()
        up_to_prime_list = []
        works = self._up_to_prime(n,up_to_prime_list)
        t1_stop = process_time() 
        d = t1_stop - t1_start; 
        self._print("uptoprime",n,ans,works,len(up_to_prime_list),d)
        if (n < max):
            if (n_prime_number_list != up_to_prime_list):
                print("Prime numbers are different between two algorithms")
                assert(False)

        t1_start = process_time()
        sieve_prime_number_list = []
        works = self._sieve_of_eratosthenes(n,sieve_prime_number_list)
        t1_stop = process_time() 
        d = t1_stop - t1_start; 
        self._print("n*log(n)",n,ans,works,len(sieve_prime_number_list),d)
        if (n < max):
            if (n_prime_number_list != sieve_prime_number_list):
                print("Prime numbers are different between two algorithms")
                assert(False)


    def _tests(self):
        n = [100,1000,10000,100000,1000000,10000000,100000000]
        a = [25,168,1229,9592,78498,664579,5761455]
        j = 0
        for i in n:
            self._test1(i,a[j])
            j = j + 1


############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
    print("Testing Prime.py Starts")
    s = Prime()
    print("Testing Prime.py ENDS")
    
############################################################

###########################################################
if (__name__    == '__main__'):
    main()