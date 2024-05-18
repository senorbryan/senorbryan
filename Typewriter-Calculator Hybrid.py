#Assignment 2 - Using What We Know

#Hello Professor. This is my typewriter-calculator hybrid, which will 
#receive text and print it based on user input as well as a calculator
#which can do 4 basic operations on two variables. Enjoy :)

#Introduction
print('Welcome to the typewriter-calculator hybrid. Please select from our options.')
print("""
      1.Typewriter
      2.Computer
      """)


#Variables needed for the truth conditions
switch = ''
key = input()

#Loop condition for an invalid input
while not(key == '1' or key == '2'):
    print('You did not input "1" or "2."         Please select from our options.')
    print("""
      1.Typewriter
      2.Calculator
      """)
    key = input()

#Condition for the typewriter selection
if key == '1':
    while not(switch == 'end'):
        print('Welcome to the typewriter. Enter "end" at the prompt to stop the program.')
        print('Please input your text:')
        character = input()
        print('Enter the number of times you want to print the text.')
        iterator = int(input())

        for i in range(int(iterator)):
            print(character)

        print('Would you like to type anything else? Input anything besides "end" to keep typing.')
        switch = input()

#Condition for the typewriter selection
elif key == '2':
    print('Welcome to the calculator. Enter "end" at the prompt to stop the program.')
    print('Please input the type of operation needed:')
    print("""
          1.Addition
          2.Subtraction
          3.Multiplication
          4.Division
          """)
    switch = input()
    
    if (switch == '1'):
        print('Please select your first variable to be added:')
        variable_1 = float(input())
        print('Please select your second variable to add to ', variable_1, ":")
        variable_2 = float(input())
        print(variable_1 + variable_2)

    elif (switch == '2'):
        print('Please select your first variable to be subtracted:')
        variable_1 = float(input())
        print('Please select your second variable to subtract from ', variable_1, ":")
        variable_2 = float(input())
        print(variable_1 - variable_2)

    elif (switch == '3'):
        print('Please select your first variable to be multiplied:')
        variable_1 = float(input())
        print('Please select your second variable to multiply by ', variable_1, ":")
        variable_2 = float(input())
        print(variable_1 * variable_2)

    elif (switch == '4'):
        print('Please select your divident:')
        variable_1 = float(input())
        print('Please select your divisor for ', variable_1, ":")
        variable_2 = float(input())
        print(variable_1 / variable_2) 

    #Condition for an invalid input whilst in the calculator if statement
    else:
        while not(switch == '1' or switch == '2' or switch == '3' or switch == '4'):
            print('You have selected an invalid option. Please input an appropriate option:')
            print('Welcome to the calculator. Enter "end" at the prompt to stop the program.')
            print('Please input the type of operation needed:')
            print("""
                1.Addition
                2.Subtraction
                3.Multiplication
                4.Division
                """)
            switch = input()
    
        if (switch == '1'):
            print('Please select your first variable to be added:')
            variable_1 = float(input())
            print('Please select your second variable to add to ', variable_1, ":")
            variable_2 = float(input())
            print(variable_1 + variable_2)

        elif (switch == '2'):
            print('Please select your first variable to be subtracted:')
            variable_1 = float(input())
            print('Please select your second variable to subtract from ', variable_1, ":")
            variable_2 = float(input())
            print(variable_1 - variable_2)

        elif (switch == '3'):
            print('Please select your first variable to be multiplied:')
            variable_1 = float(input())
            print('Please select your second variable to multiply by ', variable_1, ":")
            variable_2 = float(input())
            print(variable_1 * variable_2)

        elif (switch == '4'):
            print('Please select your divident:')
            variable_1 = float(input())
            print('Please select your divisor for ', variable_1, ":")
            variable_2 = float(input())
            print(variable_1 / variable_2)



        


