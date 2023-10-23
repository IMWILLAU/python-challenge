import os
import csv

pyBank = os.path.join('..','Resources','budget_data.csv')

# Store
PL = 0
Months = 0
Average = 0
Total_PL = 0
Count = 0

with open(pyBank, 'r') as budget_data:
        csvreader = csv.reader(budget_data, delimiter=',')
        print(csvreader)

        header = next(csvreader)
        print(f"HEADER {header}")

# The total number of months included in the dataset
        for rows in csvreader:
                Months += 1
        print("Total Months: " + str(Months))

# The net total amount of "Profit/Losses" over the entire period
        for row in csvreader:
                print(row[1])
                PL += int(row[1])
        print("Profit and loss is: " + str(PL))


# The changes in "Profit/Losses" over the entire period, and then the average of those changes

        for row in csvreader:
                Profit_loss = float(row[1])
                Total_PL += Profit_loss
                Count += 1
                Avg_PL = Total_PL / Count
        print(f'Average Change: ' + str(Avg_PL))

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

                











