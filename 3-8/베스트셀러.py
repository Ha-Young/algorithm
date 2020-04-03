
N = int(input())

books = dict()

for _ in range(N):
    book = input()
    
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

target = max(books.values())
array = []

for book, count in books.items():
    if count == target:
        array.append(book)

array.sort()

print(array[0])