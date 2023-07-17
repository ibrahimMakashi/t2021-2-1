def count_multiples(numbers):
    counts = {}

    for i in range(1, 10):
        counts[i] = 0

    for number in numbers:
        for i in range(1, 10):
            if number % i == 0:
                counts[i] += 1
    return counts

# Example
numbers_str = input("Enter a list of numbers (space-separated): ")
numbers_list = list(map(int, numbers_str.split()))
result = count_multiples(numbers_list)
print(result)