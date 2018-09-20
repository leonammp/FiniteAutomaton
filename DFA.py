# -*- coding: utf-8 -*-
from texttable import Texttable
import sys

# File with the automaton structure
automaton = open("automaton.txt", "r")
try:
	# Convert txt to code
	exec(automaton.read())
except Exception as e:
	print("Error to convert automaton.txt in python code!")
	print(e)
	sys.exit(1)

table = Texttable()
table.set_cols_align(['r', 'r', 'r'])

# Returns automaton alphabet
def getAlphabet(states):
	alphabet = []
	for state in states:
		for symbol in states[state].keys():
			if symbol not in alphabet:
				alphabet.append(symbol)
	return alphabet

# Draw transition table
def makeTable(states):
	header = getAlphabet(states)
	header.insert(0, "δ")
	table.add_rows([header])
	line = []
	for state in states:
		textState = state
		if state in ends:
			textState = '•'+textState
		if state in start:
			textState = '⇾ '+textState
		line.append(textState)	
		for symbol in header:
			if symbol in states[state]:
				line.append(states[state][symbol])
		table.add_row(line)
		line = []
	return table.draw()

# Validate the input word
def checkWord(word, state = start):
	# End of the word
	if word == 'ε':
		print('  δ*(%s, %s)' % (state, word))
		print("  Last State: %s" %(state))
		if state in ends:
			print("The word is accepted!\n")
		else:
			print("The word isn't accepted!\n")
		return
	print('  δ*(%s, %s)' % (state, word))
	# Set the next caractere of the word
	if len(word) > 1:
		print('  δ*(δ(%s,%s), %s)' % (state, word[0], word[1:]))
		# Set the next state
		state = states[state][word[0]]
		word = word[1:]
	else:
		print('  δ*(δ(%s,%s), ε)' % (state, word[0]))
		# Set next state
		state = states[state][word[0]]
		word = 'ε'
	checkWord(word, state)

# Checks whether the input symbol in the alphabet exists
def checkAplhabet(word, states):
	alphabet = getAlphabet(states)
	ret = True
	for symbol in word:
		if symbol not in alphabet:
			ret = False
	return ret

print('\nTransition Table:')
print(makeTable(states))
word = raw_input("Word: ")
while word != '':
	if checkAplhabet(word, states):
		print("\nStep by step:")
		checkWord(word)
	else:
		print("** The word contains a symbol not recognized by the automaton! **")
	word = raw_input("Word: ")