import os
import csv

#Pathing to collect data from Resources folder & Export data to text
pyBank = os.path.join('..','Resources','budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")

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
        T_Months = print("Total Months: " + str(Months))
        
        # Output file to txt
        with open(file_to_output, "a") as txt_file:
                txt_file.write(T_Months)

# The net total amount of "Profit/Losses" over the entire period
        for row in csvreader:
                print(row[1])
                PL += int(row[1])
        T_PL = print("Profit and loss is: " + str(PL))

        # Output file to txt
        with open(file_to_output, "a") as txt_file:
                txt_file.write(T_PL)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

        for row in csvreader:
                Profit_loss = float(row[1])
                Total_PL += Profit_loss
                Count += 1
                Avg_PL = Total_PL / Count
        AVG_PL = print(f'Average Change: ' + str(Avg_PL))

        # Output file to txt
        with open(file_to_output, "a") as txt_file:
                txt_file.write(AVG_PL)

# The greatest increase in profits (date and amount) over the entire period

        # Output file to txt
        with open(file_to_output, "a") as txt_file:
                txt_file.write()
# The greatest decrease in profits (date and amount) over the entire period

        # Output file to txt
        with open(file_to_output, "a") as txt_file:
                txt_file.write()

                











