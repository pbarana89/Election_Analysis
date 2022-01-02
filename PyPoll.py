# The data we need to retrieve.
# 1. The Total number5 of votes cast.
# 2.A Complete list of candidates who received voters.
# 3. The % of votes each candidates won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on the popular vote.
#Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
File_to_load = 'Resources/election_results.csv'

#Use the with statement to open the file as a text file.
File_to_save = 'Analysis/election_analysis.txt'
with open(File_to_save, "w") as txt_file:
# Write some data to the file.
    with open(File_to_load) as election_data:
#close the file
#txt_file.close()
# Read the file object with the reader function.
        file_reader = csv.reader(election_data)

# Print the header row.
        headers = next(file_reader)
        print(headers)
# Print each row in the csv file.
        for row in file_reader:
            print(row)
# print(election_data)
