def largest_smallest(numbers):
    if not numbers:
        return None,None
    largest = max(numbers)
    smallest = min(numbers)

    return largest , smallest

numbers = [3, 7, 2, 9, 5, -1, 800]   

largest,smallest = largest_smallest(numbers)

print(f"{largest} is  a largest numbers  {smallest} is smallest number " )