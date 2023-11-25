def display_chars(file_name, num_of_chars):
    with open(file_name, 'r') as file:
        partial_data = file.read(num_of_chars)
        print(partial_data)

display_chars('data.txt', 10)

def display_line(file_name):
    with open(file_name, 'r') as file:
        first_line = file.readline().rstrip('\n')
        print(first_line, end='')
        second_line = file.readline().rstrip('\n')
        print(second_line)
        third_line = file.readline().rstrip('\n')
        print(third_line)
        fourth_line = file.readline().rstrip('\n')
        print(fourth_line)

display_line('data.txt')

def display_text(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)

def run_task2():
    display_chars('library.txt', 5)
    display_text('library.txt')
    display_line('library.txt')