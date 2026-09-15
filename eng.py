def eng():
    while True:
        name = input('Hello my friend. What is your name?: ')
        print(f'Nice to meet you , {name}!')

        age = input('\nHow old are you? ')
        if not age.isdigit():
            print('Write valid age\n')
            continue

        age = int(age)
        if age < 18:
            print('Sorry, your age is too young')
            continue
        else:
            break


    friend = input('\nYou want to find Girlfriend(1) or Boyfriend(2)?(write a number): ')
    if friend == '1':
        friend = 'Girlfriend'
    elif friend == '2':
        friend = 'Boyfriend'

    information = input('\nCan you write about you? ')
    print(f'{name}, you are so interesting person')

    form = input('\nWrite 1 to see your form: ')
    if form == '1':
        print(f'''
        --- Your form ---
        Name: {name}
        Age: {age}
        Friend: {friend}
        Information: {information}
        ''')
eng()