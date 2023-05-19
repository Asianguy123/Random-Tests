# Scheduler
# SJF, RR, FCFS
# assume quantum of 5

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import random

# ---------------------------------------------------------------------------------------------------------------------
# User Input

def user_select():
    '''
    User chooses which scheduling method they want
    '''

    choice = int(input('Enter the corresponding number:\n\n1 - Shortest Job First\n2 - First Come First Serve\n3 - Round Robin\n\nEnter here:  '))
    return choice - 1

# ---------------------------------------------------------------------------------------------------------------------
# Scheduling Procedures

def SJF(bursts):
    '''
    Shortest Job First scheduling:

    - takes list of bursts, sorts by burst length, then 'executes' the tasks
    - outputs total time
    - simulates addition of a new task
    '''
    
    # output + variables
    sorted_bursts = sorted(bursts)
    time = 0
    new_task = random.randint(1, 20)
    new_task_pos = random.randint(1, len(bursts) - 2)
    print('Shortest Job First\n\n')

    # loop to iterate through bursts
    job = 0
    end = False
    while not end:

        # checks if its time for new task, if so adds and resorts
        if job == new_task_pos:
            sorted_bursts.insert(new_task_pos, new_task)
            print(f'\nNew task added with burst length {new_task}\n{sorted_bursts}\n')
            sorted_bursts = sorted(sorted_bursts)
            
        # adds to total time + output
        time += sorted_bursts[job]
        print(f'Burst of {sorted_bursts[job]}:  Total time = {time}')
        
        # checks if all tasks have been completed and loop must end
        if job == len(sorted_bursts) - 1:
            end = True

        job += 1

def FCFS(bursts):
    '''
    First Come First Serve scheduling:

    - takes list of bursts and 'executes' in given order
    - simulates addition of a new task
    '''

    # output + variables
    time = 0
    new_task = random.randint(1, 20)
    new_task_pos = random.randint(1, len(bursts) - 2)
    print('First Come First Serve\n\n')
    
    # loop to iterate through bursts
    job = 0
    end = False
    while not end:

        # checks if its time for new task, if yes adds to bursts list
        if job == new_task_pos:
            bursts.append(new_task)
            print(f'\nNew task added with burst length {new_task}\n{bursts}\n')

        # adds to total time + output
        time += bursts[job]
        print(f'Job {job + 1} - Burst of {bursts[job]}:  Total time = {time}')

        # checks if all tasks have been completed and loop must end
        if job == len(bursts) - 1:
            end = True

        job += 1

def RR(bursts):
    '''
    Round Robin scheduling:

    - takes list of bursts, and executes each one for quantum length (5)
    - cycles through every task until all completed
    - simulates addition of a new task
    '''

    # output + variables
    quantum = 5
    total_time = 0
    new_task = random.randint(1, 20)
    new_task_time = random.randint(1, round(sum(bursts) * 4/5))
    bursts_copy = bursts
    completed_tasks = []
    print('Round Robin\n\n')

    # loops until all tasks completed
    empty = False
    while not empty:

        # checks if all tasks completed, breaks loop if so
        if all(i == ' ' for i in bursts):
            empty = True

        # loop to iterate through bursts
        i = 0
        loop_end = False
        while not loop_end:
            print(f'Job {i + 1}:    {bursts[i]}')

            # check if a complete pass has occurred, breaks loop if so
            if i == (len(bursts) - 1):
                print('\n')
                loop_end = True

            # if its time for new task to be added, append to bursts list
            if total_time >= new_task_time:
                bursts.append(new_task)
                print(f'\nNew task added with burst length {new_task}\n{bursts_copy}\n')
                new_task_time = 3001 # beyond maximum possible total time

            # operates only on integer elements
            if type(bursts[i]) == int:
                
                # adds burst length/quantum to total time
                if bursts[i] < 5:
                    total_time += bursts[i]
                else:
                    total_time += quantum

                # subtracts from burst length
                bursts[i] -= quantum

                # if task complete, set element to ' ' and append job position to completed list
                if bursts[i] <= 0:
                    bursts[i] = ' '
                    completed_tasks.append(i + 1)

            i += 1

    # output      
    print(f'Completion Order: {completed_tasks}')
    print(f'Total time: {total_time}')
        
# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    '''
    Called on program running, creates bursts list and calls appropriate procedure
    '''

    # making random number of jobs, with random bursts
    bursts = []
    for count in range(random.randint(8, 15)):
        bursts.append(random.randint(1, 20))

    print(f'{bursts}\n\n')

    # calls users chosen scheduling method
    funcs = [SJF, FCFS, RR]
    choice = user_select()
    funcs[choice](bursts)
    
# ---------------------------------------------------------------------------------------------------------------------
# Runs Program

if __name__ == '__main__':
    main()
