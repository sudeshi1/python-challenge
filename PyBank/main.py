# Challenge 1
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.
# Tasks
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-------------------------------------------------------------------------------------------------------------------------------------#

# Import modules
import os
import csv

# Set path for file
PyBankcsv = os.path.join("Resources", "budget_data.csv")
PyBankcsv = r'C:\Users\shrey\Documents\python-challenge\PyBank\Resources\budget_data.csv'

# Lists to store data
months = []
profit_loss = []

# Set variables
total_months = 0
total_profit = 0
profit_changes = 0
initial_profit = 0
final_profit = 0

# Open csv file
with open(PyBankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Skip the header
    csvheader = next(csvreader)
    for row in csvreader:

        # Total number of months in dataset
        total_months = total_months + 1

        # Total amount of Profit/Losses over the entire period
        final_profit = int(row[1])
        total_profit = total_profit + final_profit

        if (total_months == 1):
            # Make the value of previous month to be equal to current month
            initial_profit = final_profit
            continue

        else:

            # Compute change in profit loss 
            profit_changes = final_profit - initial_profit

            # Append each month to the months list
            months.append(row[0])

            # Append each profit change to the profit_loss list
            profit_loss.append(profit_changes)
            initial_profit = final_profit

    # Sum and average of the changes in profit/loss over the entire period
    sum_profit = sum (profit_loss)
    average_profit = round (sum_profit/(total_months - 1), 2)

    # The greatest increase and decrease in profits (date and amount) over the entire period
    increase_profit = max(profit_loss)
    decrease_profit = min(profit_loss)

    # Locate the index value of greatest increase and decrease in profit/loss over the entire period
    increase_month = profit_loss.index(increase_profit)
    decrease_month = profit_loss.index(decrease_profit)

    # Assign greatest increase and decrease month
    highest = months[increase_month]
    lowest = months[decrease_month]

# Print results in terminal
print("---------------------------------------------------")
print("Financial Analysis")
print("---------------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Profits: " + "$ " + str(total_profit))
print("Total Average Change in Profits: " + "$ " + str(average_profit))  
print("Greatest Increase in Profits: " + str(highest) + " ($" + str(increase_profit) + ")")
print("Greatest Decrease in Profits: " + str(lowest) + " ($" + str(decrease_profit)+ ")")
print("---------------------------------------------------")

# Display results to .txt file
# Set path for output file
results = os.path.join("Output", "results.txt")
results = r'C:\Users\shrey\Documents\python-challenge\PyBank\Analysis\results.txt'

with open(results, 'w') as txt:

    # Print the results in .txt file
    txt.write("--------------------------------------------------- \n")
    txt.write("Financial Analysis" + "\n")
    txt.write("---------------------------------------------------" + "\n")
    txt.write("Total Months: " + str(total_months) + "\n")
    txt.write("Total Profits: " + "$ " + str(total_profit) + "\n")
    txt.write("Total Average Change in Profits: " + "$ " + str(average_profit) + "\n")  
    txt.write("Greatest Increase in Profits: " + str(highest) + " ($" + str(increase_profit) + ")" + "\n")
    txt.write("Greatest Decrease in Profits: " + str(lowest) + " ($" + str(decrease_profit)+ ")" + "\n")
    txt.write("---------------------------------------------------" + "\n")
    
