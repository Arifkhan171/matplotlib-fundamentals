# Matplotlib Step Plot - Discrete Step Function
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]

plt.step(x, y, color="r", marker="o",
         ms=10, mfc="g", label="Python")
plt.title("Step Plot", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
