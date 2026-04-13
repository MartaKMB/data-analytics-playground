import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "sales": [120, 180, 90, 140, 200],
    "price": [12, 11, 13, 10, 12]
})

df["revenue"] = df["sales"] * df["price"]
print(df)

# plt.plot(df["day"], df["sales"], marker="o")
# plt.show()

df.plot(x="day", y="revenue", kind="line", marker="o", title="Daily sales (line plot: Pandas)")
plt.show()

df.plot(x="day", y="revenue", kind="bar", title="Daily sales (bar char: Pandas)")
plt.show()

df["price"].plot(kind="hist", bins=5, title="Price distribution (histogram: Pandas)")
plt.show()

df.plot(x="price", y="sales", kind="scatter", title="Price distribution (scatter: Pandas)")
plt.show()

ax = df.plot(x="day", y=["sales", "price"], marker="o", style=["-o", "--s"], title="Sales and prices by day")
ax.set_xlabel("Day")
ax.set_ylabel("Value")
ax.grid(True, alpha=0.3)
plt.show()
