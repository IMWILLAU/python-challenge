import os
import csv


# Pathing to collect and export data
PyPoll = os.path.join('..','Resources','election_data.csv')

# Vote store
total_votes = 0
candidates = {}
winning_candidate = ''
max_votes = 0

# List for storing values for candidates and vote calculation
final_list = {}
winner = ""
unique_candidates = set()

with open(PyPoll, 'r') as election_data:
        csvreader = csv.DictReader(election_data, delimiter=',')
        print(csvreader)

        header = next(csvreader)
        print(f"HEADER {header}")


# The total number of votes cast
        for row in PyPoll:
            total_votes += 1
            candidate = row[2]

            if candidate in candidates:
                    candidates[candidate] += 1
            else:
                    candidates[candidate] = 1

        print(candidates)

# A complete list of candidates who received votes
        for row in PyPoll:
            candidate = row["Candidate"]
            unique_candidates.add(candidate)

        print("Unique Candidates: ")
        for candidate in unique_candidates:
            print(candidate)
# The candidate, percentage and number of votes
        for candidate in final_list:
              
              percentage = (final_list[candidate]/vote)*100
              per_form = "{:.3f}".format(percentage)

              print(candidate + ": " + str(per_form) + "%" + " (" + str(final_list[candidate]) + ")")

# The winner of the election based on popular vote
        if candidates[candidate] > winning_candidate:
              winning_candidate = candidates[candidate]
              winner = candidate
              print(
                    f"----------------------------\n"
                    f"Winner: {winner}\n"
                    f"----------------------------\n"
                    f"```\n")
              
with open(...)