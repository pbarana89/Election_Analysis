counties = ["Arapahoe", "Denver", "Jefferson"]
counties[0]

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
if  percentage_votes >=50.01:
    print("You won!")
else: 
    print("I'm sorry! You didn't win.")
print("I received " + str(percentage_votes)+"% of the total votes.")