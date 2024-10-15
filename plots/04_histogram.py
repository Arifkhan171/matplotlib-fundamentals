# Matplotlib Histogram - Distribution of Data
import matplotlib.pyplot as plt
import numpy as np

data = [32, 50, 10, 30, 59, 44, 30, 55, 58, 53, 54, 31, 53, 47, 39,
        40, 29, 52, 47, 27, 59, 54, 47, 59, 48, 11, 21, 56, 56, 54,
        43, 11, 56, 39, 35, 12, 31, 30, 21, 11, 22, 39, 54, 37, 49,
        26, 57, 39, 39, 25]

# --- Basic Histogram ---
plt.hist(data)
plt.title("Histogram - Basic", fontsize=15)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --- Styled Histogram with Bins ---
bins = [10, 20, 30, 40, 50, 60]

plt.hist(data, color="b", bins=bins, edgecolor="r",
         orientation="vertical", rwidth=0.8, label="Python Data")
plt.axvline(45, color="y", label="Threshold (45)")
plt.title("Histogram - Custom Bins and Styling", fontsize=15)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
