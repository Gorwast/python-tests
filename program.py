import functions

# variables
hello_world = "Hola mundo python"

float_number = 234.567
int_number = 12

is_true = False

print(hello_world)

# taking input from the user
user_name = input("Introduce tu nombre: ")

print("Hola " + user_name)

# lists
names = ["Luis", "Enrique", "Lopez", "Chaidez"]
print(names[2])

# accessing the last element of the list
print(names[-1])

# changing the values of the list individually
names[2] = "Chavez"
names.insert(3, "Hola")
print(names)

# Append to the end of the list
names.append("Python")

# Tuples ()
coordinates = (4, 5)
print(coordinates[0])
# You can take the values from a tuple but you cannot change the value
coordinate_list = [(4, 5), (12, 54), (23, 14)]

functions.division_by_1()
