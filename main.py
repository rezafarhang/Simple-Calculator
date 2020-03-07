import re

print("Welcome MegaCalc !")
print("Type 'help' For Guidlines.")

run = True  # running flag for perform
previous_result = 0  # this variable assign pervious equation


def help():  # this function show guidlines
    print("Type 'quit' To Exit.")
    print("Type 'reset' To Restart Evaluation.")


def evaluate():  # main function for perform mathmatical options
    global run, previous_result
    # getting input
    if previous_result == 0:
        equation = input("\nPlease Enter Your Equaiton:")
    else:
        equation = input()
    # non-evaluation actions
    if equation == 'quit':
        print("GoodBye!")
        run = False
    elif equation == 'help':
        help()
    elif equation == 'reset':
        previous_result = 0
        evaluate()
    # act of evaluating
    elif previous_result == 0:
        equation = re.sub('[A-Za-z;:()." "]', '',
                          equation)  # if input is not arithmetic equation subtitue it with nothing for handling exceptions
        previous_result = eval(equation + "+0")
        print(previous_result, end="")
    else:
        equation = re.sub('[A-Za-z;:().!@#$^&" "]', '', equation)
        previous_result = eval(str(
            previous_result) + equation + "+0")  # if input is not arithmetic equation subtitue it with nothing for handling exceptions
        print(previous_result, end="")


while run:
    evaluate()
