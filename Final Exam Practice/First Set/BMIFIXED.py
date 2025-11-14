# ----------------------------------------------------
# Final Exam Practice
# ----------------------------------------------------
from os.path import split

from BMI import bmi_database

# You are working with an ergonomics research team.
# They collected height and weight data from their human subjects participants.
# Unfortunately, this research team is not very good at data management.
# They are currently storing the data with two separate variables (‘names’ and ‘data’).
# ‘names’ is a list of lists, each containing the first and last name of a participant.

names = [
    ['Sally', 'Sue'], ['John', 'Doe'], ['Jane', 'Doe'],
    ['Mike', 'Smith'], ['Anna', 'Johnson'], ['Robert', 'Brown'],
    ['Emily', 'Davis'], ['David', 'Wilson'], ['Sarah', 'Taylor'],
    ['James', 'Anderson'], ['Linda', 'Thomas'], ['Paul', 'Jackson'],
    ['Karen', 'White'], ['Mark', 'Harris'], ['Susan', 'Martin'],
    ['Kevin', 'Thompson'], ['Laura', 'Garcia'], ['Brian', 'Martinez'],
    ['Megan', 'Robinson'], ['Chris', 'Clark']
]

# ‘data’ is a list of lists, each containing data corresponding to the height (in meters) and weight (in kg)
# of the participant (with matching index value to ‘names’).

data = [
    [1.8, 75], [2, 95], [1.5, 65],
    [1.7, 80], [1.6, 68], [1.9, 88],
    [1.5, 55], [1.8, 77], [1.6, 72],
    [1.9, 85], [1.7, 70], [1.8, 79],
    [1.6, 60], [1.9, 90], [1.7, 74],
    [1.8, 76], [1.5, 58], [1.7, 73],
    [1.6, 62], [1.9, 89]
]
bmi_values = []
# TODO 1: Recursively, calculate the BMI for each participant and store in a list called 'bmi_values' (BMI = kg/m2)
for pair in data:
    height = pair[0]
    weight = pair[1]
    bmi = weight / (height ** 2)  # Calculate BMI
    bmi_values.append(bmi)
# TODO 2: Combine ‘names’ and ‘bmi_values’ into a single dictionary called 'bmi_database'
#  with the full name (as a string) as the key and the BMI as the value.
i = 0  # Index for tracking entries
for name in names:
    first = name[0]
    last = name[1]
    fullname = first + " " + last  # Concatenate first and last names to get the full name
    bmi = bmi_values[i]  # Get the corresponding BMI value
    bmi_database[fullname] = bmi  # Add to the dictionary
    i += 1
# TODO 3: Allow your script user to input a BMI value that will be used to split the BMI dictionary (in TODO 4).
#  Use a while loop to repeatedly prompt the user until they provide a non-zero positive value.
while True:
    user_input=float(input("BMI:"))
    break

# TODO 4: Neatly print the a message for each participant stating their name, BMI, and
#  whether they are above or below the indicated value (gathered in the previous step from the user).
for name, bmi in bmi.database.items():
    if bmi >user_input:
        comparison = "above"
    elif bmi < user_input:
        comparison = "below"
    else:
        comparison = "equal"
