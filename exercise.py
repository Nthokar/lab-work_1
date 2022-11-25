import numpy as np
from matplotlib import pyplot as plt

era = list(range(8))
total_error = {
    "OR":[2, 2, 1, 0],
    "AND":[2, 2, 3, 2, 1, 0],
    "NAND":[2, 2, 3, 2, 1, 0]
    }

ig, ax = plt.subplots()

ax.bar(range(len(total_error["NAND"])), total_error["NAND"])

plt.show()

print(era)
