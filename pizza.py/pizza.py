from tabulate import tabulate
import csv
import sys

table =[]

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        csvFile = sys.argv[1]
        if csvFile.endswith(".csv"):
            with open(csvFile) as file:
                reader = csv.reader(file)
                for row in reader:
                    table.append(row)
                print(tabulate(table, tablefmt = "grid" , headers = "firstrow"))
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError :
        sys.exit("File does not exist")
