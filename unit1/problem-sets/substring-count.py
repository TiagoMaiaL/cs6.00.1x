# The solution to the second exercise of the first problem set: counting the occurrence of a specific substring.

s = "azcbobobegghakl"
s_len = len(s)
sub_string = "bob"
sub_string_count = 0

for s_index in range(s_len):
  # is the sub_string empty?
  if len(sub_string) == 0:
    break

  # Do not proceed if the substring lenght is greater than 
  # the amount of remaing chars in s.
  if s_len - s_index < len(sub_string):
    break

  is_substring_valid = True

  # try to match the substring, looking ahead of the current char.
  for sub_index in range(len(sub_string)):
    if s[s_index + sub_index] != sub_string[sub_index]:
      is_substring_valid = False
      break
  
  if is_substring_valid:
    sub_string_count += 1

print("Number of times " + sub_string + " occurs is: " + str(sub_string_count))

