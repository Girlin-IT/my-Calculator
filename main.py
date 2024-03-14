# time module will help set time and delays in printing
# colorama module will help add colour and style your code
import time
from time import sleep
import sys
import random
import colorama
from colorama import Fore, Back, Style
ct = time.ctime()

# print(Fore.BLACK)
# colorama.init(autoreset = True)
def slow_word(text):
  words = text
  for char in words:
      time.sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
    # this function will display the output on the console as if it's being typed out
slow_word(Fore.BLACK + Back.WHITE + Style.BRIGHT + ct)
slow_word(Fore.BLACK + Back.WHITE + Style.BRIGHT + '\n' "Welcome to P's calculator")
print(Style.RESET_ALL)
# Creating a procedural computer program
# I've added a while statement at the beginning of the code
# tryexcept statement will help with error handling

# Implement basic math operations
# We need to make sure that the results are rounded to 2 decimal points
# I used the round function to return the result to a number rounded to 2 decimal points

print(Fore.GREEN + Style.NORMAL)

def validate_numbers():
  while True:
    try:
      number = float(input())
      return number
    except ValueError:
      slow_word(Fore.RED + Back.WHITE + Style.BRIGHT + "Please enter a valid number: " + Style.RESET_ALL)
      continue
    
        
def validate_operators():
  while True:
    operator = input()
     # if statements help check if a condition is true or false, it's used for decision making
     #I used a list that contains the valid operators [] 
    if operator in ['+', '-', '*', '/']:
        return operator
    else:
      slow_word(Fore.RED + Back.WHITE + Style.BRIGHT + "Error!! Please enter a valid operator: " + Style.RESET_ALL)
      print(Style.RESET_ALL)
      continue
    
while True:
  time.sleep(1)
  slow_word(Fore.GREEN + "Enter your first number: ")
  num1 = validate_numbers()
  time.sleep(0.3)
  slow_word(Fore.GREEN + "Enter your second number: ")
  num2 = validate_numbers()
  time.sleep(0.5)

  slow_word(Fore.BLUE + "Enter operator: ")
  operator = validate_operators()
  time.sleep(0.5)
  if operator == '+':
    slow_word(Fore.BLACK + str( num1) + ' + ' + str( num2) + ' = ' + str(round(num1 + num2 , 2 )))
  elif operator == '-':
    slow_word(Fore.BLACK + str( num1) + ' - ' + str( num2) + ' = ' + str(round(num1 - num2, 2 )))
  elif operator == '*':
    slow_word(Fore.BLACK + str(num1) + ' * ' + str(num2) + ' = ' + str(round(num1 * num2, 2 )))
  elif operator == '/':
    try:
      num1/num2
      slow_word(Fore.BLACK + str(num1) + ' / ' + str(num2) + ' = ' + str(round(num1 / num2, 2)))
    except ZeroDivisionError:
      slow_word(Fore.RED + Style.BRIGHT + Back.WHITE + "You cannot divide by zero"  + "\n" + Style.RESET_ALL)
      continue
      # I included the try except inside the / elif statement to handle the ZeroDivisionError
  else: 
    slow_word(Fore.RED + Style.BRIGHT + Back.WHITE + 'Error!!! , Please enter a valid opreator: ')
    continue
  
  op = input(Fore.YELLOW + '\n' "Do you want to continue? (y/n): ").lower()
  if op == 'y':
    continue
  else:
    break
slow_word(Fore.BLACK + Back.WHITE + Style.BRIGHT + "Thank you for using P's calculator!!, Goodbye!!")
  

  

    
    







  




  
  

  

