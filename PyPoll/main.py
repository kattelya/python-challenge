#import required package
import csv
import os 

#Files to load and output 
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("Election Results.txt")

#create 3 variables to hold re-read files that store as a list 
voterID = []
counties = []
candidates = []

#Read the csv and conver it into a list 
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter =",")
    header = next(reader)

#Loop through each row, re-grab each data and store in a new list 
    for row in reader:
        voterID.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
    
    total_voters = len(voterID)
    #using set to know how many counties and candidates actually are in our data. -geeksforgeeks.org (list and set)
    distinct_counties = list(set(counties))
    distinct_candidate = list(set(candidates))

    #use .count method to find each candidate total vote and convert -- "stackoverflow.com/questions/14540143/python-3-float-decimal-points-precision" = learn from this website to format the percent result"
    khan_total = candidates.count("Khan")
    khan = float(khan_total / total_voters) * 100
    khan_percent = "{:.3f}".format(khan)

    correy_total = candidates.count("Correy")
    correy = float(correy_total / total_voters) * 100
    correy_percent = "{:.3f}".format(correy) 

    li_total = candidates.count("Li")
    li = float(li_total / total_voters) * 100
    li_percent = "{:.3f}".format(li)

    otooley_total = candidates.count("O'Tooley")
    otooley = float(otooley_total / total_voters) * 100
    otooley_percent = "{:.3f}".format(otooley)

    print(khan_total, correy_total, otooley_total, li_total)
    print(khan_percent, correy_percent, li_percent, otooley_percent)
    
    #to find the percentage - each candidate total votes divided by total number votes (total_voters)

print(distinct_counties)
print(distinct_candidate)
output = (
    f"\nElection Results\n"
    f"------------------------\n"
    f"Total Votes: {total_voters}\n"
    f"------------------------\n"
    f"Khan: {khan_percent}% ({khan_total})\n"
    f"Correy: {correy_percent}% ({correy_total})\n"
    f"Li: {li_percent}% ({li_total})\n"
    f"Otooley: {otooley_percent}% ({otooley_total})\n"
    f"------------------------\n"
    f"Winner: Khan\n"
    f"------------------------"
)
print(output)
