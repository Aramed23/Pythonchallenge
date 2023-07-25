# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

budget_data = os.path.join("budget_data.csv")
 
# Define variables 
month = 0 
Total=0
Profitlist=[]
change = 0
previous = 0
Dates = []
with open(budget_data, newline= "") as csvfile:
   
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
# Keeping track of the dates
        Dates.append(row[0])
        
        # Month tracker
        month= month +1 
       # Total of profit & loss over entire time
        Total= Total+int(row [1])
        # caculate change over time 
        change = int(row [1])- previous
        previous = int(row [1])
        Profitlist.append(change)
        previous = int(row [1])
    
        
         #Greatest increase in profits
        greatest_increase = max(Profitlist)
        greatest_index = Profitlist.index(greatest_increase)
        greatest_date = Dates[greatest_index]
        
         # Greatest decrease in profits
        greatest_decrease=  min(Profitlist)
        lowest_index = Profitlist.index(greatest_decrease)
        lowest_date = Dates[lowest_index]

        #Avg change in profit & loss 
        Avg_change = sum(Profitlist)/len(Profitlist)
        
    
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total months: {month}")
print(f"Total : {Total}")
print(f"Average change: ${str(round(Avg_change,2))}")
print(f"Greatest Increases in profits:{greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decreases in profits:{lowest_date} (${str(greatest_decrease)})")
      

