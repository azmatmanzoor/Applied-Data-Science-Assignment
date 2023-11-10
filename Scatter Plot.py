import pandas as pd
import matplotlib.pyplot as plt

# Assuming the data is saved in a CSV file named 'pollster_data.csv'
df = pd.read_excel('scatter__data.xlsx')

# Extract relevant data
mean_reverted_bias = df['Mean-Reverted Bias']
simple_average_error = df['Simple Average Error']
pollster_names = df['Pollster']

# Plotting the scatter chart
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot
ax.scatter(mean_reverted_bias, simple_average_error, color='blue', alpha=0.7)

# Adding labels to each point
for i, txt in enumerate(pollster_names):
    ax.annotate(txt, (mean_reverted_bias[i], simple_average_error[i]), fontsize=8, ha='right')

# Corrected labels
ax.set_xlabel('Mean-Reverted Bias')
ax.set_ylabel('Simple Average Error')
ax.set_title('Scatter Plot of Mean-Reverted Bias vs. Simple Average Error for Pollsters')

# Display the plot
plt.show()
