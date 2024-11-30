import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Company Sales Data.csv')

plt.plot(df['month'], df['profit'], linestyle='dotted', marker='o', color='red', linewidth=3, markerfacecolor='black', markeredgecolor='black')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Month-wise Profit')
plt.show()

plt.plot(df['month'], df['facecream'], marker='o', linewidth=3, label='Face Cream')
plt.plot(df['month'], df['facewash'], marker='o', linewidth=3, label='Face Wash')
plt.plot(df['month'], df['toothpaste'], marker='o', linewidth=3, label='Toothpaste')
plt.plot(df['month'], df['bathingsoap'], marker='o', linewidth=3, label='Bathing Soap')
plt.plot(df['month'], df['shampoo'], marker='o', linewidth=3, label='Shampoo')
plt.plot(df['month'], df['moisturizer'], marker='o', linewidth=3, label='Moisturizer')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Month-wise Sales')
plt.legend()
plt.show()

plt.bar(df['month'], df['facecream'], label='Face Cream')
plt.bar(df['month'], df['facewash'], bottom=df['facecream'], label='Face Wash')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream and Face Wash Sales')
plt.legend()
plt.show()
