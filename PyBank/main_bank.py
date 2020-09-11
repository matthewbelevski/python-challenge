import os
import csv

# finds the budget_data csv using the os module
main_bank_csv = os.path.join('PyBank', 'Resources','budget_data.csv')

# lists to store data as I split the columns into date and price. I created an extra, avgchange to calculate the average change and started it with zero since the first month has no change
date = []
price = []
avgchange = [0]
#avgchange2 = [] 
avgchange3 = [0]

# opens the csv file to start manipulating it
with open(main_bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #removes the header
    header = next(csvreader,None)
    #starts a for loop to split the columns into lists
    for row in csvreader:
        date.append(row[0])
        price.append(float(row[1]))
        avgchange.append(float(row[1]))

    # deletes the last figure in the avgchange so the columns match  up    
    del avgchange[-1]
    # counts the elements in the date list to determine the number of months
    totalmonths = (len(date))
    # sums the values in the Profit/Loss list
    net_total = sum(price)
    # zips the lists price and avgchange together and minuses the correspending element and creates a new list
    avgchange2 = [a - b for a, b in zip(price, avgchange)]
    del avgchange2[0]

    #avgchange3.append(avgchange2)
    # finds the max value in the avgchange2 list to determing the highest average change
    max_change = max(avgchange2)
    # finds the min value in the avgchange2 list to determing the lowest average change
    min_change = min(avgchange2)
    # finds the average value of the avgchange2 list
    avg_change = sum(avgchange2) / len(avgchange2)
    
    # finds the index value of the max and min change values to be used to find the corresponding date element. adds 1 as avgchange2 has 1 less element
    index_max = avgchange2.index(max_change) + 1
    index_min = avgchange2.index(min_change) + 1
    #max_change_date = 
    # finds and stores the corresponding date value to the above to be used when printing the max and min values
    index_max_date = date[index_max]
    index_min_date = date[index_min]

    #print(round(net_total))
    #print(totalmonths)
    #print(avgchange)
    #print(avgchange2)
    #print(round(max_change))
    #print(round(min_change))
    #print(round(avg_change,2))
    #print(index_max)
    #print(index_min)
    #print(index_max_date)

#print("Financial Analysis")
#print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
#print("Total Months: ", str(totalmonths))
#print("Total: $", str(round(net_total)))
#print("Average Change: $", str(round(avg_change,2)))
#print("Greatest Increase in Profits: $", str(index_max_date), str(round(max_change)))
#print("Greatest Decrease in Profits: $", str(index_min_date), str(round(min_change)))
    
#print(avgchange3) 
# stores the prints as seperate lines to make it easier when writing the text document. rounds the figures to make them look more user friendly   
line1 = ("Financial Analysis")
line2 = ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
line3 = (f"Total Months: {totalmonths}")
line4 = (f"Total: ${(round(net_total))}")
line5 = (f"Average Change: $ {(round(avg_change,2))}")
line6 = (f"Greatest Increase in Profits:  {index_max_date} (${(round(max_change))})")
line7 = (f"Greatest Decrease in Profits:  {index_min_date} (${(round(min_change))})")

# prints the above into the terminal
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

# sets the directory to create the text file
output_file = os.path.join('PyBank', 'Analysis','financial_analysis.txt')

# creates the output text file and prints the lines '\n' is used to print them onto seperate lines
with open(output_file, "w") as text_file:
    text_file.writelines([line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7])
   
