# Tuples - immutable lists that can't be changed

city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA')]
#length of three objects

first_city_state = city_state[0]
print(first_city_state) #('Seattle', 'WA')

#tuple unpacking
print(first_city_state[0])
# print(first_city_state[1] - out of bounds error

city, state = first_city_state
print(city) #Seattle

animals = ('lion', 'puma', 'tiger')
lion, puma, tiger = animals

print(tiger) # prints third value NOT just tiger

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km

distances = get_distance()
print(distances) # returns tuple (1000, 1600.0)
print(distances[0]) # 1000

miles, km = get_distance()
print(km) #1600.0

#useful for returning multiple values from a function
def get_random_cat_and_pattern():
    return 'tiger', 'stripes' #return a tuple

# unpack tuple to get both values in seperate variables
cat, pattern = get_random_cat_and_pattern()

#alternative more work method
data = get_random_cat_and_pattern()
print(data[0]) # tiger

#out of bounds error - try and except
try:
    print(data[10])
except:
    print('oops, that does not exist')

