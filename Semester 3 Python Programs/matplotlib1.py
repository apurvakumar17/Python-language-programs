import matplotlib.pyplot as plt

data = [5,7,3,9,4,2]
labels = ["home", "pen", "laptop","mouse", "tv", "wire"]

plt.pie(data, labels = labels)
plt.title("Home appliances")
plt.show() #pie chart

plt.bar(labels, data)
plt.show()  #bar graph