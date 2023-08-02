import numpy as np

sales_data = np.array([
    [100, 150, 120],
    [80, 90, 110],
    [200, 180, 210]
])

average_price = np.mean(sales_data)

print("Average price of all products sold in the past month:", average_price)
