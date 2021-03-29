def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max              


numbers = [10, 300, 6, 2]
print(max(numbers))
    