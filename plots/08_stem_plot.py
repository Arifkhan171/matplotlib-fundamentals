# Matplotlib Stem Plot - Discrete Data Visualization
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 6, 5, 3]

plt.stem(x, y,
         markerfmt="ro",
         bottom=0,
         basefmt="g-",
         label="Python Data")
plt.title("Stem Plot", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.tight_layout()
plt.show()
