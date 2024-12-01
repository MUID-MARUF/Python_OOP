class Loan:
    interest = 0
    def __init__(self,loan_id, name, amount, years):
        self.loan_id = loan_id
        self.name = name
        self.amount = amount
        self.years = years
        self.balance = amount
        self.interest_rate = 0.5
    
    def calculate_int(self):
        interest = self.amount * self.interest_rate *self.years
        return interest
    
    def calculate_total(self):
        total = self.amount + self.interest
        return total
        
class AgricultureLoan(Loan):
    def __init__(self,loan_id, name, amount, years):
        super().__init__( loan_id, name, amount, years)
        
        self.subsidy_rate = 0.01
        
    def calculate_int(self):
        if self.years > 2:
            self.interest_rate = 0.04
            
        return self.amount * self.interest_rate *self.years
    
    def calculate_total(self):
        total = self.amount + self.interest + (self.subsidy_rate*self.years)
        return total
    
class SmallBusiness(Loan):
    def __init__(self, name, amount, years):
        super().__init__( name, amount, years)
        self.interest_rate = 0.06
        
    def calculate_int(self):
        return self.amount * self.interest_rate *self.years
    
    def calculate_total(self):
        total = self.amount + self.interest
        return total
    
class ManagementSystem:
    def __init__(self):
        self.loans = []
        
    def add_loan(self, loan):
        self.loans.append(loan)

    def calculate_total_interest(self):
        total_interest = sum(loan.calculate_interest() for loan in self.loans)
        return total_interest

    def display_loans(self):
        for loan in self.loans:
            print(loan)


while(True):
    print("Fillup the form bellow to get a loan :: ")
    print("----------------------------------------")
    print(" ")

    acc_id = int(input("Enter your bank id : "))
    n = input("Enter your name : ")
    amo = int(input("Enter the amount : "))
    years_inp = input("Enter for how long you want the loan : ")

    print("What type of loan you want?")
    print("1. Agriculture")
    print("2. Small Business")
    type_of_loan = int(input("Press 1 or 2 option :: "))
    
    if type_of_loan == 1:
        obj = AgricultureLoan(acc_id, n, amo, years_inp)
    elif type_of_loan == 2:
        obj = SmallBusiness(acc_id, n, amo, years_inp)
    else:
        print("No valid input. ")
        
    checker = input("Do you want to make moore loans ? Y/N ")
    if checker == "N":
        break
    
