import csv

Row = ['James Smith', 'james@smith.com', 200000]

# Make sure 'customers.csv' is in your root directory, or provide path to open() method.
# pass in 'a' to append new row or 'w' to overwrite CSV file
with open('customers.csv', 'a', newline='') as csvfile:
    cust_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    cust_writer.writerow(Row)
