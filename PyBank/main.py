import os     
import csv

# Load the data file location
data_file = "budget_data.csv"

#Create the lists
month_lst = []
pnl_lst = []

# Open the data file and read as CSV
with open(data_file,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

# Loop through file and Populate the month_lst & pnl_lst
    for row in csv_reader:
        month_lst.append(str(row[0]))
        pnl_lst.append(int(row[1]))

# the total number of months included in the sheet
num_months = len(month_lst)
print("Print total Months -> ", num_months)

net_pnl = 0

for i in pnl_lst:
    net_pnl = net_pnl + i

# define the average profit/loss list
monthly_avg_change_lst = []
previous_month = 0

# print("Print PNL List -> ", pnl_lst)

for i in range(len(pnl_lst)):
    if i == 0:
        previous_month = pnl_lst[i]
    else:
        monthly_change = pnl_lst[i] - previous_month
        monthly_avg_change_lst.append(monthly_change)
        previous_month = pnl_lst[i]


#  Calculate the monthly average change by deviding the number rows with total sum of PNL Values


# get the total row_count for the months
row_count = len(monthly_avg_change_lst)

# Add PNL values together
total = sum(monthly_avg_change_lst)

print("total row_count and total amount -> ", row_count, total)

pnl_avg = total / row_count
print("Print PNL Average (row_count / total) -> ", pnl_avg)

#Round pnl_avg to 2 decimal places 
pnl_avg = round(pnl_avg, 2)
print("Print PNL Average Rounded to 2 decimal -> ", pnl_avg)


# the highest and lowest profit/loss and their months

# Set all variables to known state
highest_month = ''
highest_amount = 0
lowest_month = ''
lowest_amount = 0


for i in range(len(monthly_avg_change_lst)):

    # For each of the values in the list, compare next value in month_avg_lst to current highest_amount, 
    # if 1st value is higher than current value, reset highest value to current list value, ultimately     
    # leaving the hight number assigned 
    if monthly_avg_change_lst[i] > highest_amount:
        highest_amount = monthly_avg_change_lst[i]
        highest_month = month_lst[i+1]
    # Sme as above, but populate the lower values.
    elif monthly_avg_change_lst[i] < lowest_amount:
        lowest_amount = monthly_avg_change_lst[i]
        lowest_month = month_lst[i+1]


print(f'Total Months:{num_months} ')
print(f'Total: ${net_pnl}.')
print(f'Average Change: {pnl_avg}.')
print(f'Greatest Increase in Profits: {highest_month}  (${highest_amount})')
print(f'Greatest Dcrease in Profits: {lowest_month}  (${lowest_amount})')
