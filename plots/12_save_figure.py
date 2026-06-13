# Matplotlib Save Figure - Export Charts as Image Files
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]

# IMPORTANT: always plot BEFORE saving
plt.plot(x, y, color="b", marker="o", label="Data")
plt.title("Save Figure Example", fontsize=15)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.tight_layout()

# Save with high resolution
plt.savefig("saved_chart.jpg",
            dpi=200,
            bbox_inches="tight")

print("Chart saved as saved_chart.jpg")
plt.show()
