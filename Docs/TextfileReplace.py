import sys
import fileinput

# replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th
for i, line in enumerate(fileinput.input('demoText.txt', inplace=1)):
    sys.stdout.write(line.replace('sit', 'SIT'))  # replace 'sit' and write
    if i == 4: sys.stdout.write('\n')  # write a blank line after the 5th line