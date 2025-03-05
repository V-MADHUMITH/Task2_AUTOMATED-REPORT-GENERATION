#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#file_path=r"C:\users\madhu\Documents\task 2\data.csv"
#df=pd.read_csv(file_path)
#print("Data Preview:\n",df.head())
#summary=df.describe()
#print("\n Summary Statistics:\n",summary)
#dept_salary=df.groupby("Department")["Salary"].mean()
#print("\n Average Salary by Department:\n",dept_salary)
#plt.figure(figsize=(8,5))
#sns.histplot()
#sns.histplot(df["Salary"], bins=5, kde=True, color="blue")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\madhu\Documents\task 2\data.csv")

# Check if df is loaded
print(df.head())  # ✅ This will confirm if the DataFrame is loaded properly

sns.histplot(df["Salary"], bins=5, kde=True, color="red")  # ✅ Correct function
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

# Save the plot
plt.savefig("salary_histogram.png")
plt.show()
