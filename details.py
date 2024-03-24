# ask the user to input name, age, house number and street name and store these variables using the input function
name = input('Enter your name: ')
age = input('Enter your age: ')
house_number = input('Enter your house number: ')
street_name = input('Enter your street name: ')
# use function print() to print a sentance to state the user's name, age and where they live
# convert the variables that are integers into string using f-strings
print(f'This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}')