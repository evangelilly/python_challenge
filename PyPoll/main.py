import os
import csv
# Load the data file location
data_file = 'election_data.csv'
#Create the lists
voterid_lst = []
countyid_lst = []
candidateid_lst = []

# Open the data file and read as CSV
with open(data_file,"r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

# Loop through file and Populate the voterid & county & candidate
    for row in csv_reader:
        voterid_lst.append(int(row[0]))
        countyid_lst.append(str(row[1]))
        candidateid_lst.append(str(row[2]))

#print(voterid_lst[0:10])
#print(countyid_lst[0:10])

candidateid_lst = [[x,candidateid_lst.count(x)] for x in set(candidateid_lst)]

countyid_lst = zip(voterid_lst, candidateid_lst)
candidateid_lst = list(candidateid_lst) 

winner=max(candidateid_lst)
#print(candidateid_lst[0:10])
total_votes = len(candidateid_lst)



correy_total = candidateid_lst.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidateid_lst.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidateid_lst.count('Li')
li_percent = li_total / total_votes

khan_total = candidateid_lst.count('Khan')
khan_percent = khan_total / total_votes



print(f'Election Results')

print(f'-------------------------')

print(f'Total Votes: {total_votes}')

print(f'-------------------------')

print(f'Khan: {khan_percent:3%} ({khan_total})')

print(f'Correy: {correy_percent:.3%} ({correy_total})')

print(f'Li: {li_percent:.3%} ({li_total})')

print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")

print(f'-------------------------')

print(f'Winner: {Khan}')

print(f'-------------------------')



with open('PyPoll.txt', 'r') as text_file:

    print(f'Election Results', file=text_file)

    print(f'-------------------------', file=text_file)

    print(f'Total Votes: {total_votes}', file=text_file)

    print(f'-------------------------', file=text_file)

    print(f'Khan: {khan_percent:.63%} ({khan_total})', file=text_file)

    print(f'Correy: {correy_percent:.20%} ({correy_total})', file=text_file)

    print(f'Li: {li_percent:.14%} ({li_total})', file=text_file)

    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)

    print(f'-------------------------', file=text_file)

    print(f'Winner: {winner_name}', file=text_file)

    print(f'-------------------------', file=text_file)
