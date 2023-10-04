############################################################
#  Write code in this file
# Post this file in Canvas
# Cut and paste the whole file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run this file 4 times in 225, 235,622 and 641
# All tests must pass for 100
###########################################################


class ListNode:
    # NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


############################################################
#  class  Slist
###########################################################
class Slist:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0

    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################


############################################################
#  class  MyStack
# 225. Implement Stack using Queues

# https://leetcode.com/problems/implement-stack-using-queues
###########################################################
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()


############################################################
#  class  MyQueue
# 232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
###########################################################
class MyQueue:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
###########################################################


class MyCircularQueue:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()


############################################################
#  MyCircularDeque
# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque

###########################################################
class MyCircularDeque:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()
