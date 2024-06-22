import time

# Number of arithmetic operations to perform
num_operations = 100_000_000

# Addition
start_time = time.time()
result = 0
for _ in range(num_operations):
    result += 1
end_time = time.time()
print(f"Time taken for 100 million additions: {end_time - start_time:.4f} seconds")

# Subtraction
start_time = time.time()
result = num_operations
for _ in range(num_operations):
    result -= 1
end_time = time.time()
print(f"Time taken for 100 million subtractions: {end_time - start_time:.4f} seconds")

# Multiplication
start_time = time.time()
result = 1
for _ in range(num_operations):
    result *= 1
end_time = time.time()
print(f"Time taken for 100 million multiplications: {end_time - start_time:.4f} seconds")

# Division
start_time = time.time()
result = num_operations
for _ in range(num_operations):
    result /= 1
end_time = time.time()
print(f"Time taken for 100 million divisions: {end_time - start_time:.4f} seconds")

'''
Time taken for 100 million additions: 4.7678 seconds
Time taken for 100 million subtractions: 4.7421 seconds
Time taken for 100 million multiplications: 3.8866 seconds
Time taken for 100 million divisions: 4.7869 seconds
'''

