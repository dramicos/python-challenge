# Creating a script to analyse financial records.

# imports
import os
import csv

# Setting the file path
csvpath = os.path.join("Resources", "budget_data.csv")

# Create and ititialize variables to be reported on
# Create variable to store the months count and initialize and to get the data
total_months = 0
date = []

# Create variable to store the total profit/loss over time and initialize
total_profit = 0

# Create variables for saving the average change
average_profit_change = 0
average_profit_change_total = 0
average_profit_change_l = []

# Create variables to show average change in profit/loss over time
profit_change = []


# Create variable to capture the greatest increase in profit (date and amount)
greatest_profit = 0
greatest_profit_date = ""

# Create variable to capture the greatest loss (date and amount)
greatest_loss = 0
greatest_loss_date = ""


# Open cvs file
with open(csvpath, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # skip the header
    csv_header = next(csvreader)
  
    # count the remaining rows to count the months, populate profit change array, calculate total
    for row in csvreader:
        total_months += 1
        profit_change.append( int( row[1] ) )
        total_profit += int( row[1] )
        date.append( row[0] )
          
    # sort through the lists to pick out the biggest changes   
         
    for i in range(len(profit_change)):
        # to get the difference need to start at the 2nd index
        if i != 0:
            average_profit_change_total += profit_change[ i ] - profit_change[ i -1]
            if profit_change[ i ] - profit_change[ i -1] > greatest_profit:
                greatest_profit = profit_change[ i ] - profit_change[ i -1]
                greatest_profit_date = date[i]
            
            if profit_change[ i ] - profit_change[ i -1] < greatest_loss:
                greatest_loss = profit_change[ i ] - profit_change[ i -1]
                greatest_loss_date = date[i]
            
    # Calculate the average profit change not forgetting to remove one since counting from the 2nd point
    average_profit_change = round( average_profit_change_total / (len(profit_change) - 1), 2)

    # Print to console
    print("Financial Analysis")
    print("-------------------------------------")    
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_profit_change}")
    print(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit})")
    print(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})")

# Set variable for output file
output_file = os.path.join("Analysis", "analysis.txt")

#  Open the output file to write a text file of data
with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------------"])
    writer.writerow(["Total Months: " + str(total_months)])
    writer.writerow(["Total: " + str(total_profit)])
    writer.writerow(["Average Change: $" + str(average_profit_change)])
    writer.writerow(["Greatest Increase in Profits: " + str(greatest_profit_date) + " $(" + str(greatest_profit) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(greatest_loss_date) + " $(" + str(greatest_loss) + ")"])
    
    



