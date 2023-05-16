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
	'''
	Creates safe object, with a random code (1-20) and as default sets the status to not solved
	checks if an object is solved and displays appropriate CLI text art for each object
	'''

	status = 0 # sets status to 0 for all instances ==> not solved

	def __init__(self): # creates safe object
		self.code = randint(1, 20) # assigns random code 1-20
		
	def guess(self, attempt):
		if int(attempt) == self.code: # checks to see if correct code is guessed for the individual safe
			self.status = 1 # if solved status = 1

	def art(self):
		if self.status: # if status is 1, add open lock art to art list
			print('''
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
		if not self.status: # if status is 0, closed lock art to art list
			print('''        
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
	
	# while turns still available and not yet solved
	while counter > 0 and not end:
		solved_count = 0
		attempt = input('Guess a code:  ')
		
		for safe in safes:
			safe.guess(attempt) # checks if input is correct for any of the objects
			solved_count += safe.status # counts how many safes have been cracked
			safe.art() # displays text art
		counter -= 1 # decrements number of turns
		
		sleep(1)
		if solved_count == num_of_safes: # checks if all safes have been solved
			end = True # exits loops
		else:
			print(f'{counter} attempts left') # outputs number of turns left
		sleep(1)

	# outputs message based on outcome
	if counter == 0:
		print('You got caught') 
	if counter > 0:
		print(f'You cracked all the safes and stole £{randint(1, 1000000000)}')

# --------------------------------------------------------------------------------------------------
# Runs program

if __name__ == '__main__':
	run()