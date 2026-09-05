"""Solution 09 (bonus) -- Leap years.

On the follow-up question, the honest answer:

Without the parentheses Python reads

    (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

because `and` binds more tightly than `or`. And that expression gives the same
result as the parenthesised one for EVERY year. Checked for years 1 to 4000:
zero differences. The reason: anything divisible by 400 is also divisible by 4,
so the case where the two forms could disagree does not exist.

So why the parentheses? Because the expression should mirror the RULE, not just
its result. The rule says "divisible by 4 AND (...)". Writing it without
parentheses relies on an operator precedence and on a property of numbers,
neither of which is stated anywhere. The next reader would have to prove what
they ought to be able to read.
"""

year = 2024
print(f"{year}: {year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)}")

year = 1900
print(f"{year}: {year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)}")

year = 2000
print(f"{year}: {year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)}")

year = 2023
print(f"{year}: {year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)}")
