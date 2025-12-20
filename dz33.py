from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque


nums = [1, 3, 4, 3, 2, 2, 1, 2, 2, 3, 4, 3, 4, 3, 2, 3, 4, 2, 3, 4, 3, 4, 3, 3, 3, 3, 5, 6, 7, 8, 7, 6, 6, 5, 8, 9, 7,]
count = Counter(nums)
sort_count = count.most_common()
print(len(count))
print(sort_count[:3])


book = namedtuple("book", ["title", "author", "genre"])
book_one = book(title='Harry Potter', author='Джоан Кэтлин Роулинг', genre='фэнтези')
book_two = book(title='Война и мир', author='Лев Толстой', genre='роман')
book_three = book(title='Гордость и предубеждение', author='Джейн Остен', genre='проза')
book_four = book(title='Обитаемый остров', author='Братья Стругацкие', genre='фантастика')
print(book_one.title, book_two.author, book_three.genre, book_four.author)


collections_dict = [1, 3, 4, 3, 2, 2, 1, 2, 2, 3, 4, 3, 4, 3, 2, 3, 4, 2, 3, 4, 3, 4, 3, 3, 3, 3, 5, 6, 7, 8, 7, 6, 6, 5, 8, 9, 7,]
collection_dict = defaultdict(list)
test_list = []
for i in collections_dict:
    collection_dict[i].append(i)
print(collection_dict)


nums = deque([8, 7, 6, 5, 4, 3, 2, 1,])
nums.append(0)
print(nums)
nums.appendleft(9)
print(nums)
nums.pop()
print(nums)
nums.popleft()
print(nums)


def queue_append(queue, item):
    queue.append(item)
def queue_appendleft(queue, item):
    queue.appendleft(item)
def queue_pop(queue):
    return queue.pop()
def queue_popleft(queue):
    return queue.popleft()

nums = deque([])
queue_append(nums, 1)
print(nums)
queue_appendleft(nums, 0)
print(nums)
queue_pop(nums)
print(nums)
queue_popleft(nums)
print(nums)