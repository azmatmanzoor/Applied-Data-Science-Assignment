import matplotlib.pyplot as plt
import pandas as pd

# Load data from an Excel file
# Replace 'your_data.xlsx' with the path to your Excel file
df = pd.read_excel('line__data.xlsx')

# Convert the "date" column to a datetime format
df['date'] = pd.to_datetime(df['date'])

# Create a line plot for home_team_score and away_team_score over time
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['home_team_score'], label='Home Team Score', marker='o')
plt.plot(df['date'], df['away_team_score'], label='Away Team Score', marker='o')
plt.xlabel('Date')
plt.ylabel('Score')
plt.title('Home Team and Away Team Scores Over Time')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
