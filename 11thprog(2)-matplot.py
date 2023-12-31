import matplotlib.pyplot as plt

# Sample data for sales over 6 months
months = [1, 2, 3, 4, 5, 6]
sales = [1000, 1200, 900, 1500, 1800, 1300]

# Create the scatter plot
plt.scatter(months, sales)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales of Product X Over Time')
plt.grid(True)
plt.show()
