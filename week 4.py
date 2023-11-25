def from_chart_to_ascii():
    print('Program started!')
    single_chart = input('Please enter a standard character:')

    if len(single_chart) == 1:
        print(f'The ASCII code for {single_chart} is {ord(single_chart)}')
    else:
        print(f'Please type a number within the correct range. The program is terminating!')

def from_ascii_to_chart():
    print('Program started!')
    ascii_code = int(input("Please type an ASCII code [32-126]: "))
    if ascii_code in range(32, 127):
        print(f'The character for the {ascii_code} is {chr(ascii_code)}')
    else:
        print(f'Please type a number within the correct range. The program is terminating!')

while True:
    choice = input("""
Please choose an option:
1 => From chart to ASCII
2 => From ASCII to chart
q => Exit/Quit
""")

    if choice == '1':
        from_chart_to_ascii()
        break
    elif choice == '2':
        from_ascii_to_chart()
        break
    elif choice == 'q':
        print('The program is terminated!')
        break
    else:
        print('Type either 1 or 2, or q to quit, please!')
