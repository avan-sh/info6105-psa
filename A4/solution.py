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

    def add_last(self, val):
        # adds a new element towards the end of SList
        new_node = ListNode(val=val, next=None)
        if self._first is None:
            # if no elements in list:
            # set new node as first, last & set len =1
            self._first = new_node
            self._last = self._first
            self._len += 1
        else:
            # if some element already exists,
            # set last.next to new node and set new node as last
            self._last.next = new_node
            self._last = new_node
            self._len += 1

    def add_first(self, val):
        # adds a new element towards the first of SList
        new_node = ListNode(val=val, next=None)
        if self._len == 0:
            # if no elements in list:
            # set new node as first, last & set len =1
            self._first = new_node
            self._last = self._first
            self._len += 1
        else:
            # if some element already exists,
            # set node.next to new node and set new node as first
            new_node.next = self._first
            self._first = new_node
            self._len += 1

    def remove_first(self) -> bool:
        # returns true if some len is there and can be removed
        # returns false if no eleement in Slist
        if self._len == 0:
            return False
        new_first = self._first.next
        self._first = new_first
        if new_first is None:
            self._last = None
        self._len += -1
        return True

    def remove_last(self) -> bool:
        # returns true is last element can be deleted
        # else false
        if self._len == 0:
            return False
        if self._len == 1:
            self._first, self._last = None, None
            return
        current = self._first.next
        prev = self._first
        while current.next is not None:
            prev = current
            current = current.next
        self._last = prev
        self._len += -1
        return True

    def __len__(self):
        return self._len

    def len(self):
        return self._len

    def first_value(self):
        if self._first is None:
            return None
        else:
            return self._first.val

    def last_value(self):
        if self._last is None:
            return None
        else:
            return self._last.val


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
        self._s.add_first(x)

    def pop(self) -> int:
        first_val = self._s.first_value()
        if first_val is not None:
            self._s.remove_first()
        return first_val

    def top(self) -> int:
        return self._s.first_value()

    def empty(self) -> bool:
        return len(self._s) == 0


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
        if self._s._last == None:
            self._s._first = node
            self._s._last = node
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
        return self._s._len == 0


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

    def enQueue(self, value: int) -> bool:
        pass

    def deQueue(self) -> bool:
        pass

    def Front(self) -> int:
        pass

    def Rear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass


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

    def insertFront(self, value: int) -> bool:
        pass

    def insertLast(self, value: int) -> bool:
        pass

    def deleteFront(self) -> bool:
        pass

    def deleteLast(self) -> bool:
        pass

    def getFront(self) -> int:
        pass

    def getRear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass
