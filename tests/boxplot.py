import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Display first few rows
print(tips.head())

# Create a boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x="day", y="total_bill", data=tips, palette="pastel")

plt.title("Distribution of Total Bill by Day", fontsize=14)
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()
