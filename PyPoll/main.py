#import required package
import csv
import os 

#Files to load and output 
file_to_load = os.path.join("..","Resources","election_data.csv")
file_to_output = os.path.join("Election Results.txt")

#create 3 empty variable - list to hold re-read data
voterID = []
counties = []
candidates = []

#Read the csv
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter =",")
    header = next(reader)

#Loop through each row, re-grab each data and store in a new list 
    for row in reader:
        voterID.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
    #use len function on our list to find total_voters in our data
    total_voters = len(voterID)

#using set to know how many counties and candidates actually are in our data. 
# -geeksforgeeks.org (list and set) below 2 lines code is not necessary for this project, 
# but include as future reference if we want to find destinct value on an even larger data set. 
# distinct_counties = list(set(counties))
# distinct_candidate = list(set(candidates))

    #use .count method to find each candidate total vote 
    #use geeksforgeeks.org/python-format-function/
    # originally tried using round function but it doesn't work as it will not display the 0000 after the decimal 
    khan_total = candidates.count("Khan")
    khan_percent = "{:.3f}".format(float(khan_total / total_voters) * 100)
 
    correy_total = candidates.count("Correy")
    correy_percent = "{:.3f}".format(float(correy_total / total_voters) * 100)
    
    li_total = candidates.count("Li")
    li_percent = "{:.3f}".format(float(li_total / total_voters) * 100)

    otooley_total = candidates.count("O'Tooley")
    otooley_percent = "{:.3f}".format(float(otooley_total / total_voters) * 100)

#use PyParagraph class exercise as a reference to write this convenient codes + write to txt file 
output = (
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {total_voters}\n"
    f"------------------------\n"
    f"Khan: {khan_percent}% ({khan_total})\n"
    f"Correy: {correy_percent}% ({correy_total})\n"
    f"Li: {li_percent}% ({li_total})\n"
    f"Otooley: {otooley_percent}% ({otooley_total})\n"
    f"------------------------\n"
    f"Winner: Khan\n"
    f"------------------------\n")
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)