import os
import csv

#imports counter module
from collections import Counter

id_ = []
county = []
name = []

new_list = []

main_poll_csv = os.path.join('PyPoll', 'Resources','election_data.csv')

with open(main_poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #removes the header
    header = next(csvreader,None)

    for row in csvreader:
        #id_.append(row[0])
        #county.append(row[1])
        name.append(row[2])
        #name_dict = dict((row[2]) for row in csvreader)

#my_dict = {i.name.count(i) for i in name}

name.sort(key=len)

#sorts names by the total number of elements
sorted_name = [item for items, c in Counter(name).most_common() for item in [items] * c] 

#determines the winner by counting the elements and then providing the most common, like working out the mode
winner = Counter(name).most_common(1)[0][0]

#counts the votes by turning name into a dictionary
votes = dict(Counter(name))

#creates a temporary dictionary called sorted_votes which has all the names sorted by their total votes
sorted_votes = dict(Counter(sorted_name))

#prints the sorted votes dictionary showing the totals of the sublists
#print(f"Sorted by total votes: {sorted_votes}")

#creates the sublists within the list sorted_names by looping through and appending the next value to the value above if it's the same otherwise it creates a new sublist
for value in sorted_name:
    if new_list and new_list[-1][0] == value:
        new_list[-1].append(value)
    else:
        new_list.append([value])

#Just gets the candidates names
can_names = [item[0] for item in new_list]
#print("The candidates are:", can_names)

#finds the longest sublist
#highest_votes = len(max(new_list,key=len))

#calculates the total number of elements within the list name
total_votes = len(name)
#print(f"The total votes are: {votes}")

#calculates the percentage of votes the candidates received 
vote1_result = len(new_list[0]) / total_votes * 100
vote2_result = len(new_list[1]) / total_votes * 100
vote3_result = len(new_list[2]) / total_votes * 100
vote4_result = len(new_list[3]) / total_votes * 100

line1 = ("Election Results")
line2 = ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
line3 = (f"Total Votes: {total_votes}")
line4 =("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
line5 = (f"{can_names[0]}: {(round(vote1_result,3))}% ({len(new_list[0])})")
line6 = (f"{can_names[1]}: {(round(vote2_result,3))}% ({len(new_list[1])})")
line7 = (f"{can_names[2]}: {(round(vote3_result,3))}% ({len(new_list[2])})")
line8 = (f"{can_names[3]}: {(round(vote4_result,3))}% ({len(new_list[3])})")
line9 = ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
line10 = (f"Winner: {winner}")
line11 = ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

#prints the results
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(line10)
print(line11)

# sets the directory to create the text file
output_file = os.path.join('PyPoll', 'Analysis','poll_analysis.txt')

# creates the output text file and prints the lines '\n' is used to print them onto seperate lines
with open(output_file, "w") as text_file:
    text_file.writelines([line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7 + '\n' + line8 + '\n' + line9 + '\n' + line10 + '\n' + line11])