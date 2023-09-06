

import csv

customers = open('EmployeePay.csv','r')

csv_file = csv.reader(customers)

next(csv_file)

for record in csv_file:
    Salary = int(record[3])
    Bonus = float(record[4]) * Salary
    Pay = Salary + Bonus
    print(f'First Name: {record[1]}')
    print(f'Last Name: {record[2]}')
    print(f'Salary: $ {Salary:10,.2f}')
    print(f'Bonus:  $ {Bonus:10,.2f}')
    print(f'Pay:    $ {Pay:10,.2f}')
    input()