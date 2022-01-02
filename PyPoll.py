# The data we need to retrieve.
# 1. The Total number5 of votes cast.
# 2.A Complete list of candidates who received voters.
# 3. The % of votes each candidates won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on the popular vote.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create total vote variable and create loop to count vote totals
total_votes = 0
candidate_options =[]
candidate_votes = {}
# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count.
        total_votes +=1
    #Print the candidate namee from each row
        candidate_name = row[2]
    #Add the candidate name to the candidate list.
    #If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
        #add it to list of candidates.
            candidate_options.append(candidate_name)
        #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Increase candidates vote
        candidate_votes[candidate_name] +=1
           #1. Iterate through the candidate lsst. 
print(candidate_votes)
for candidate_name in candidate_votes:
            #2 retrieve the vote count of a candidate.
    votes = candidate_votes[candidate_name]
            #3 calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
            #4 Print the candidate name and percentage of votes.
         
#print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning_candidate equal to the candidates name.
        winning_candidate = candidate_name
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
