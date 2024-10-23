import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset
tips = sns.load_dataset('tips')


# 1. Scatterplot for Totalbill/ Tip amount
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', color='blue')
plt.title('total bill to tip amount')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip Amount ($)')
plt.grid(True)
plt.show()
#Yes there seems to be a trend between total bill and tip


#hisogram of the most common total bill
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], bins=20, color='green')
plt.title('Distribution of Total Bills')
plt.xlabel('Total Bill ($)')
plt.ylabel('Common')
plt.grid(True)
plt.show()
#most common bill total is around 15 dollars

#plt.figure(figsize=(8, 6))
sns.barplot(tips, x="day", y="tip", color='pink')
plt.title('Greatest Tip day')
plt.xlabel('Tip($)')
plt.ylabel('Amount per day')
plt.grid(True)
plt.show()
#sunday

# Calculate the average tips per day using pandas
average_tips_per_day = tips.groupby('day')['tip'].mean().reset_index()

# Plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.bar(average_tips_per_day['day'], average_tips_per_day['tip'], color='yellow')
plt.title('Greatest Tip Day (Average Tips)')
plt.xlabel('Day')
plt.ylabel('Average Tip ($)')
plt.grid(True)