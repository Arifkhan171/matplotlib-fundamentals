# Matplotlib Scatter Plot - Basic, Styled and Multi-Series
import matplotlib.pyplot as plt

# --- Basic Scatter Plot ---
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 6, 9]

plt.scatter(x, y)
plt.title("Scatter Plot - Basic", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.tight_layout()
plt.show()

# --- Styled Scatter with Colormap ---
days = [1, 2, 3, 4, 5]
hours = [2, 5, 3, 6, 9]
sizes = [200, 200, 200, 200, 200]
colors = [20, 22, 24, 25, 26]

sc = plt.scatter(days, hours, s=sizes, c=colors,
                 marker="*", cmap="BrBG")
cbar = plt.colorbar(sc)
cbar.set_label("Color Scale")
plt.title("Scatter Plot - With Colormap", fontsize=15)
plt.xlabel("Days")
plt.ylabel("Hours")
plt.tight_layout()
plt.show()

# --- Multi-Series Scatter Plot ---
days = [1, 2, 3, 4, 5]
series1 = [2, 5, 3, 6, 9]
series2 = [3, 5, 4, 2, 1]

plt.scatter(days, series1, s=200, color="r",
            marker="*", label="Series 1")
plt.scatter(days, series2, s=200, color="b",
            marker="*", label="Series 2")
plt.title("Scatter Plot - Multi Series", fontsize=15)
plt.xlabel("Days")
plt.ylabel("Values")
plt.legend()
plt.tight_layout()
plt.show()
