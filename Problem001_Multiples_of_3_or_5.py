# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

all_natural_numbers = list(range(1000))
numbers_that_are_multiples_of_3_or_5 = list(numbers for numbers
            in all_natural_numbers if numbers % 3 == 0 or numbers % 5 == 0)
print(sum(numbers_that_are_multiples_of_3_or_5))
