# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through the range from 12 to 19
for number in range(12, 20):
    if number % 2 == 0:
        print(f"{number} is an even number.")
        even_count += 1
    else:
        print(f"{number} is an odd number.")
        odd_count += 1

# Output the counts
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
