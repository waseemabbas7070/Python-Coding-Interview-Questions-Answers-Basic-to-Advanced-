# Using set() (Fastest, but loses order)

# def remove_duplicates(lst):
#     return list(set(lst))
# numbers = [1, 2, 3, 2,2, 4, 5, 1, 6]
# print(remove_duplicates(numbers))

# Using set() (Fastest, but Unordered)
# def remove_duplicates(lst):
#     return list(set(lst))
# numbers = [3, 7, 2, 9, 5, 1, 8, 3, 2, 9]

# unique_numbers = remove_duplicates(numbers)

# print(unique_numbers)


# Using a loop (Maintains order)

# def remove_duplicates(lst):
#     unique_list = []
#     for num in lst:
#         if num not in unique_list:
#          unique_list.append(num)
#     return unique_list
# numbers = [1, 2, 3, 2, 4, 5, 1, 6]
# print(remove_duplicates(numbers))

#  Using a Loop (Preserves Order)

# def remove_duplicates(lst):
#     unique_list = []
#     for num in lst:
#         if num not in unique_list:
#             unique_list.append(num)
#     return unique_list
# numbers = [3, 7, 2, 9, 5, 1, 8, 3, 2, 9]
# unique_number = remove_duplicates(numbers) 
# print(unique_number)

# Using dict.fromkeys() (Maintains order, faster than a loop)

# def remove_duplicates(lst):
#     return list(dict.fromkeys(lst))
# numbers = [1, 2, 3,3,4,5,5,6,1, 2, 4, 5, 1, 6]
# print(remove_duplicates(numbers))    

# Using dict.fromkeys() (Pythonic and Ordered)


def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
numbers = [3, 7, 2, 9, 5, 1, 8, 3, 2, 9]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)