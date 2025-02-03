def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: 0

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: 3.0

my_numbers = [1, 2, 3, 4, 5, "a"]
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: 3.0 (ignores the string)

my_numbers = ["a", "b", "c"]
average = calculate_average(my_numbers) 
print(f"The average is: {average}") #Output: 0