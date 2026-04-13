import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [120, 180, 90, 140, 200] # units per day
prices = [12, 11, 13, 10, 12] # average price per day
samples = [3,7,12,15,18,20,19,14,9,5,2,5,8,11,13,1,4] # histogram data

# LINE PLOT

plt.plot(days, sales, marker = "o")
plt.title("Daily sales, line plot")
plt.xlabel("Day")
plt.ylabel("Units")
plt.grid(True, alpha=0.3)
plt.show()

# BAR CHART

plt.bar(days, sales)
plt.title("Daily sales, bar chart")
plt.xlabel("Day")
plt.ylabel("Units")
plt.grid(True, alpha=0.3)
plt.show()

# HISTOGRAM

plt.hist(samples, bins=6)
plt.title("Samples distribution, histogram")
plt.xlabel("Value")
plt.ylabel("Count")
plt.show()

# SCATTER

plt.scatter(prices, sales)
plt.title("Price vs sales, scatter")
plt.xlabel("Price")
plt.ylabel("Units")
plt.grid(True, alpha=0.3)
plt.show()
