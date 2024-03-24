swimming = int(input('Enter your swim time in minutes: '))
cycling = int(input('Enter your cycle time in minutes: '))
running = int(input('Enter your running time in minutes: '))

total = swimming + cycling + running

if total <= 100:
    print('Provincial colours')
elif total <= 105:
    print('Provincial half colours')
elif total <= 110:
    print('Provincial scroll')
else:
    print('NO AWARD')