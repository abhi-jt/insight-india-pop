import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("indian_states_population.csv")

# Show top 5 rows
print("First 5 rows of the dataset:\n", data.head())

# Sort by population and take top 10
top_states = data.sort_values(by="Population", ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.bar(top_states['State'], top_states['Population'], color='skyblue')
plt.xticks(rotation=45)
plt.title("Top 10 Most Populous States in India")
plt.xlabel("State")
plt.ylabel("Population")
plt.tight_layout()

# Save plot
plt.savefig("top_10_states_population.png")
print("Plot saved as 'top_10_states_population.png'")
