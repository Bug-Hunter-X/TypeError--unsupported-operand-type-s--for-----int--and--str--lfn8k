def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}") #This will return 0 which is the intended behavior

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}") #This will return 3.0 which is the intended behavior

my_numbers = [1, 2, 3, 4, 5, "a"]
average = calculate_average(my_numbers) # This will throw TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(f"The average is: {average}")