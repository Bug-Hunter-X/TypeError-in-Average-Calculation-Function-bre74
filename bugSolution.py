def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list or only non-numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage
data = [10, 20, 30, 'a']
try:
    average = calculate_average(data)
    print(f"The average is: {average}")
except TypeError as e:
    print(f"Error: {e}")
data2 = [10,20,30,40]
try:
    average2 = calculate_average(data2)
    print(f"The average is: {average2}")
except TypeError as e:
    print(f"Error: {e}")
