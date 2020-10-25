# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sys

# count down function
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)

# count up function
def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n+1)

# ask user to enter number
if sys.version_info[0] == 3:
  num = input('Enter number: ')
else:
  num = raw_input('Enter number: ')

# convert string to number
num = int(num)

if num > 0:
  # count down positive number
  countdown(num)
elif num < 0:
  # count up negative number
  countup(num)
else:
  print('Blastoff!')
