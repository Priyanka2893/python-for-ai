# name = "Priyanka"
# name

# age = 32
# age

power = 20**2
power

first_name = "Priyanka"
last_name = "Shaktawat"
full_name = first_name + " " + last_name
full_name
len(full_name)

is_true = True
is_false = False

# is_18 = age == 18
# is_18

age = 19
has_license = True
drunk = True

can_drive = age >= 18 and has_license and not drunk
can_drive

score = 10
score = score + 5
score

name = "Priyanka"

print(name.upper())
print(name.lower())
print(name[0])  # First character
print(name[1:4])  # Substring from index 1 to 3
print(name[-1])  # Last character
print(name + " is learning Python.")  # String concatenation


string = f"Hello, {name}! Welcome to Python programming."
string

print(string.split("Hello"))
print(string.replace("Python", "programming"))
print(string.find("Python"))
print(string.count("o"))

temperature = 18
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a nice day.")
else:
    print("It's a cold day.")


for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)


# Lists
# Ordered, mutable, allows duplicate elements

my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # First element
print(my_list[1:4])  # Sublist from index 1 to 3
my_list.append(6)  # Add an element to the end of the list
print(my_list)
my_list.remove(3)  # Remove the element with value 3
print(my_list)
my_list[0] = 10  # Change the first element to 10
print(my_list)
my_list.insert(2, 15)  # Insert 15 at index 2
print(my_list)
my_list.pop()  # Remove the last element
print(my_list)
my_list.sort()  # Sort the list in ascending order
print(my_list)
my_list.reverse()  # Reverse the order of the list
print(my_list)
my_list.clear()  # Remove all elements from the list
print(my_list)

# Dictionaries
# Unordered, mutable, key-value pairs

my_dict = {"name": "Priyanka", "age": 32, "city": "New York"}
print(my_dict["name"])  # Access value by key
my_dict["age"] = 33  # Update value for key "age"
print(my_dict)
my_dict["country"] = "USA"  # Add a new key-value pair
print(my_dict)
del my_dict["city"]  # Remove key-value pair with key "city"
print(my_dict)
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs


# Tuples
# Ordered, immutable, allows duplicate elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # First element
print(my_tuple[1:4])  # Subtuple from index 1 to 3
# my_tuple[0] = 10  # This will raise an error because tuples are

# Sets
# Unordered, mutable, no duplicate elements
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)  # Add an element to the set
print(my_set)
my_set.remove(3)  # Remove an element from the set
print(my_set)
my_set.add(2)  # Adding a duplicate element does nothing
print(my_set)

fruits = set(["apple", "banana", "orange", "apple"])
fruits


# functions
def greet(name):
    return f"Hello, {name}"


greet("Priyanka")


def person_info(name="Guddu", age=30):
    return f"{name} is {age} years old."


person_info("Priyanka", 32)

# always use keyword arguments when calling a function with default values
# to avoid confusion and ensure that the correct values are assigned
# to the correct parameters.

person_info(name="Priyanka", age=32)  # Using keyword arguments
person_info(age=32, name="Priyanka")  # Order does not matter with keyword arguments
person_info()  # Using default values

discount = 20  # Global variable


def calculate_price(price, discount=0):
    discount = 10  # Local variable that shadows the global variable 'discount'
    final_price = price - (price * discount / 100)
    print(discount)
    return final_price


result = calculate_price(100, discount)  # Using the global variable 'discount'
discount  # points to the global variable, not the local variable inside the function


def simple_function():
    numbers = [1, 2, 3, 4, 5]  # Local variable
    first_number = numbers[0]  # Local variable
    last_number = numbers[-1]  # Local variable
    return first_number, last_number


first, last = simple_function()
print(f"First number: {first}, Last number: {last}")

# External Tools
