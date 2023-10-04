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

    def append(self, val):
        # adds a new element towards the end of SList
        new_node = ListNode(val=val, next=None)
        if self._first is None:
            self._first = new_node
            self._last = self._first
            self._len += 1
        else:
            self._last.next = new_node
            self._last = new_node
            self._len += 1



############################################################
#  class  MyStack
# 225. Implement Stack using Queues

# https://leetcode.com/problems/implement-stack-using-queues
###########################################################
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    
    def push(self, x: int) -> None:
        node = ListNode(x)
        node.next = self._s._first
        self._s._first = node
        self._s._len += 1
        pass
        

    def pop(self) -> int:
        head = self._s._first
        if head:
            head_val = self._s._first.val
            self._s._first = self._s._first.next
            self._s._len += -1
            return head_val
        else:
            return None
        

    def top(self) -> int:
        return self._s._first.val
        

    def empty(self) -> bool:
        return self._s._len == 0

############################################################
#  class  MyQueue
# 232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
###########################################################
class MyQueue:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x: int) -> None:
        node = ListNode(x)
        if self._s._last==None:
            self._s._first=node
            self._s._last=node
            self._s._len += 1
        else:
            self._s._last.next = node
            self._s._last = node
            self._s._len += 1


    def pop(self) -> int:
        print(self._s._first)
        if self._s._first == None:
            return None
        first_val = self._s._first.val
        next_node = self._s._first.next
        self._s._first = next_node
        self._s._len += -1
        if self._s._len == 0:
            self._s._last = None
        return first_val


    def peek(self) -> int:
        print(self._s._first)
        if self._s._first == None:
            return None
        return self._s._first.val
        # return 1
        
    def empty(self) -> bool:
        return self._s._len==0


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
