## PyBank Challenge:
## Read the CSV
## Count the rows to find the months
## Find the sum the profit/losses
## Find the average profit/loss per month
## Find the month with the greatest increase
## Find the month with the greatest decrease

import csv
import os

## Open our CSV and create an analysis text file
budget_csv = os.path.join(r"C:\Users\nnoar\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv")
analysis_txt = os.path.join(r"C:\Users\nnoar\OneDrive\Desktop\python-challenge\PyBank\Analysis\analysis.txt")

#Create variables
total_months = 0
total_pl = 0
total_pl_change = 0
#Read our CSV
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    row = next(csvreader)
    greatest_month = row[0]
    least_month = row[0]
    pl = float(row[1])
    greatest_pl = pl
    least_pl = pl
    previous_pl = pl
    total_months = 1
    total_pl = float(row[1])
    total_pl_change = 0

    #Read each line
    for row in csvreader:

        total_months = total_months + 1
        pl = float(row[1])
        total_pl = pl + total_pl
        pl_change = pl - previous_pl
        total_pl_change = total_pl_change + pl_change

        #Find the max and min of Profit/loss change
        if pl_change > greatest_pl:
            greatest_month = row[0]
            greatest_pl = pl_change

        if pl_change < least_pl:
            least_month = row[0]
            least_pl = pl_change
        previous_pl = pl
    average_pl = total_pl/total_months
    average_change = total_pl_change/(total_months - 1)

    print(f"Financial Analysis")
    print(f"-----------------------------------------------------------")
    print(f"Total Months: " + str(total_months))
    print(f"Total: $" + str(total_pl))
    print(f"Average Change: $" + str(average_change))
    print(f"Greatest Increase in Profits: " + str(greatest_month)+ " $" + str(greatest_pl))
    print(f"Greatest Decrease in Profits: " + str(least_month + " $" + str(least_pl)))

#Write to a text file
with open("analysis.txt", "w") as text:
    text.write(f"Financial Analysis\n")
    text.write(f"-----------------------------------------------------------\n")
    text.write(f"Total Months: " + str(total_months) +"\n")
    text.write(f"Total: $" + str(total_pl) +"\n")
    text.write(f"Average Change: $" + str(average_change)+"\n")
    text.write(f"Greatest Increase in Profits: " + str(greatest_month)+  "$" + str(greatest_pl)+"\n")
    text.write(f"Greatest Decrease in Profits: " + str(least_month) +  "$" + str(least_pl)+"\n")


    




