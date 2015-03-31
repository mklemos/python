# Lab 7 Problem 4
# Maximilian Lemos

class Employee():
        count = 0
        def __init__(self):
                Employee.count = Employee.count + 1
                
        def store_name(self, n):
                self.name = n
        def store_ID(self, i):
                self.ID = i
        def store_rate(self, r):
                self.rate = r
        def store_job(self, j):
                self.job = j

        def return_name(self):
                return self.name
        def return_ID(self):
                return self.ID
        def return_rate(self):
                return self.rate
        def return_job(self):
                return self.job
