import itertools


items = [1, 2, 3, 4]
for i in itertools.combinations(items, 2):
    print(i)


items = ["P", "y", "t", "h", "o", "n"]
for i in itertools.permutations(items):
    print(i)


list_one = ['a', 'b']
list_two = [1, 2, 3]
list_three = ['x', 'y']
count = 0
for i in itertools.cycle(itertools.chain(list_one, list_two, list_three)):
    if count >= 35:
        break
    print(i)
    count += 1


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for i in itertools.islice(fibonacci(), 10):
    print(i)


list1 = ['red', 'blue']
list2 = ['shirt', 'shoes']
for i in itertools.product(list1, list2):
    print(i)