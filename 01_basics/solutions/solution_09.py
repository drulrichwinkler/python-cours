"""Solution 09 (bonus) -- The log line.

Which one reads better? The f-string -- because the line in the source looks the
way the output will look. With sep= you have to assemble the result in your head.

From module 08 onwards we read exactly this format back in.
"""

tag = "TH-04"
time = "14:05"
reading = 22.83333

# Way 1 -- using sep=
print(time, tag, f"{reading:.1f} C", sep=" | ")

# Way 2 -- as an f-string
print(f"{time} | {tag} | {reading:.1f} C")
