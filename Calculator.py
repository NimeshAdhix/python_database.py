import re
print("Welcome to the magical calculator!!!")
print("Type quit to end calculation")
previous = 0
run = True

def perform_calculation():
    global run
    global previous
    #Checks whether there was any calculation or not
    if previous == 0:
        equation = input("Enter the calculation:")
    else:
        equation = input(str(previous))
    #Checks whether the input is to quit the calculation
    if equation == 'quit':
        print("Good Bye Human")
        run = False
        #re.sub() method is used to neglect the unncecessary items/values
    else:
        equation = re.sub(r'[a.;'']', "", equation)
        #Checks whether there is any previous calculation or not
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
while run:
    perform_calculation()








