# Loop Notes

# FOR LOOPS

for i in range(10):
    print("Python")

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)
# prints 1-11

for i in range(5, 50, 3):
    print(i)

for i in range(100, 0, -5):
    print(i)

for i in range(1, 21):
    print(1/i)
    print("{}".format(i/1))


# IF STATEMENT
x = 4
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5")
else:
    print("Neither")


# RANDOM NUMBERS
import random   # normally at top of program

print(random.randrange(10)) # random int from 0 to 9
print(random.randrange(10, 20)) # from 10 to 19
print(random.randrange(5, 101, 5)) # counting 5 to 100 by fives

print(random.random()) # float form 0 to 1
print(random.random() * 5 + 5) # float from 5 to 10


# BREAK
# automatically exits from nearest loop
for i in range(100):
    print(i)
    if i > 50:
        break

for i in range(10000):
    n = random.randrange(1000)
    if n == 0:
        print(i)
        break

# FOR ELSE

# if you complete the FOR loop, you do the else
for i in range(1000):
    n = random.randrange(1000)
    if n == 0:
        print(i)
        break
else:
    print("Else statement was triggered")

# CONTINUE

# continue ends the current iteration and skips to the next
for i in range(100):
    n = random.randrange(100)
    if n % 2:
        continue
    print(n) # skipped over for odd numbers




