import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
excel_file_path = 'bar__data.xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file_path)

# Extracting relevant columns for the bar chart
matches = df[['team1', 'team2', 'score1', 'score2']]

# Creating a bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Number of matches
num_matches = len(matches)

# Bar width
bar_width = 0.35

# Index for each match
index = range(num_matches)

# Plotting the bars for team1
bars_team1 = ax.bar(index, matches['score1'], bar_width, label='Team 1')

# Plotting the bars for team2
bars_team2 = ax.bar([i + bar_width for i in index], matches['score2'], bar_width, label='Team 2')

# Adding labels and title
ax.set_xlabel('Matches')
ax.set_ylabel('Scores')
ax.set_title('Actual Scores of Matches')

team_names = [f"{matches['team1'].iloc[i]} vs {matches['team2'].iloc[i]}" for i in index]
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(team_names, rotation=45, ha='right')  # Adjust rotation for better visibility

#ax.set_xticklabels([f'Match {i + 1}' for i in index])
ax.legend()

# Display the bar chart
plt.show()
