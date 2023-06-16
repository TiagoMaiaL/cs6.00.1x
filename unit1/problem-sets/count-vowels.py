# The solution to the first problem in the problem set for unit one.

s = "azcbobobegghakl"
num_vowels = 0

for char in s:
  if char == "a" or char == "e" or char == "u" or char == "o" or char == "u":
    num_vowels += 1

print("Number of vowels:", num_vowels)
