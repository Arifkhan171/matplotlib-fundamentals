# Matplotlib Pie Chart - Basic and Styled
import matplotlib.pyplot as plt

# --- Basic Pie Chart ---
sizes = [10, 30, 80, 50]
labels = ["C", "C++", "Java", "Python"]

plt.pie(sizes, labels=labels)
plt.title("Programming Languages - Basic Pie")
plt.tight_layout()
plt.show()

# --- Styled Pie Chart with Explode ---
sizes = [10, 30, 80, 50]
labels = ["C", "C++", "Java", "Python"]
explode = [0.4, 0.0, 0.0, 0.0]   # explode first slice
colors = ["g", "r", "y", "b"]

plt.pie(sizes, labels=labels,
        explode=explode,
        colors=colors,
        autopct="%0.2f%%",
        shadow=True,
        radius=1.1,
        labeldistance=1.1,
        textprops={"fontsize": 15},
        wedgeprops={"linewidth": 4, "edgecolor": "m"})

plt.title("Programming Languages - Styled Pie", fontsize=15)
plt.legend(loc=2)
plt.tight_layout()
plt.show()
