import os
import csv

#Pathing to collect data from Resources folder & Export data to text
PyPoll = os.path.join('..','Resources','election_data.csv')
file_to_output = os.path.join("analysis", "election_analysis.txt")


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
        for row in csvreader:
            total_votes += 1
            candidate = row[2]

            if candidate in candidates:
                    candidates[candidate] += 1
            else:
                    candidates[candidate] = 1

        print(f"```text")
        print(f"Election Results")
        print(f"----------------------------")
        print(f"Total Votes: {vote_total}")
        print(f"----------------------------")

        T_Candidates = (
        f"```text\n"
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"----------------------------\n"
        )

        # Output file to txt
        with open(file_to_output, "w") as txt_file:
                txt_file.write(T_Candidates)

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

        Candiate_Details = (f"{candidate} : {per_form}% ({final_list[candidate]})\n")

            # Appending output file with results
        with open(file_to_output, "a") as txt_file:
                txt_file.write(Candiate_Details)


# The winner of the election based on popular vote
        if candidates[candidate] > winning_candidate:
              winning_candidate = candidates[candidate]
              winner = candidate
              W_Candidate = (
                    f"----------------------------\n"
                    f"Winner: {winner}\n"
                    f"----------------------------\n"
                    f"```\n")
              
# Printing results in terminal
        print(W_Candidate)
# Appending output file
        with open(file_to_output, "a") as txt_file:
                txt_file.write(W_Candidate)