#!/usr/bin/python
import re

def extract_and_multiply(memory):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r'mul\(\d+,\d+\)'
    
    # Find all matches in the memory string
    matches = re.findall(pattern, memory)
    
    # Initialize sum of results
    total_sum = 0
    
    # Iterate over each match
    for match in matches:
        # Extract the numbers X and Y
        numbers = re.findall(r'\d+', match)
        x, y = int(numbers[0]), int(numbers[1])
        
        # Multiply X and Y and add to the total sum
        total_sum += x * y
    
    return total_sum

# Read the corrupted memory string from the file "day3.txt"
with open('./s.txt', 'r') as file:
    memory_string = file.read()

# Calculate the sum of results of valid mul(X,Y) instructions
result = extract_and_multiply(memory_string)

print(f"The sum of the results of valid mul(X,Y) instructions is {result}.")