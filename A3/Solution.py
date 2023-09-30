############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################


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
