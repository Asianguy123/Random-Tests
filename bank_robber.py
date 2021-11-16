# OOP Bank Robber Game

'''
5 safes that need a code to open 
Codes are random numbers 1-20
10 turns to unlock all 5 safes
'''

# --------------------------------------------------------------------------------------------------
# Imports

import random
import time
from random import randint
from time import sleep

# --------------------------------------------------------------------------------------------------
# Classes

class Safe():
	
	status = 0 # sets status to 0 ==> not solved

	def __init__(self): # creates safe object
		self.code = randint(1, 5) # assigns random code 1-20
		
	def guess(self, attempt):
		if int(attempt) == self.code: # checks to see if correct code is guessed for the individual safe
			self.status = 1 # if solved status = 1

# --------------------------------------------------------------------------------------------------
# Visual Representation

def art(safes):
	'''
	Creates, assigns and displays appropriate CLI lock text art for each safe
	'''

	art = []
	for safe in safes: # for each safe in safe list
		if safe.status: # if status is 1, add open lock art to art list
			art.append('''
      ██████      
    ██      ██    
    ██      ██    
    ██            
  ██████████████ 
██              ██
██      ██      ██
██      ██      ██
██              ██
  ██████████████
''')
		if not safe.status: # if status is 0, closed lock art to art list
			art.append('''        
      ██████
    ██      ██
    ██      ██
  ██████████████
██              ██
██      ██      ██
██      ██      ██
██              ██
  ██████████████
''')
		
		print(f'{art[safes.index(safe)]}') # outputs corresponding art

# --------------------------------------------------------------------------------------------------
# Main Code

def run():
	'''
	Main function that takes input and combines all elements of the program to form the required game
	'''

	counter = 10 # number of turns to solve all the safes
	num_of_safes = 5 # number of objects to be created
	safes = [] 
	end = False # flag

	for i in range(num_of_safes):
		safes.append(Safe()) # creates desired number of safe objects and stores in safes list
	
	while counter > 0 and not end: # while turns still available and not yet solved
		solved_count = 0
		art(safes) # displays text art
		attempt = input('Guess a code:  ') # user input
		
		for safe in safes:
			safe.guess(attempt) # checks if input is correct for any of the objects
		counter -= 1 # decrements number of turns
		
		for safe in safes:
			solved_count += safe.status # counts how many safes have been cracked
			
		if solved_count == num_of_safes: # checks if all safes have been solved
			print(f'You crack all the safes and stole £{randint(1, 1000000000)}')
			end = True # exits loops
		else:
			print(f'{counter} attempts left') # outputs number of turns left
			sleep(1) # pauses program so user can read message

	if counter == 0: # if no more turns, output message
		print('You got caught') 

# --------------------------------------------------------------------------------------------------
# Runs program

if __name__ == '__main__':
	run()