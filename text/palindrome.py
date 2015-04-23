# Query user for input, remove all spaces and convert all to lowerspace
# Additional steps can be removing all punctuations as well
word = raw_input('Please enter a word: ').replace(' ', '').lower()

# Check whether word is a palindrome
print word[::] == word[::-1]
