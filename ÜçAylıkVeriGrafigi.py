import pandas as pd
import matplotlib.pyplot as plt

Q1 = [20, 35, 30, 35]
Q2 = [25, 32, 34, 28]
Q3 = [30, 34, 37, 30]
Months = ['Jan', 'Feb', 'Mar', 'Apr']

df = pd.DataFrame({
    'Months': Months,
    'Q1': Q1,
    'Q2': Q2,
    'Q3': Q3
})

plt.bar(df['Months'], df['Q1'], color='red', label='Q1')
plt.bar(df['Months'], df['Q2'], bottom=df['Q1'], color='blue', label='Q2')
plt.bar(df['Months'], df['Q3'], bottom=df['Q1'] + df['Q2'], color='green', label='Q3')

plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Quarterly Data')


plt.show()