############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################
import logging
logger = logging.getLogger(__name__)

class Solution:
    def __init__(self, n: "int", prime_number_list: "list"):
        self._n = n
        self._prime_number_list = (
            prime_number_list  # You need to append this using _append_prime_number
        )
        self._work_done = 0  # You need to increment using _increment_work_done()
        ##YOU CANNOT have anything here

    ############################################################
    # All work done goes through this routine.
    # Nothing can be changed
    ###########################################################
    def _increment_work_done(self):
        self._work_done = self._work_done + 1

    ############################################################
    # All prime numbers are appended to the list.
    # Nothing can be changed
    ###########################################################
    def _append_prime_number(self, p):
        self._prime_number_list.append(p)

    ##Required function to implement
    def nsquare(self) -> "int":
        ## NOTHING CAN BE CHANGED HERE
        ## YOU CANNOT CALL math.log from Python library
        self._nsquare()
        return self._work_done

    ##Required function to implement
    def up_to_prime(self) -> "int":
        ## NOTHING CAN BE CHANGED HERE
        ## you cannot call log from Python library
        self._up_to_primes()
        return self._work_done

    ##Required function to implement
    def sieve_of_eratosthenes(self) -> "int":
        ## NOTHING CAN BE CHANGED HERE
        ## YOU CANNOT CALL math.log from Python library
        self._sieve_of_eratosthenes()
        return self._work_done

    ############################################################
    # Implement your code BELOW
    # You can have any number of private variables and functions
    # YOU CANNOT CALL math.log from Python library
    ###########################################################

    def _is_prime(self, val):
        # this is o(sqrt(n)) complexity as it only 
        # verifies numbers upto sqrt(n)
        if val%2==0:
            return False
        
        i = 3 # check only for odd num_divisiblity
        
        while i*i <= val:
            self._increment_work_done()
            if val%i==0:
                return False
            i += 2
        return True


    def is_prime_check_only_primes(self, val):
        # this is of complexity sqrt(n)/logn as we only check 
        # for prime numbers that are under sqrt(n)
        # given the number of prime nums is of order 
        primes = self._prime_number_list
        
        if val%2==0:
            return False
        
        if val==3:
            return True
        
        i = 1 #start with prime_num: 3 at index 1
        while (primes[i]*primes[i])<=val:
            self._increment_work_done()
            if val % primes[i]==0:
                return False
            i += 1
        return True


    def _nsquare(self):
        num = self._n
        if num<2:
            return 

        self._append_prime_number(2)
        for check_prime_num in range(3, num, 2):
            self._increment_work_done()
            
            if self._is_prime(check_prime_num):
                self._append_prime_number(check_prime_num)
        return None

    
    def _up_to_primes(self) -> "int":
        num = self._n
        if num<2:
            return 
        self._append_prime_number(2)

        for check_prime_num in range(3, num, 2):
            self._increment_work_done()
            
            if self.is_prime_check_only_primes(check_prime_num):
                # logger.info(f"{check_prime_num} is a prime num")
                self._append_prime_number(check_prime_num)

    
    def _sieve_of_eratosthenes(self) -> "int":
        num = self._n
        
        is_prime = [True for i in range(num)]
        is_prime[0] = False
        is_prime[1] = False
        
        i = 2
        while i < num:
            #is_prime index would be set to i
            #if it was not divisible by any number less than i
            if is_prime[i]==True:
                self._append_prime_number(i)
                self._increment_work_done()
                
                multiplier = i
                # multiply by every number higher than itself below would've been complete
                # eg: 11*(2 to 10) would've been marked as False already
                # only needs 11 * 11 as the first 
                while (i*multiplier) < num:
                    is_prime[i*multiplier] = False
                    multiplier += 1
                    pass
            i += 1
        pass
