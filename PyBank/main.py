#import required packages 
import csv 
import os 

#Files to load and output
file_to_load = os.path.join( "budget_data.csv")
file_to_output = os.path.join("Financial Analysis.txt")

#Placeholders for re-formatted contents 
months_total = []
total_value = []
avg_change = []

#Read the csv file and skip the header - class discussion
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data, delimiter =",")
    header = next(reader)

#Loop through each row, re-grab each data and store in a new list - similar to example in PyBoss / Paragraph exercise
    for row in reader:
        months_total.append(row[0])
        total_value.append(row[1])
    #use len function to find the length of the list = to total months in our report.
    months = len(months_total)
    #since the list that we copy is a string, need to convert string to an integer before we can perform any calculations. 
    total_value = [int(i) for i in total_value]
    total = sum(total_value)

#I have something similar in mind but struggling to write the code. Once I saw this code at "http://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in" it helps a lot. This chunk of code loop through the entire length specificly on total_value list and manipulate using their index in order to perform our computation
    for i in range(1, len(total_value)):
        avg_change.append(total_value[i] - total_value[i-1])
        average = round((sum(avg_change) / len(avg_change)), 2)
        max_val_change = max(avg_change)
        min_val_change = min(avg_change)

# to read from months_total list using the .index build in function in python and with specific value that match max or min - concept taken from geeksforgeeks    
    max_val_change_date = str(months_total[avg_change.index(max(avg_change))])
    min_val_change_date = str(months_total[avg_change.index(min(avg_change))])

#use PyParagraph class exercise as a reference to write this convenient codes + write to txt file 
output = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total month: {months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {max_val_change_date} (${max_val_change})\n"
    f"Greatest Decrease in Profits: {min_val_change_date} (${min_val_change})\n")
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)