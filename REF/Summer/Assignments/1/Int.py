class Int():
    def __init__(self,n:'int' = 0):  
        #ONLY DATA STRUCTURE ALLOWED
        self._positive = True if n>=0 else False
        self._val = n
        # self._digits = self._get_digits(n)
    
    
    # def _get_digits(n):
    #     digits_list = []
    #     while n>=0:
    #         digits_list.append(n%10)
    #         n = n//10
    #     digits_list.reversed()
    #     return digits_list
    
    
    def __str__(self):
        symbol = "+" if self._positive else "-"
        # [*a] # converts string to chars
        return f"{str(self._val)} {symbol}{[*str(abs(self._val))]}"
    

    def __len__(self):
        return len(str(abs(self._val)))
    

    def __getitem__(self, key):
        "function allows you to get a particular digit from the integer"
        return int(str(abs(self._val))[key])
    

    def __setitem__(self, key, value):
        int_digits = [*str(abs(self._val))]
        int_digits[key] = str(value)
        multiplier = 1 if self._positive else -1
        self._val = multiplier * int(''.join(int_digits))
        # convert to -1 if val is zero
        # return 

    def __add__(self, other):
        return Int(self._val + other._val)

    def __sub__(self, other):
        return Int(self._val - other._val)

    def __lt__(self, other):
        return self._val < other._val
    
    def __gt__(self, other):
        return self._val > other._val
    
    def __le__(self, other):
        return self._val <= other._val
    
    def __ge__(self, other):
        return self._val >= other._val
    
    def __eq__(self, other):
        return self._val == other._val
    
    def __ne__(self, other):
        return self._val != other._val
    
    def int(self):
        return self._val

