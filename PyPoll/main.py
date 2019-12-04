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
    #using set to know how many counties and candidates actually listed from all the big data!
    distinct_counties = list(set(counties))
    distinct_candidate = list(set(candidates))
print(total_voters)
#
print(distinct_counties)
print(distinct_candidate)


