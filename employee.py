"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        pass


class SalaryContractEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary
    
    def __str__(self):
        return "{} works on a monthly salary of {}. Their total pay is {}.".format(self.name, self.salary, self.get_pay())
    

class SalaryContractBonusComissionEmployee(SalaryContractEmployee):
    def __init__(self, name, salary, bonus_comission):
        super().__init__(name, salary)
        self.bonus_comission = bonus_comission

    def get_pay(self):
        return self.salary + self.bonus_comission
    
    def __str__(self):
        return "{} works on a monthly salary of {} and receives a bonus commission of {}. Their total pay is {}.".format(self.name, self.salary, self.bonus_comission, self.get_pay())


class SalaryContractContractComissionEmployee(SalaryContractEmployee):
    def __init__(self, name, salary, contract_comission, contracts_sold):
        super().__init__(name, salary)
        self.contract_comission = contract_comission
        self.contracts_sold = contracts_sold

    def get_pay(self):
        return self.salary + self.contract_comission * self.contracts_sold
    
    def __str__(self):
        return "{} works on a monthly salary of {} and receives a commission for {} contract(s) at {}/contract. Their total pay is {}.".format(self.name, self.salary, self.contracts_sold, self.contract_comission, self.get_pay())


class HourlyContractEmployee(Employee):
    def __init__(self, name, wage, hours_worked):
        super().__init__(name)
        self.wage = wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.wage * self.hours_worked

    def __str__(self):
        return "{} works on a contract of {} hours at {}/hour. Their total pay is {}.".format(self.name, self.hours_worked, self.wage, self.get_pay())


class HourlyContractBonusComissionEmployee(HourlyContractEmployee):
    def __init__(self, name, wage, hours_worked, bonus_comission):
        super().__init__(name, wage, hours_worked)
        self.bonus_comission = bonus_comission

    def get_pay(self):
        return self.wage * self.hours_worked + self.bonus_comission
    
    def __str__(self):
        return "{} works on a contract of {} hours at {}/hour and receives a bonus commission of {}. Their total pay is {}.".format(self.name, self.hours_worked, self.wage, self.bonus_comission, self.get_pay())
    

class HourlyContractContractComissionEmployee(HourlyContractEmployee):
    def __init__(self, name, wage, hours_worked, contract_comission, contracts_sold):
        super().__init__(name, wage, hours_worked)
        self.contract_comission = contract_comission
        self.contracts_sold = contracts_sold

    def get_pay(self):
        return self.wage * self.hours_worked + self.contract_comission * self.contracts_sold
    
    def __str__(self):
        return "{} works on a contract of {} hours at {}/hour and receives a commission for {} contract(s) at {}/contract. Their total pay is {}.".format(self.name, self.hours_worked, self.wage, self.contracts_sold, self.contract_comission, self.get_pay())


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryContractEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractContractComissionEmployee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractContractComissionEmployee('Jan', 150, 25, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryContractBonusComissionEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContractBonusComissionEmployee('Ariel', 120, 30, 600)

print(billie)
print(charlie)
print(renee)
print(jan)
print(robbie)
print(ariel)