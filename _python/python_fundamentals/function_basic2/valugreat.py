def filter_greater_than_second(first):
    if len(first) < 2:
        return False

    second_value = first[1]
    new_list = [value for value in first if value > second_value]
    print(f"The new list contains {len(new_list)} values greater than the second value.")
    return new_list
original_list = [5, 2, 8, 1, 9]
new_list = filter_greater_than_second(original_list)
print(new_list)

short_list = [1]
result = filter_greater_than_second(short_list)
print(result)  