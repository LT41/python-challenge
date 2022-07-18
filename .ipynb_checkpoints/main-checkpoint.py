# PyBank Module 2 Challenge -- Luke Turner
# Importing 
from pathlib import Path
import csv

# Declaring variables and lists 
dates = []
total_profit = []
high_low_list = []

total_months = 0
total_profits = 0
profit = 0 
min_profit = 0
average_change = 0

# File Path

csv_path = Path('budget_data.csv')

with open(csv_path, 'r') as csv_path:
    budget_data = csv.reader(csv_path, delimiter = ',')
    header = next(budget_data)
    for line in budget_data:
        
        total_months += 1
        dates.append(str(line[0]))
        total_profit.append(int(line[1]))
        total_profits = sum(total_profit)
        
        profit = int(line[1])
    
        # Assigns a new list that iterates through the list total_profit and returns a value subtracting each number from the one that preceded it to find the change from day to day 
        
        high_low_list = [total_profit[i+1] - total_profit[i] for i in range(len(total_profit) - 1)]
        
        for num in high_low_list:
            if profit < num:
                profit = num
            if min_profit > num:
                min_profit = num
                
       #Setting final variables 
    
average_change = ((total_profit[-1] - (total_profit[0])) / (len(total_profit) - 1))
    
    # Probably there is a cleaner way to do this, but to find the corresponding dates to the highest and lowest profit days, I took the elements for those numbers and made their indexes an integer variable
    # I then plugged those variables into the dates list that I made above so they correspond to the high and low price data. 
    # It was necessary to add 1 to the index becasue the lists work by subtracting a number from the one that preceded it. 
    
index_max = (int(high_low_list.index(profit))+1)
index_min = (int(high_low_list.index(min_profit))+1)
date_of_max = dates[index_max]
date_of_min = dates[index_min]

# Printing results

print ('Financial Analysis' + '\n' * 2)
print ('----------------------------' + '\n' * 2)
print (f'Total Months: {total_months}' + '\n' * 2)
print (f'Average Change: ${round(average_change, 2)}' + '\n' * 2)
print (f'Greatest Increase in Profits: {date_of_max} ${profit}' + '\n' * 2) 

# Writing results to a txt file: 

with open('pybank_results.txt' , 'w') as txt:
    
    txt.write('Financial Analysis' + '\n' * 2)
    txt.write('----------------------------' + '\n' * 2)
    txt.write(f'Total Months: {total_months}' + '\n' * 2)
    txt.write(f'Average Change: ${round(average_change, 2)}' + '\n' * 2)
    txt.write(f'Greatest Increase in Profits: {date_of_max} ${profit}' + '\n' * 2) 
    txt.write(f'Greatest Decrease in Profits: {date_of_min} ${min_profit}' + '\n' * 2)