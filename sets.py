# sets are unordered and cannot have duplicates
# sets are not accessed by keys
# members of sets are immutable objects


# there are two ways to create sets
# first way
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

print("="*40)

for animal in farm_animals:
    print(animal)

print("="*40)

# second way to create functions i.e. by passing a list to the built in function set()
# this method is used when creating a set from other iterables.
wild_animals = set(["lion", "tiger", "panter", "cheetah", "hare"])
print(wild_animals)

print("="*40)

for animal in wild_animals:
    print(animal)

# adding items to a set
farm_animals.add("chicken")
wild_animals.add("horse")

# sets are unordered by default (look at the output)
print(farm_animals)
print(wild_animals)

# this will create an empty dictionary
empty_set = {}

# this will rather create an empty set
empty_set2 = set()

print("="*40)

print(type(empty_set))  # this will print an empty dictionary
print(type(empty_set2))  # this will print an empty set

# empty_set.add("a") = this will raise an error
empty_set[1] = "red"
empty_set[2] = "blue"
empty_set2.add("a")

print(empty_set)
