import numpy as np

# Load data from CSV files
points = np.loadtxt('points.csv')  # points scored per game
minutes = np.loadtxt('minutes.csv')  #minutes he played per game

# points per minute for each game
points_per_minute = points / minutes

# average points per minute
average_points_per_minute = np.mean(points_per_minute)

# Print final points per minutes
print("Lebrons point per average=", average_points_per_minute)

