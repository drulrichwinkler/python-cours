"""Solution 06 -- Age group as a boolean expression.

Four output lines because four questions are asked. In module 03 this becomes ONE
line with if/elif -- and then the comparison is worth making: which of the two
reads better, and which one answers the question that was actually asked?
"""

age = 25

print(f"Child: {age < 12}")
print(f"Teen: {12 <= age <= 17}")
print(f"Adult: {18 <= age <= 64}")
print(f"Senior: {age >= 65}")
