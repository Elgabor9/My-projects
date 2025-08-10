'''
first my code takes the input in a 2d array.
then I use nested loop to get the decoded script
then I use re module to replace any non_wanted char between the alphabets and replace it with space
'''
import re
line=input().split()
num_rows=int(line[0])
num_cols=int(line[1])
array = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
for i in range(num_rows):

    string=input() # I use it because the input is already a string and I want to separate it

    for j in range(len(string)):
        array[i][j]=string[j]
decoded_script=''
for i in range(num_cols):
    for j in range(num_rows):
        decoded_script+=array[j][i]

# The regular expression pattern
pattern = r"([a-zA-Z0-9])([^a-zA-Z0-9]+)([a-zA-Z0-9])"

# The replacement string
replacement = r"\1 \3"

# Perform the substitution
final_output = re.sub(pattern, replacement, decoded_script)

print(final_output)