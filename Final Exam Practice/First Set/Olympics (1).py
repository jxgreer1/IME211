# You are interested in analyzing performance from swimmers who competed in the 2024 Summer Olympics.
# You manage to find 2 datasets: swimming_medals and swimming_performance

swimming_medals = {
    "Michael Phelps": "gold",
    "Katie Ledecky": "gold",
    "Caeleb Dressel": "bronze",
    "Ryan Lochte": "silver",
    "Missy Franklin": "gold",
    "Ian Thorpe": "no medal",
    "Katinka Hosszu": "bronze",
    "Nathan Adrian": "silver",
    "Simone Manuel": "no medal",
    "Adam Peaty": "gold"
}

swimming_performance = {
    "Michael Phelps": {"distance_meters": 200, "time_seconds": 115.32},
    "Katie Ledecky": {"distance_meters": 400, "time_seconds": 230.45},
    "Caeleb Dressel": {"distance_meters": 100, "time_seconds": 47.85},
    "Ryan Lochte": {"distance_meters": 200, "time_seconds": 117.20},
    "Missy Franklin": {"distance_meters": 200, "time_seconds": 112.98},
    "Ian Thorpe": {"distance_meters": 400, "time_seconds": 240.50},
    "Katinka Hosszu": {"distance_meters": 200, "time_seconds": 121.34},
    "Nathan Adrian": {"distance_meters": 100, "time_seconds": 48.10},
    "Simone Manuel": {"distance_meters": 100, "time_seconds": 52.70},
    "Adam Peaty": {"distance_meters": 100, "time_seconds": 57.13}
}

# First, create a user input that asks the user of the script to select a medal category.
# The options are: no medal, bronze, silver, or gold.
# Ensure only these options are accepted and the user is re-prompted otherwise.
# Store this as 'medal_selection'
while True:
    medal_selection= input("Please Select Metal type. no medal, brone, silver, or gold:").lower()
    if medal_selection in ["no medal","gold","silver","bronze"]:
        break
    else:
        print("Not a Selection")



# Next, create a list of names (store as 'swimmers') from the swimming_medals dataset in the selected medal category
#swimmers = swimming_performance.keys()
swimmers = [name for name, medal in swimming_medals.items() if medal == medal_selection]

print(swimmers)
# Next, create a new dictionary called 'swimming speed'.
# The dictionary should have the swimmers in the selected medal category as keys
# and their speed in m/s (distance / time) as the value.
i=0
#for swimming_speed in swimming_medals:
swimming_speed = {}
for swimmer in swimmers:
    distance=swimming_performance[swimmer]["distance_meters"]
    time = swimming_performance[swimmer]["time_seconds"]
    speed= distance/time
    swimming_speed[swimmer] = speed
# Finally, produce a printout with the following structure:
# Speeds for gold (m/s):
# Michael Phelps - 1.73
# Katie Ledecky - 1.73
#
# Average gold medal speed: 1.75 m/s
# Step 4: Print out the swimmers and their speeds
print(f"\nSpeeds for {medal_selection} medal (m/s):")
for swimmer, speed in swimming_speed.items():
    print(f"{swimmer} - {speed:.2f}")

# Step 5: Calculate and print the average speed
if swimming_speed:
    avg_speed = sum(swimming_speed.values()) / len(swimming_speed)
    print(f"\nAverage {medal_selection} medal speed: {avg_speed:.2f} m/s")
else:
    print(f"\nNo swimmers with a {medal_selection} medal.")