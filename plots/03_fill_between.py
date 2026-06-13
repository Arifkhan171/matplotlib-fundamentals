# Matplotlib Fill Between - Highlight Areas Under Line
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y, color="r", label="Line")
plt.title("Fill Between Plot", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Fill area where x is between 2 and 4
plt.fill_between(x, y, color="g", alpha=0.4,
                 where=(x >= 2) & (x <= 4),
                 label="Filled Area (x=2 to x=4)")
plt.legend()
plt.tight_layout()
plt.show()
