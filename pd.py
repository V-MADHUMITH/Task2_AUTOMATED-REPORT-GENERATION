import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.figure(figsize=(8,5))
df = pd.read_csv(r"C:\Users\madhu\Documents\task 2\data.csv")
print(df.head())  
sns.histplot(df["Salary"], bins=5, kde=True, color="red")  
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.savefig("salary_histogram.png")
plt.show()
