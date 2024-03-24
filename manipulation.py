str_manip = input('Enter a sentence: ')
# how many characters in the sentence
print(len(str_manip))

# replace every letter that matches the last letter with @
last_letter = str_manip[-1]

for letter in str_manip:
    if letter == last_letter:
        str_manip = str_manip.replace(letter, '@')

print(str_manip)

# last 3 letters backwards
print(str_manip[:-4:-1])

# word made up of first 3 letters and last 2 letters
five_word = str_manip[0:3] + str_manip[-2:]
print(five_word)