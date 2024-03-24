total = 0
count = 0

while True: # while the following is true, the program will loop this command
    number = float(input("Please enter a number: "))
    if number == -1:
        if count == 0:
            print("Stop") # if the only number entered is -1 then the average will not be calculated and the user stops entering numbers
        else:
            average = float(total / count) # calculates the average of the numbers entered
            print("Average of numbers entered (excluding -1):", average)
        break
    total += number # adds the number entered to the running total, does not happen if the number entered is -1
    count += 1