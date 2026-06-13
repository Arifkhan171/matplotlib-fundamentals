# Matplotlib Text and Annotations - Labels on Charts
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]

plt.plot(x, y, color="b", marker="o", label="Data")
plt.title("Text and Annotations", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Add text box at specific position
plt.text(4, 5, "Python",
         style="italic",
         fontsize=12,
         bbox={"facecolor": "red", "alpha": 0.5})

# Add annotation with arrow
plt.annotate("Start Point",
             xy=(2, 3),
             xytext=(3, 2),
             fontsize=11,
             arrowprops=dict(facecolor="black",
                             shrink=0.05,
                             width=2))
plt.legend()
plt.tight_layout()
plt.show()
