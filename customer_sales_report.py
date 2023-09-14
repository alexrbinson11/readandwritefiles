def main():

    import csv

    infile = open('sales.csv','r')

    outfile = open('salesreport.csv','w')

    csv_file = csv.reader(infile)

    next(csv_file)

    outfile.write('Customer ID,Total\n')

    custid = '250'
    total = 0

    for record in csv_file:
        if custid == record[0]:
            total += float(record[3])+float(record[4])+float(record[5])

        else:
            outfile.write(f'{custid},{total:.2f}\n')
            custid = record[0]
            total = float(record[3])+float(record[4])+float(record[5])

    outfile.write(f'{custid},{total:.2f}')

    outfile.close()

main()



