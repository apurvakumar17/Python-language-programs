import matplotlib.pyplot as plt

activities = ['Study', 'Sleep', 'Exercise', 'Entertainment', 'Others']
time_spent = [5, 8, 1, 3, 2]

plt.pie(time_spent, labels=activities, autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Daily Time Distribution")

plt.show()
