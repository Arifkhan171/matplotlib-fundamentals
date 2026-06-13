# Matplotlib Bar Chart - Single and Grouped
import matplotlib.pyplot as plt
import numpy as np

# --- Single Bar Chart ---
students = ["Arif", "Ajab", "Gul", "Sattar"]
marks = [85, 60, 70, 90]
colors = ["r", "b", "g", "y"]

plt.xlabel("Students", fontsize=15)
plt.ylabel("Marks", fontsize=15)
plt.title("Student Marks - Single Bar", fontsize=20)
plt.bar(students, marks, color=colors, width=0.3,
        align="edge", edgecolor="r", linewidth=5, label="Math Paper")
plt.legend()
plt.tight_layout()
plt.show()

# --- Grouped Bar Chart ---
students = ["Arif", "Ajab", "Gul", "Sattar"]
math_marks = [69, 55, 43, 24]
english_marks = [80, 66, 70, 66]
width = 0.5

positions = np.arange(len(students))
positions2 = [j + width for j in positions]

plt.xlabel("Students", fontsize=15)
plt.ylabel("Marks", fontsize=15)
plt.title("Student Marks - Grouped Bar", fontsize=20)
plt.bar(positions, math_marks, color="y", width=0.5,
        label="Math Paper", edgecolor="b", linewidth=2)
plt.bar(positions2, english_marks, color="r", width=0.2,
        label="English Paper", edgecolor="b", linewidth=2,
        linestyle=":", alpha=0.3)
plt.xticks(positions + width / 2, students)
plt.legend()
plt.tight_layout()
plt.show()
