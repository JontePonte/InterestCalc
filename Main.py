
from InputValues import *


class InterestCalc:
    """ Main class for the interest calculator """
    def __init__(self):
        # Input variables from in "InputValues"
        self.yearly_interest = YEARLY_INTEREST
        self.monthly_deposit = MONTHLY_DEP
        self.start_money = START_MONEY
        self.time_years = TIME_YEARS

        # Variables & values
        self.monthly_interest = (self.yearly_interest / 100) / 12
        self.time_month = self.time_years * 12
        self.current_month = 0
        self.savings = self.start_money

        # Do all the calculations
        self.calculate_interest()

        # Print the results in a nice way
        self.print_result()

    def calculate_interest(self):
        """ Do all the calculations to get total savings after X years """
        for month in range(self.time_month):
            # Deposit money in account
            self.savings += self.monthly_deposit
            # Add interest
            self.savings = (1 + self.monthly_interest) * self.savings

    def print_result(self):
        """ Print the result from the calculation """
        savings_print = round(self.savings, 2)

        print(" ")
        print("Monthly deposition:  ", self.monthly_deposit, "sek")
        print("Yearly interest:     ", self.yearly_interest, "%")
        print("Savings from start:  ", self.start_money, "sek")
        print(" ")
        print("After", self.time_years, "years you have", savings_print, "sek in your account")
        print(" ")


run = InterestCalc()
