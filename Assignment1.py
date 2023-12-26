import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'C:\\Users\\smrit\\OneDrive\\Desktop\\sem6\\CSA\\Obfuscated-MalMem2022.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
# print(df)
print("3rd task")
cols_sel = ['pslist.nppid', 'dlllist.avg_dlls_per_proc', 'ldrmodules.not_in_mem',
                      'psxview.not_in_deskthrd', 'svcscan.kernel_drivers', 'callbacks.ncallbacks','Class']

# Randomly select 15 rows and specific columns
r15 = df.sample(n=15)[cols_sel]
# Display the selected data


print(r15)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("6th task")
print('Scatter plot')
# Extract the last two numerical attributes
last_two_attributes = r15.iloc[:, -2:]
# Scatter plot
plt.scatter(last_two_attributes.iloc[:, 0], last_two_attributes.iloc[:, 1])
plt.title('Scatter Plot for Last Two Numerical Attributes (Randomly Selected 15 Rows)')
plt.xlabel('Last Numerical Attribute')
plt.ylabel('Second to Last Numerical Attribute')
plt.show()

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print('7th task')
print('Histogram')
first_three_attributes = r15.iloc[:, :3]

# Plot histograms for the first three numerical attributes
first_three_attributes.plot.hist(alpha=0.5, bins=20, figsize=(12, 6), layout=(1, 3), sharex=True, sharey=True)
plt.suptitle('Histograms for First Three Numerical Attributes (Randomly Selected 15 Rows)')
plt.show()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print('8th task')
print('Analyze first attribute')
attribute_1 = r15.iloc[:, 0]

# Display descriptive statistics
print("Descriptive Statistics for Attribute 1:")
print(attribute_1.describe())

# Plot a histogram
plt.hist(attribute_1, bins=20, edgecolor='black')
plt.title('Histogram for Attribute 1 (Randomly Selected 15 Rows)')
plt.xlabel('Attribute 1 Values')
plt.ylabel('Frequency')
plt.show()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print('9th task')
print('Box plot')
attribute_1 = r15.iloc[:, 0]

# Create a box plot
plt.figure(figsize=(8, 5))
sns.boxplot(x=attribute_1)
plt.title('Box Plot for Attribute 1 (Randomly Selected 15 Rows)')
plt.xlabel('Attribute 1')
plt.show()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print('10th task')
print('Scatter plots')
# Selecting two numerical attributes for scatter plots
attribute1 = 'callbacks.ncallbacks'
attribute2 = 'dlllist.avg_dlls_per_proc'
class_variable = 'Class'

colors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #Variable colors for different 15 variables

# Create a scatter plot using matplotlib
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.scatter(r15[class_variable], r15[attribute1], c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], cmap='viridis', alpha=0.5)
plt.xlabel(class_variable)
plt.ylabel(attribute1)
plt.title(f'Scatter Plot: {attribute1} vs {class_variable}')

plt.subplot(2, 2, 2)
plt.scatter(r15[class_variable], r15[attribute2], c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], cmap='viridis', alpha=0.5)
plt.xlabel(class_variable)
plt.ylabel(attribute2)
plt.title(f'Scatter Plot: {attribute2} vs {class_variable}')

# Create a scatter plot using seaborn
plt.subplot(2, 2, 3)
sns.scatterplot(x=class_variable, y=attribute1, hue=class_variable, data=r15, palette='viridis', alpha=0.7)
plt.title(f'Scatter Plot(seaborn): {attribute1} vs {class_variable}')

plt.subplot(2, 2, 4)
sns.scatterplot(x=class_variable, y=attribute2, hue=class_variable, data=r15, palette='viridis', alpha=1)
plt.title(f'Scatter Plot(seaborn): {attribute2} vs {class_variable}')

plt.tight_layout()
#plt.show()

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("11th task")
# Assuming r15 is your DataFrame with the selected rows and columns

# Extract the first numerical attribute
attribute_1 = r15.iloc[:, 0]

# Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x=attribute_1)
plt.title('Box Plot for Attribute 1 (Randomly Selected 15 Rows)')
plt.xlabel('Attribute 1 Values')
plt.show()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
