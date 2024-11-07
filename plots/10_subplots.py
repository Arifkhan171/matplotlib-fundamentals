# Matplotlib Subplots - Multiple Charts in One Figure
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]
x2 = [10, 20, 30, 40, 50]
labels = ["C", "C++", "Java", "Python"]

# --- 4 subplots in one figure ---
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Multiple Plot Types in One Figure", fontsize=16)

# Line plot
axes[0, 0].plot(x, y, color="b")
axes[0, 0].set_title("Line Plot")
axes[0, 0].set_xlabel("X")
axes[0, 0].set_ylabel("Y")

# Pie chart
axes[0, 1].pie([1, 1, 1, 1], labels=labels)
axes[0, 1].set_title("Pie Chart")

# Pie chart with custom sizes
axes[1, 0].pie(x2, labels=labels, autopct="%1.1f%%")
axes[1, 0].set_title("Pie Chart with Percentages")

# Bar chart
axes[1, 1].bar(labels, x2, color=["r", "g", "b", "y"])
axes[1, 1].set_title("Bar Chart")
axes[1, 1].set_xlabel("Language")
axes[1, 1].set_ylabel("Score")

plt.tight_layout()
plt.show()
