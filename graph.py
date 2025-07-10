import matplotlib.pyplot as plt

# Data points
magnetic_field = [500, 700, 900, 1100, 1300]  # in mA
hall_voltage = [72.3, 75.1, 78.1, 80.1, 82.5]  # in mV

# Creating the plot
plt.figure(figsize=(8, 6))
plt.plot(magnetic_field, hall_voltage, marker='o', linestyle='-', color='b', label='Current vs Hall Voltage')

# Adding titles and labels
plt.title('magnetic_field vs Hall Voltage')
plt.xlabel('magnetic_field (hz)')
plt.ylabel('Hall Voltage (mV)')
plt.legend()

# Setting the grid
plt.grid(True)

# Display the plot
plt.show()
