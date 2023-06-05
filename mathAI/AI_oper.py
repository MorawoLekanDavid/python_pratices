def my_bot():
    print("Welcome to a simple math session\n")
    print("I can perform any simple arithmetic for you in a split seconds.\n")
    #print("tell me what you would like me to do for you.feel free to express yourself")

def bot_task_array():
    task_array = ['addition','subtraction','division','multiplication']
    return task_array

def user():
    user_input = input("tell me what you would like me to do for you.feel free to express yourself\n")
    return user_input

def perform_arithmetic(oper,nums):
    num_array = []
    for n in nums:
        num_array.append(n)
    if oper == bot_task_array()[0]:
        result = sum(num_array)
        print(f"The {oper} of the numbers is: {float(result)}")
    if oper == bot_task_array()[1]:
        minus = float(num_array[0])-sum(num_array[1:])
        print(f"The {oper} of the numbers is: {float(minus)}")
    if oper == bot_task_array()[2]:
        res = float(num_array[0])
        for num in num_array[1:]:
            try:
                if float(num) == 0:
                      raise ZeroDivisionError
            except ZeroDivisionError:
                print("You can't divide by zero")
                break
            else:
                res /= float(num)
        print(f"The {oper} of the numbers is: {res}")
    if oper == bot_task_array()[3]:
        dm = 1
        for num in num_array:
            dm *= float(num)
        print(f"The {oper} of the numbers is: {float(dm)}")

def check_user_input(inp):
    for oper in bot_task_array():
        if str(oper) in inp:
            user_input = input(f"Enter the number(s) seperated by commas you would like to {oper} on\n")
            input_string = user_input.split(',')
            num_array = []
            for num_entry in input_string:
                num_array.append(float(num_entry))
            num_entries = tuple(num_array)
            perform_arithmetic(oper,num_entries)
            break
    else:
        msg = f"Try using the keyword {bot_task_array()}"
        print(msg)
