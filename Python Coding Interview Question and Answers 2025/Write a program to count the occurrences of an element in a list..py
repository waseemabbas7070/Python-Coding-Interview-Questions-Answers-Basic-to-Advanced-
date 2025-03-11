def counter(lst,element):
    return lst.count(element)
numbers = [3, 7, 2, 9, 5, 1, 8, 3, 2, 9, 3]
element = 2
count = counter(numbers,element)


print(f"{element} appears {count} time")