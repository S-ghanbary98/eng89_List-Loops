# Task 1
for i in range(10):
    print("Hello")


 # Task 2
names = []
num = 0
list_names_lower = []


for i in range(5):
    name = input("type in a name for index {}".format(num))
    num += 1
    names.append(name)
print(names)

# Task 3
for name in names:
    list_names_lower.append(name.lower())
print(list_names_lower)

#Task 4

for name in names:
    len(name)

    if len(name) % 2 == 0:
        print("{}, has an even number of letters".format(name))
    else:
        print("{}, has an odd number of letters".format(name))

if len(names) % 2 == 0:
    print("{}, has an even number of letters".format(names))
else:
    print("{}, has an odd number of letters".format(names))


