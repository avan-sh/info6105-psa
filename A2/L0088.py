############################################################
# L0088.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################
############################################################
# All imports
###########################################################
from typing import List
from time import process_time
import math
import logging

logger = logging.getLogger(__name__)


class Solution:
    #YOU CANNOT CHANGE THIS INTERFACE
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        work = [0]
        p = L0088(nums1,m,nums2,n,work,"ntime_1space")

class L0088:
    def __init__(self,nums1: List[int], m: int, nums2: List[int], n: int,work:'List of size 1',alg:'string') -> None:
        self._nums1 = nums1 
        self._m = m
        self._nums2 = nums2 
        self._n = n
        self._work = work ;
        
        # logger.info(f"m: {self._m} n: {self._n}")
        if (alg == "ntime_1space"):
            self._n_time_constant_space()
        elif (alg == "nlogntime_1space"):
            self._nlogn_time_constant_space()
        elif (alg == "ntime_nspace"):
            self._n_time_n_space()
        
        else:
            assert(False)


    ########################################
    # TIME:THETA(Nlogn)
    # Space:THETA(1)
    #########################################
    def _nlogn_time_constant_space(self):
        for i in range(self._n):
            self._nums1[self._m+i] = self._nums2[i]

        self._nums1.sort()
        total  = self._m + self._n
        self._work[0] = math.ceil(total * math.log(total, 2))
        
        
        
        
        
    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self):
        print("Write Code")
        # for i in range(self._n):
        #     self._nums1[i+self._m] = self._nums2[i]

        # a = sorted(self._nums1)
        # for i in range(self._m + self._n):
        #     self._nums1[i] = a[i]
        # return
        if self._n==0:
            return 

        if self._m==0:
            for i in range(self._n):
                val = self.get_from_arr(arr=self._nums2, index=i)
                self.set_val_arr(value=val, index=i)
            return 
        
        sorted_arr = [0] * (self._m + self._n)
        arr1_ptr, arr2_ptr = 0, 0
        arr1_val = self.get_from_arr(self._nums1, arr1_ptr)
        arr2_val = self.get_from_arr(self._nums2, arr2_ptr)
        
        while (arr1_ptr<self._m) and (arr2_ptr<self._n):
            arr1_val = self.get_from_arr(self._nums1, arr1_ptr)
            arr2_val = self.get_from_arr(self._nums2, arr2_ptr)
            new_index = arr1_ptr + arr2_ptr
            
            # logger.debug(f"{new_index} = arr1 + arr2 {arr1_ptr} + {arr2_ptr}")
            # logger.debug(f"comparing = arr1 val {arr1_val} at index {arr1_ptr} to arr2 val {arr2_val} at index {arr2_ptr}")
            if arr1_val<arr2_val:
                
                self.set_val_arr(arr=sorted_arr, value=arr1_val, index=new_index)
                arr1_ptr += 1
                # logger.debug(f"updated arr1_ptr to {arr1_ptr}")
            
            else:
                self.set_val_arr(arr=sorted_arr, value=arr2_val, index=new_index)
                arr2_ptr += 1
                # logger.debug(f"updated arr2_ptr to {arr2_ptr}")
            
            # logger.debug(f"pointers {arr1_ptr}, {arr2_ptr}")
    
        # logger.debug(sorted_arr)
        if (arr1_ptr>=self._m): # case when arr1 reached end but elements from arr2 are pending
            # logger.debug("updating remaingin values from arr2")
            
            while (arr2_ptr<self._n):
                new_index = arr1_ptr + arr2_ptr
                arr2_val = self.get_from_arr(arr=self._nums2, index=arr2_ptr)
                self.set_val_arr(arr=sorted_arr, value=arr2_val, index=new_index)
                arr2_ptr += 1
                logger.debug(sorted_arr)
        
        elif (arr2_ptr>=self._n): # case when arr2 reached end but elements from arr1 are pending
            # logger.debug("updating remaingin values from arr1")
            while (arr1_ptr<self._m):
                new_index = arr1_ptr + arr2_ptr
                arr1_val = self.get_from_arr(arr=self._nums1, index=arr1_ptr)
                self.set_val_arr(arr=sorted_arr, value=arr1_val, index=new_index)
                arr1_ptr += 1
                
        for i in range(self._n + self._m):
            val = self.get_from_arr(arr=sorted_arr, index=i)

            self.set_val_arr(arr=self._nums1, value=val, index = i)
        
        # print(self._nums1, self._nums2)
            
            
    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_constant_space(self):
        if self._n==0:
            return 

        if self._m==0:
            for i in range(self._n):
                val = self.get_from_arr(arr=self._nums2, index=i)
                self.set_val_arr(arr=self._nums1, value=val, index=i)
            return 
        
        arr1_ptr, arr2_ptr = self._m-1, self._n-1
        arr1_val = self.get_from_arr(self._nums1, arr1_ptr)
        arr2_val = self.get_from_arr(self._nums2, arr2_ptr)
        new_index = arr1_ptr + arr2_ptr
        
        while arr1_ptr>=0 or arr2_ptr>=0:
            
            arr1_val = self.get_from_arr(self._nums1, arr1_ptr)
            arr2_val = self.get_from_arr(self._nums2, arr2_ptr)
            new_index = arr1_ptr + arr2_ptr+1
            # logger.info(f"comparing arr1_val{arr1_val} ind{arr1_ptr} & arr2_val {arr2_val} ind {arr2_ptr}")

            if arr1_ptr==-1:
                self.set_val_arr(arr=self._nums1, value=arr2_val, index=new_index)
                arr2_ptr -= 1
            
            elif arr2_ptr == -1:
                self.set_val_arr(arr=self._nums1, value=arr1_val, index=new_index)
                arr1_ptr -= 1
            
            elif arr1_val>arr2_val:
                # logger.info(f"new value {arr1_val} added to index {new_index}")
                self.set_val_arr(arr=self._nums1, value=arr1_val, index=new_index)
                arr1_ptr -= 1

            elif arr2_val>=arr1_val:
                # logger.info(f"new value {arr2_val} added to index {new_index}")
                self.set_val_arr(arr=self._nums1, value=arr2_val, index=new_index)
                arr2_ptr -= 1

            pass
        
        # logger.info(f"Arr after loop: {self._nums1}")
        

    
    def get_from_arr(self, arr, index):
        self._work[0] += 1
        return arr[index]

    def set_val_arr(self, arr, value, index):
        # logger.debug(f"Setting arr value to {value} in index{index}")
        self._work[0] += 1
        arr[index] = value
        pass

    def set_val_arr1(self, value, index):
        self._work[0] += 1
        self._nums1[index] = value
        pass
    