#!/usr/bin/python
from itertools import product

def generate_operator_combinations(num_vars):
    # Generate all combinations of '+' and '*' for the given number of variables
    return list(product(['+', '*', '||'], repeat=num_vars))

def evaluate_expression(operands, operators):
    # Evaluate the expression strictly left-to-right
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += operands[i + 1]
        elif operators[i] == '*':
            result *= operands[i + 1]
        elif operators[i] == '||':
            #remeber we cant just mulitply by 10 and add becase this doesnt work for mulit digits eg 45 || 68
            result = int(str(result) + str(operands[i + 1]))
    return result

validSum = 0

def ParseInput():
    global validSum
    
    with open("./day7.txt") as f:
        for line in f:
            operands = []
            (grossNum, numbers) = line.split(":")
            numbers = numbers.split()
            grossNum = int(grossNum)
            noOps = len(numbers) - 1
            for n in numbers:
                operands.append(int(n))

            permutations = generate_operator_combinations(noOps)
            for opList in permutations:
                expressionResult = evaluate_expression(operands, opList)
                if expressionResult == grossNum:
                    validSum += grossNum
                    break

ParseInput()
print("Answer part1 is", validSum)