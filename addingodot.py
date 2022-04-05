while True:
    print('\n','this is adding machine','\n')
    try:
        first_number = int(input("what is the first number you want to add >"))
        second_number = int(input('what is the second number you want to add >'))
        sum=first_number+second_number
        print('the of the numbers is',sum)
        break
    except:
        print('Your input is not correct')
