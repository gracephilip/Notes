# Searching

file = open('data/villians.txt', 'r')

for line in file:
    # strip method removes spaces and \t and \n from a string
    print(line.strip())

file.close()

file = open('data/villians.txt', 'r')

for line in file:
    print("Hello", line.strip())

file.close()

'''
# We can also write to a file.
file = open('data/villians.txt', 'w') # w for write instead of r for read
# you can only read, write, or append a file
# this overwrites the entire file
file.write("Lee The Merciless")

file.close()
'''
'''
# appending to a file

file = open('data/villians.txt', 'a') # append to a file

file.write("\nLee The Merciless")
# adds to it every time you run it

file.close()
'''
# Read a file into an array (list)

villians = []
file = open('data/villians.txt', 'r')

for name in file:
    villians.append(name.strip())

file.close()
print(villians)


# Linear Search
# now that it is in a list, we don't need to open the file again because we have the info in a list that we can work with
# find 'The Infamous Devourer'
key = "The Infamous Devourer"
i = 0
while i < len(villians) and villians[i] != key:
    i += 1
if i < len(villians):
    print(key, "is at position", i)
else:
    print(key, "is not found")

# Binary Search

key = "Morgiana the Shrew"
lower_bound = 0
upper_bound = len(villians)
found = False

while not found and lower_bound <= upper_bound:
    middle_pos = (upper_bound - lower_bound) // 2
    if villians[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villians[middle_pos] > key:
        upper_bound = middle_pos -1
    else:
        found = True

if found:
    print("Found", key, "at position", middle_pos)
else:
    print(key, "was not found")


