# Create a script to give results of a small county election

# Imports
import os
import csv

# Variables for storing data
vote_list = []
unique_candidates = []

candidate_votes = []
candidate_vote_percent = []

total_votes = 0

winning_vote_percent = 0.000
winner = ""

# filepath for election data
election_csv = os.path.join("Resources", "election_data.csv")

# read data in variables from file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header
    csv_header = next(csvreader)

    for row in csvreader:
        vote_list.append(row[2])

# Get the total votes
total_votes = len(vote_list)

# Get a list of unique candidates and add spot to candidate votes and percent
for name in vote_list:
    if name in unique_candidates:
        continue
    else:
        unique_candidates.append(name)
        candidate_votes.append(0)
        candidate_vote_percent.append(0)

# Get votes per candidate (i.e. count the number of times their name appears in vote list)

for candidate in unique_candidates:
    votes = 0 # reset vote count
    for name in vote_list:
        if name == candidate:
            votes += 1
    candidate_votes[unique_candidates.index(candidate)] = votes

# Calculate each candidates vote percent and print results to console

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")
for i in range( len(unique_candidates) ):
    candidate_vote_percent[i] = round( candidate_votes[i]/total_votes * 100, 3)
    print(f"{unique_candidates[i]}: {candidate_vote_percent[i]}% ({candidate_votes[i]})")
# get winning percentage
for percent in candidate_vote_percent:
     if winning_vote_percent == 0.000 or percent > winning_vote_percent:
        winning_vote_percent = percent
# match with the candidate
for i in range( len(unique_candidates) ):
    if candidate_vote_percent[i] == winning_vote_percent:
        winner = unique_candidates[i]

print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")    

# Set variable for output file
output_file = os.path.join("Analysis", "analysis.txt")

#  Open the output file to write a text file of data
with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)

    # Write the header row
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------"])
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["-------------------------------"])
    for i in range( len(unique_candidates) ):
        writer.writerow([unique_candidates[i] + ": " + str(candidate_vote_percent[i]) + "% (" + str(candidate_votes[i]) + ")"])
    writer.writerow(["-------------------------------"])
    writer.writerow(["Winner: " + winner])
    writer.writerow(["-------------------------------"])