from typing import List

class ProfitResult:
    def __init__(self, profit, buy_day, sell_day) -> None:
        assert buy_day <= sell_day
        self.buy_day = buy_day
        self.sell_day = sell_day
        self.profit = profit
        pass

    def __repr__(self) -> str:
        return f"[profit:{self.profit}, buy on: {self.buy_day}, sell_on: {self.sell_day}]"
    
    def add_days_index(self, index):
        # updated buy & sell days by a set index
        self.buy_day += index
        self.sell_day += index
        return self

    def __eq__(self, other):
        return self.profit == other.profit
    
    def __ne__(self, other):
        return self.profit != other.profit
    
    def __lt__(self, other):
        return self.profit < other.profit
    
    def __gt__(self, other):
        return self.profit > other.profit

    def __le__(self, other):
        return self.profit <= other.profit
    
    def __ge__(self, other):
        return self.profit >= other.profit


class Solution:
    def __init__(self):
        pass
        ## YoU can have what ever you want here
        

    ##LEETCODE INTERFACE.  DO NOT CHANGE
    ## YOU CANNOT CHANGE ANYTHING
    def maxProfit(self, prices: List[int]) -> int:
        if False:
            [sellday, buyday, work] = self.nsquare_time_constant_space(prices)
        if False:
            [sellday, buyday, work] = self.nlogn_time_logn_space(prices)
        if True:
            [sellday, buyday, work] = self.ntime_constant_space(prices)
        p = self._compute_profit(prices, sellday, buyday)
        return p

    #############################################
    # All public function here. 
    #############################################
    class ProfitResult:
        def __init__(self, profit, buy_day, sell_day) -> None:
            assert buy_day <= sell_day
            self.buy_day = buy_day
            self.sell_day = sell_day
            self.profit = profit
            pass

        def __repr__(self) -> str:
            return f"[profit:{self.profit}, buy on: {self.buy_day}, sell_on: {self.sell_day}]"
        
        def add_days_index(self, index):
            # updated buy & sell days by a set index
            self.buy_day += index
            self.sell_day += index
            return self

        def __eq__(self, other):
            return self.profit == other.profit
        
        def __ne__(self, other):
            return self.profit != other.profit
        
        def __lt__(self, other):
            return self.profit < other.profit
        
        def __gt__(self, other):
            return self.profit > other.profit

        def __le__(self, other):
            return self.profit <= other.profit
        
        def __ge__(self, other):
            return self.profit >= other.profit



    ########################################
    # TIME:THETA(N^2)
    # Space:THETA(1)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def nsquare_time_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._nsquare_time_constant_space(a) 


    ########################################
    # TIME:THETA(NlogN)
    # Space:THETA(logn)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def nlogn_time_logn_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._nlogn_time_logn_space(a)

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def ntime_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._ntime_constant_space(a)
        

    #############################################
    # All private function here. 
    # WRIYE CODE BELOW
    # You can have any number of private functions and variables
    # NOTHING CAN BE CHABGED BELOW
    #############################################
    def _compute_profit(self, a: List[int], s: "int", b: "int") -> "int":
        n = len(a)
        if n == 0:
            return 0
        assert s >= 0 and s < n
        assert b >= 0 and b < n
        assert s >= b
        p = a[s] - a[b]
        return p

    def _nsquare_time_constant_space(self, a):
        work = 0
        max_profit = 0
        max_profit_buy_day, max_profit_sell_day = 0, 0
        num_days = len(a)
        for i in range(num_days):
            buy_price = a[i] 
            for j in range(i, num_days):
                sell_price = a[j]
                profit = (sell_price - buy_price)
                work += 1
                if profit>max_profit:
                    max_profit = profit
                    max_profit_buy_day, max_profit_sell_day = i, j
        return max_profit_sell_day, max_profit_buy_day, work

    def base_case_lists(self, prices):
        # profit is ord_pair of profit_val, buy_day, sell_day for that profit
        profit = [0,0,0]
        
        if len(prices) <= 1:
            best_buy_day, best_sell_day = 0, 0

        elif len(prices) == 2:
            if (prices[1] <= prices[0]):
                # if right is lower than left
                # within the set it's best to buy on second day globally
                # and best to sell on first day globally
                best_buy_day, best_sell_day = 1, 0
            else:
                profit_val = prices[1]-prices[0]
                # profit = ProfitResult(profit_val, 0, 1)
                profit = [profit_val, 0, 1]
                best_buy_day, best_sell_day = 0, 1
        return profit, best_buy_day, best_sell_day
    
    def move_buy_sell_day_by_index(self, profit_list, move_by_val):
        profit_list[1] += move_by_val
        profit_list[2] += move_by_val
        return profit_list


    def compare_three_profits(self, profit1, profit2, profit3):
        if (profit1[0]>=profit2[0]) and (profit1[0]>=profit3[0]):
            return profit1
        elif (profit2[0]>=profit1[0]) and (profit2[0]>=profit3[0]):
            return profit2
        elif (profit3[0]>=profit1[0]) and (profit3[0]>=profit1[0]):
            return profit3

    def div_conq_calculate_max_profit_buy_day_sell_day(self, prices, work):
        work += 1
        total_days = len(prices)
        if total_days<=2:
            profit, best_buy_day, best_sell_day = self.base_case_lists(prices)
        else:
            #divide into two parts
            ind_break = total_days//2
            first_half = prices[:ind_break]
            second_half = prices[ind_break:]
            left_profit, left_bb_day, left_bs_day, work = self.div_conq_calculate_max_profit_buy_day_sell_day(
                first_half, work
            )
            right_profit, right_bb_day, right_bs_day, work = self.div_conq_calculate_max_profit_buy_day_sell_day(
                second_half, work
            )
            right_profit = self.move_buy_sell_day_by_index(right_profit, ind_break)
            right_bb_day, right_bs_day = right_bb_day+ind_break, right_bs_day+ind_break

            right_buy_price, right_sell_price = prices[right_bb_day], prices[right_bs_day]
            left_buy_price, left_sell_price = prices[left_bb_day], prices[left_bs_day]

            # check if it's more profitable to buy in first_half and sell in second_half
            possible_profit = right_sell_price -  left_buy_price
            # possible_profit_result = ProfitResult(possible_profit, buy_day=left_bb_day, sell_day=right_bs_day)
            possible_profit_list = [possible_profit, left_bb_day, right_bs_day]
            # profit = max(left_profit, right_profit, possible_profit_result)
            profit = self.compare_three_profits(left_profit, right_profit, possible_profit_list)

            best_buy_day = right_bb_day if right_buy_price<=left_buy_price else left_bb_day
            best_sell_day = left_bs_day if left_sell_price>=right_sell_price else right_bs_day
        return profit, best_buy_day, best_sell_day, work


    def _nlogn_time_logn_space(self, a):
        work = 0
        profit, _, _, work = self.div_conq_calculate_max_profit_buy_day_sell_day(a, work)
        # return profit.sell_day, profit.buy_day, work
        return profit[2], profit[1], work

    def _ntime_constant_space(self, a):
        work = 0
        l_ind, r_ind = 0, 0
        profit = [0, 0, 0]
        # profit = 0
        total_days = len(a)

        while (r_ind<total_days):
            work += 1
            l_price, r_price = a[l_ind], a[r_ind]
            profit_val = r_price - l_price
            new_profit = [profit_val, l_ind, r_ind]
            # profit = max(profit, new_profit)
            if new_profit[0]>=profit[0]:
                profit = new_profit
            
            if l_price<=r_price:
                r_ind += 1
            else:
                l_ind = r_ind

        return profit[2], profit[1], work
        # return profit.sell_day, profit.buy_day, work

