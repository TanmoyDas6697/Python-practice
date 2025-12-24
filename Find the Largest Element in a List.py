def find_largest_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    largest = lst[0]
    for element in lst:
        if element > largest:
            largest = element
    return largest

List = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in List]
largest_element = find_largest_element(numbers)
print("The largest element in the list is:", largest_element)