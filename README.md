# Loops and Lists

- This project was mainly concerned with the manipulation of list and use of control flows and conditional statements.

## Part 1: Printing "Hello" Ten Times

- A for loop was used with a built in method `range` to get the desired number of iterations.
```python
for i in range(10):
    print("Hello")

```

## Part 2: Appending Names to a List

- A for loop was used with a built in method `range` to get the desired number of iterations, along with the `append` method. Empty list created before hand.
```python
names = []
num = 0
list_names_lower = []


for i in range(5):
    name = input("type in a name for index {}".format(num))
    num += 1
    names.append(name)
print(names)

```

## Part 3: New List with Names in Lower Case

- A for loop along with the built in method .lower() was used.
```python
for name in names:
    list_names_lower.append(name.lower())
print(list_names_lower)

```


## Part 4: for name in names: ODD or EVEN??

- names list was looped over to test if length of each value was even or odd dependant on an if condition that will search for a remainder. This was also done for the list itself.

```python
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



```


