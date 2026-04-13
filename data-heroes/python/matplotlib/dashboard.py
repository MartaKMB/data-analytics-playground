import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "product": ["Coffee", "Tea", "Water", "Juice"],
    "price": [12, 8, 3, 5],
    "units": [350, 220, 410, 180],
})

df["revenue"] = df["units"] * df["price"]
print(df)

fig, axs = plt.subplots(2, 2, figsize=[10,6])

axs[0][0].plot(df["product"], df["units"], marker="o", label="Units")

axs[0,0].set_title("Line - units per product")
axs[0,0].set_xlabel("Product")
axs[0,0].set_ylabel("Units")
axs[0,0].grid(True, alpha=0.3)
axs[0,0].legend()

axs[0,1].bar(df["product"], df["revenue"], color="orange")
axs[0,1].set_title("Bar - revenue per product")
axs[0,1].set_xlabel("Product")
axs[0,1].set_ylabel("Units")
axs[0,1].grid(True, alpha=0.3)

sns.set_theme()
print(df)

corr = df[["units", "price", "revenue"]].corr()
print(corr)

sns.heatmap(corr, annot=True, cmap="Blues", ax = axs[1,0])
axs[1,0].set_title("Seaborn - correlation heatmap")

sns.boxplot(data=df, y="units", ax=axs[1,1])
axs[1,1].set_title("Seaborn - units distribution")

fig.suptitle("Matplotlib OO + Seaborn dashboard", fontsize=14)

plt.tight_layout()
plt.show()
