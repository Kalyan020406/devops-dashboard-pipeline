import pandas as pd
import matplotlib.pyplot as plt

# Load pipeline metrics
data = pd.read_csv('pipeline-metrics.csv')

# Count success vs failure
status_counts = data['Status'].value_counts()

# Plot bar chart
plt.figure(figsize=(6, 4))
status_counts.plot(kind='bar', color=['green', 'red'])
plt.title('Pipeline Build Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()

# Save the dashboard
plt.savefig('sample-dashboard.png')
print("Dashboard saved as 'sample-dashboard.png'")
