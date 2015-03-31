# Lab 7 problem 4
# Maximilian Lemos

from Employee import *

person1 = Employee()
person2 = Employee()
person3 = Employee()
person4 = Employee()

person1.store_name("Bob Smith")
person1.return_name()
person1.store_ID("10012")
person1.return_ID()
person1.store_rate("19.54")
person1.return_rate()
person1.store_job("lab tech")
person1.return_job()

person2.store_name("Alice Moore")
person2.return_name()
person2.store_ID("22321")
person2.return_ID()
person2.store_rate("49.78")
person2.return_rate()
person2.store_job("manager")
person2.return_job()

person3.store_name("Sue Lyon")
person3.return_name()
person3.store_ID("12345")
person3.return_ID()
person3.store_rate("26.00")
person3.return_rate()
person3.store_job("nurse")
person3.return_job()

person4.store_name("Ralph Leon")
person4.return_name()
person4.store_ID("20024")
person4.return_ID()
person4.store_rate("10.75")
person4.return_rate()
person4.store_job("custodian")
person4.return_job()

person1_profile = [person1.return_name(), person1.return_ID(), person1.return_rate(), person1.return_job()]
person2_profile = [person2.return_name(), person2.return_ID(), person2.return_rate(), person2.return_job()]
person3_profile = [person3.return_name(), person3.return_ID(), person3.return_rate(), person3.return_job()]
person4_profile = [person4.return_name(), person4.return_ID(), person4.return_rate(), person4.return_job()]

all_profiles = [person1_profile, person2_profile, person3_profile, person4_profile]

##all_names = [person1_profile[0], person2_profile[0], person3_profile[0], person4_profile[0]]
##all_IDs = [person1_profile[1], person2_profile[1], person3_profile[1], person4_profile[1]]
##all_rates = [person1_profile[2], person2_profile[2], person3_profile[2], person4_profile[2]]
##all_jobs = [person1_profile[3], person2_profile[3], person3_profile[3], person4_profile[3]]

search = 'manager'
for sublist in all_profiles:
    if sublist[3] == search:
        print("Found the manager's profile!", sublist)
        hourly = eval(sublist[2])
        weekly_wage = hourly * 40
        print(sublist[0],"weekly wage: $",weekly_wage)
        break
print("There are",Employee.count," employees total.")
