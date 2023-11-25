def directions():
    steps = ['Move forward' ,'Move backward','Move left','Move right']
    return steps
def movements():
    path = ['Move forward',10,'Move backward',5,'Move left',3,'Move right',1]
    return path

def menu():
    print('Please select a direction: ')
    returned_steps = directions()
    for index_position in range(len(returned_steps)):
        print(f'{index_position}: {returned_steps[index_position]}')
        input()
def run_task1():
    returned_steps = directions()
    print(directions())
def run_task2():
    print('Moving...')
    returned_path = movements()

    for index in range(len(returned_path)):
        print(f'{returned_path[index]} for {returned_path[index+1]} steps')

run_task1()