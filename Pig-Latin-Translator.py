

#Pig Latin translator.

"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."pyg = 'ay'"""

#Enter user input
original = raw_input('Enter a word:')

#Check a valid word is entered by user
if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word +first+pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'