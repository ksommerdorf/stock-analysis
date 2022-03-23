# Assign a variable for the file to lead and the path.
#file_to_load = r'C:\Users\Kaylaa\Documents\Bootcamp\03-Python\Resources\election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
#To do: perform analysis.
# Close the file.
#election_data.close()
# Open the election results and read the file
#with open(file_to_load) as election_data:

    #To do: perform analysis.
    #print(election_data)
# The data we need to retrieve.
import csv
import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join(".", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_date:
    # Print the file object.
    # print(election_data)
#Import the datetime classs  from the datetime module
#import datetime
#Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
#Print the present time
#print("The time right now is ", now)
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
    # Using the open() function with the "w" mode we will write data to the file
    #outfile = open(file_to_save,"w")
# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
# Write some data to the file
    #outfile.write("Hello World")
#txt_file.write("Hello World")
    #Close file
    #outfile.close()
# Write three counties to the file
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
total_votes = 0
candidate_options = []
candidate_votes = {}
vote_percentage = 0
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    #print(headers)
# 1. The total number of votes cast
    for row in file_reader:
        total_votes += 1
# 2. A complete list of candidates who received votes
    # Print the candidate name from each row
        candidate_name = row[2]
    # Add the candidate name from each row
    #candidate_options.append(candidate_name)
    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# 3. The percentage of votes each candidate won
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
# 4. The total number of votes each candidate won
    # Determine if the the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
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
# 5. The winner of th election based on popular vote. 