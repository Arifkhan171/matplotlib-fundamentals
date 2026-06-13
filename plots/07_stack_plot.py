# Matplotlib Stack Plot - Stacked Area Chart
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
area1 = [1, 3, 1, 7, 9]
area2 = [2, 4, 1, 3, 5]
area3 = [1, 3, 1, 9, 5]
labels = ["Area 1", "Area 2", "Area 3"]

plt.stackplot(x, area1, area2, area3,
              labels=labels,
              colors=["r", "g", "m"],
              alpha=0.8)
plt.title("Stack Plot - Stacked Area Chart", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()
