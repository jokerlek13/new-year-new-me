def custom_sorting(element):
    if isinstance(element, int):
        return element
    elif isinstance(element, list) and len(element) == 1:
        return element[0]

def sort_list_by_content(lst):
    return sorted(lst, key=custom_sorting)

# Test cases
print(sort_list_by_content([4, 1, 3]))  # Output: [1, 3, 4]
print(sort_list_by_content([[4], [1], [3]]))  # Output: [[1], [3], [4]]
print(sort_list_by_content([4, [1], 3]))  # Output: [[1], 3, 4]
print(sort_list_by_content([[4], 1, [3]]))  # Output: [1, [3], [4]]
print(sort_list_by_content([[3], 4, [2], [5], 1, 6]))  # Output: [1, [2], [3], 4, [5], 6]
