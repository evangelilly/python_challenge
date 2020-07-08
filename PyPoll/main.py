import csv
PyPoll = "election_data.csv"

# Load the data file location
data_file = os.path.join ("Resources", "election_data.csv")

vote_count = 0 
most_vote = {}
candidate_dict = {}


for row in election_data:
 vote_count += 1
candidate_dict[row[2]] = candidate_dict.get(row[2], 0) + 1

print()
print(f'Election Results')
print(f'----------------------------')
print(f'Total vote: {vote_count}')
print(f'----------------------------')


for candidate, vote in candidate_dict.items():
print(f'{candidate}: {vote / vote_count * 100:.3f}% ({vote})')
if vote > most_vote:
vote = most_vote 
winner = candidate
        
print(f'----------------------------')
print(f'Winner: {winner}')
print(f'----------------------------')
