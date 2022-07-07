# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

# Variant 1

fibonacci_sequence = [1, 2]
a = 1
b = 2
while a + b < 4000000:
    b = a + b
    a = b - a
    fibonacci_sequence.append(b)
even_valued_terms = [numbers for numbers in fibonacci_sequence
                     if numbers % 2 == 0]
print("List of even-valued terms: ", even_valued_terms)
print("Sum of even-valued terms:", sum(even_valued_terms))

# Variant 2

a = 1
b = 2
summa = 2
while a + b < 4000000:
    b = a + b
    a = b - a
    if b % 2 == 0:
        summa = summa + b
print("Sum of even-valued terms:", summa)
