def my_bot():
    print("Welcome to a simple math session\n")
    print("I can perform any simple arithmetic for you in a split seconds.\n")
    #print("tell me what you would like me to do for you.feel free to express yourself")

def bot_task_array():
    task_array = ['addition','subtraction','division','multiplication']
    return task_array

def user():
    user_input = input("tell me what you would like me to do for you.feel free to express yourself")
    return user_input

def check_user_input():
    for oper in bot_task_array():
        print(oper)
