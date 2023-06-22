
import os
import csv

# Part 1 of the Assignmnet 3 - Python challenge
datavalue=os.path.join('Resources/budget_data.csv')

# this is the assignment relating to Week 3 - python challenge
# it reads the csv file and finds the value for certain things
# this is helpful to run script quickly rather than manually finding it

# this here is opening the csv and setting up variables + skips the headers
with open(datavalue) as csvfile:
    datavalue = csv.reader(csvfile,delimiter=",")
    header = next(datavalue)

    # these are variables specific for the functions, the max/min values have "inf", this means that it will keep growing and update the min/max value until it has ran through
    # all of the datas
    
    num_months = 0.0
    num_amounts = 0.0
    max_value = float("-inf")
    min_value = float("inf")
    max_date = ""
    min_date = ""
# this one counts how many months is in the data
    for row in datavalue:
        num_months += 1
# this one adds all of the values from the second column to get the total value
        secondrow = int(row[1])
        num_amounts = num_amounts + secondrow

# these two finds the highest/lowest values 
        amount = int(row[1])
        if amount > max_value:
            max_value = amount
            max_date = row[0] 

        if amount < min_value:
            min_value = amount
            min_date = row[0] 

print("Financial Analysis")
print("-----------------------------------------------------")
print("Total months: ", num_months)
print("total amount: ", num_amounts)
print("highest increase: ", max_value,"- Date: ", max_date)
print("lowest increase: ", min_value,"- Date: ", min_date)


file_to_output=os.path.join('Analysis/exported_budget_result.txt')

output = (
    "Financial Analysis\n"
    "----------------------------------------------------\n"
    f"Total months: {num_months}\n"
    f"Total amount: {num_amounts}\n"
    f"Highest increase: {max_value} - Date: {max_date}\n"
    f"Lowest increase: {min_value} - Date : {min_date}\n"
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)



# Part 2 of the Assignment 3-Python challenge
votevalue=os.path.join('Resources/election_data.csv')

with open(votevalue) as csvfile:
    votevalue = csv.reader(csvfile,delimiter=",")
    header = next(votevalue)

    num_vote = 0.0
    
    canadites_options = []    
    canadites_votes = []
    percent = []
    vote = 0
    
    for row in votevalue:
        # counts the total vote
        num_vote += 1
        # adds all unique names 
        name = row[2]    
        if name not in canadites_options:
            canadites_options.append(name) 
            canadites_votes.append(0)
         # adds votes connected to the names
        vote = 1
        canadites_votes[canadites_options.index(name)] += 1
        # takes the total canadites vote and convert into percentage
total_vote = sum(canadites_votes)
for num_percent in canadites_votes:
     canadites_percent = (num_percent/total_vote)
     percent_vote = "{0:.0%}".format(canadites_percent)
     percent.append(percent_vote)
#   merges the name, percent and number of vote together for printing.
overall_info = zip(canadites_options, percent, canadites_votes)
information = list(overall_info)
winner = max(information, key=lambda x:x[2])


print("Election Results")
print("--------------------------------------------")
print("Total vote: ", num_vote)
print("--------------------------------------------")
print("Name, vote percent, total vote")
print(information)
print("--------------------------------------------")
print("Winner: ", winner)

file_to_output=os.path.join('Analysis/exported_vote_result.txt')

output = (
    "Election Results\n"
    "----------------------------------------------------\n"
    f"Total vote:  {num_vote}\n"
    "----------------------------------------------------\n"
    f"Name, vote percent, total vote\n"
    f"{information}\n"
    "----------------------------------------------------\n"
    f"Winner: {winner} \n"
    
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
