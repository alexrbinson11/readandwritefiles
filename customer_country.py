def main():
    
    import csv

    customers = open('customers.csv','r')

    outfile = open('customer_country.csv','w')

    csv_file = csv.reader(customers)

    next(csv_file)

    outfile.write('Full Name, Country\n')

    for record in csv_file:
        outfile.write(f'{record[1]} {record[2]}, {record[4]}\n')
        
    outfile.close()

main()