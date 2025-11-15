import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [88, 92, 76, 81, 95]

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks Bar Graph")

plt.show()