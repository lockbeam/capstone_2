#The classes a student is registered for
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only the ITEC classes with list comp
# like a loop nested inside of a list creation/list initialization statement
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ]
print(only_itec)

# record temperature every day. Record -1 if not possible to take measurement
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# in the above example a recorder recorded -1 when recording failed so
# we want to make a new list of only numbers that represent a valid temp measurement
only_real_measurements = [ temp for temp in high_temps if temp != -1]
print(only_real_measurements)

temp_celsius = [ round((temp_f - 32) * 5 / 9, 2 ) for temp_f in only_real_measurements]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is {average:.2f}C')

# length of strings list comprehensions
strings = ['pizza', 'Beyonce', 'cat']
lengths = []

#loop method
for string in strings:
    length = len(string)
    lengths.append(length)

print(lengths)

#list comp method
lengths_comp = [len(string) for string in strings]
print(lengths_comp)

#list of numbers where each number is double the original
numbers = [1, 40, 333]
doubled_numbers = [n *2 for n in numbers]
print(doubled_numbers) #[2, 80, 666]

#convert strings to int
string_numbers = ['42', '10', '6', '789']
int_numbers = [int(string) for string in string_numbers]
print(int_numbers) # [42, 100, 6, 256]

#plus one
original_numbers = [5, 6, 10000]
numbers_plus_one = [n +1 for n in original_numbers]
print(numbers_plus_one)

# add a condition to filter a list
# remember python doesn't have contains()
# use the in operator
more_numbers = [1, -10, 40, -6, -500, 350]
positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers) #[1, 40, 350]

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas)

even_more_numbers = [0, 3, 4, 0, 22, 1]
get_them_zeros_outta_here = [n for n in even_more_numbers if n != 0]
print(get_them_zeros_outta_here)

classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
only_itec_classes = [itecs for itecs in classes if 'ITEC' in itecs]
print(only_itec_classes)

numbers_to_double = [0, 10, 4, 0, 32]
doubled_exlcuding_zeros = [n*2 for n in numbers_to_double if n != 0]
print(doubled_exlcuding_zeros)

