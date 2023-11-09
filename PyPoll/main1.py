 # First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

election_data = os.path.join("Resources" ,"election_data.csv")
# Define variables 
candidate= {}
candidate_options =[]
number_votes= []
total_votes = 0
percent_votes = []
candidate_name = ""

with open(election_data, newline = "") as csvfile:
# CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvreader)
   
# Read each row of data after the header
   for row in csvreader:
      
      candidate_name = row[2]

      if candidate_name not in candidate_options:
         candidate_options.append(candidate)
         candidate[candidate_name] = 0
         
      candidate [candidate_name] = candidate[candidate_name] +1

for votes in number_votes:
    percent= (votes/total_votes)* 100
    percent = round(percent)
    percentage = "%.3f%%" % percent
    percent_votes.append(percent)

