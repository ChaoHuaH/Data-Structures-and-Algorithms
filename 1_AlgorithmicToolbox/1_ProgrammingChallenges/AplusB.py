# Sum of Two Digits Problem
# Compute the sum of two single digit numbers.
# Input: Two single digit numbers
# Output: The sum of these numbers.
import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
sys.stdout.write(str(a + b))


