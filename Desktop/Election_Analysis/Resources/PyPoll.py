# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes
import os
import csv
file_to_save = os.path.join("desktop", "Election_Analysis", "analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
      txt_file.write ("Arapahoe, ")
      txt_file.write("Denver, ")
      txt_file.write("Jefferson")
file_to_load = os. path.join("desktop", "Election_Analysis", "Resources", "election_results.csv")
file_to_save = os.path.join("desktop", "Election_Analysis", "analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
      file_reader = csv.reader(election_data)
headers = next(file_reader)
print(headers)


