# Challenge 2
# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Tasks
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-------------------------------------------------------------------------------------------------------------------------------------#

# Import modules
import os
import csv

# Set path for file
PyPollcsv = os.path.join("Resources", "election_data.csv")
PyPollcsv = r'C:\Users\shrey\Documents\python-challenge\PyPoll\Resources\election_data.csv'

# Lists to store data
candidates = []
num_votes = []
percent_votes = []

# Set variables
total_votes = 0

# Open csv file
with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Skip the header
    csvheader = next(csvreader)
    for row in csvreader:
# Total number of votes cast
        total_votes = total_votes + 1
# A complete list of candidates who received votes
# Appending candidate names list
        name_candidate = row[2]
# Condition for if candidate does not match any candidates
        if name_candidate not in candidates:
            candidates.append(name_candidate)
            index = candidates.index(row[2])
            num_votes.append(1)
        else: 
            index = candidates.index(row[2])
            num_votes[index] += 1
# Percentage of votes each candidate won and the total number of votes each candidate won
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

# Winner of the election based on popular vote
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]
            
# Print results in terminal
print("---------------------------------------------------")
print("Election Results")
print("---------------------------------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print(f"Winner: {winning_candidate}")  
print("---------------------------------------------------")

# Display results to .txt file
# Set path for output file
results = os.path.join("Output", "results.txt")
results = r'C:\Users\shrey\Documents\python-challenge\PyPoll\Analysis\results.txt'

with open(results, 'w') as txt:

    # Print the results in .txt file
    txt.write("--------------------------------------------------- \n")
    txt.write("Election Results" + "\n")
    txt.write("--------------------------------------------------- \n")
    txt.write("Total Votes: " + str(total_votes) + "\n")
    txt.write("--------------------------------------------------- \n")
    for i in range(len(candidates)):
        txt.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})" + "\n")
    txt.write("Winner: " + str(winning_candidate) + "\n")  
    txt.write("--------------------------------------------------- \n")

    

