# Matplotlib Box Plot - Single and Multiple
import matplotlib.pyplot as plt

# --- Single Box Plot ---
data = [32, 50, 10, 30, 59, 44, 30, 55, 58, 53, 54, 31, 53, 47, 39,
        40, 29, 52, 47, 27, 59, 54, 47, 59, 48, 11, 21, 56, 56, 54,
        43, 11, 56, 39, 35, 12, 31, 30, 21, 11, 22, 39, 54, 37, 49,
        26, 57, 39, 39, 25, 150]

plt.boxplot(data, widths=0.3, labels=["Python"],
            patch_artist=True, showmeans=True, sym="r",
            boxprops=dict(color="r"),
            capprops=dict(color="b"),
            whiskerprops=dict(color="y"))
plt.title("Box Plot - Single Dataset", fontsize=15)
plt.tight_layout()
plt.show()

# --- Multiple Box Plot ---
group1 = [32, 50, 10, 30, 59, 44, 30]
group2 = [58, 53, 54, 31, 53, 47, 39]

plt.boxplot([group1, group2], widths=0.3,
            labels=["Python", "C"],
            patch_artist=True, showmeans=True, sym="r",
            boxprops=dict(color="r"),
            capprops=dict(color="b"),
            whiskerprops=dict(color="y"))
plt.title("Box Plot - Multiple Datasets", fontsize=15)
plt.tight_layout()
plt.show()
