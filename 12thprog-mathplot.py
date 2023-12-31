import matplotlib.pyplot as plt

def plot_monthly_data(months, temperatures, rainfall):
    # Create the line plot for temperature
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(months, temperatures, marker='o', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Monthly Temperature Data')
    plt.grid(True)

    # Create the scatter plot for rainfall
    plt.subplot(1, 2, 2)
    plt.scatter(months, rainfall)
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.title('Monthly Rainfall Data')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Sample data for monthly temperature and rainfall (replace this with your actual data)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    temperatures = [25, 27, 28, 30, 32, 35, 36, 34, 33, 30, 28, 26]
    rainfall = [50, 45, 70, 80, 90, 110, 120, 100, 95, 85, 60, 55]

    plot_monthly_data(months, temperatures, rainfall)
