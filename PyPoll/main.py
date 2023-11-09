 # First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

election_data = os.path.join("Resources" ,"election_data.csv")
# Define variables 
candidate_dict= {}
candidate_options =[]
number_votes= []
total_votes = 0
percent_votes = []
candidate_name = ""
winner_name = ""
winner_votes = 0

with open(election_data, newline = "") as csvfile:
# CSV reader specifies delimiter and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')
  next(csvreader)
# Read each row of data after the header
  for row in csvreader:
      total_votes += 1 
      candidate_name = row[2]

      if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)
         candidate_dict[candidate_name] = 0
         
      candidate_dict[candidate_name] = candidate_dict[candidate_name] +1

     
with open("Analysis/text.txt","w") as outfile:
  results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

  print(results,)
  outfile.write(results)
  
  for candidate in candidate_options:
    votes = candidate_dict[candidate]
    percent= votes/total_votes* 100

    voter_output = f"{candidate}: {percent:.3f}% ({votes})\n"

    print(voter_output)
    outfile.write(voter_output)

    if votes > winner_votes:
       winner_votes= votes
       winner_name = candidate

  
  winning_candidate = (
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")
  print(winning_candidate)
  outfile.write(winning_candidate)
