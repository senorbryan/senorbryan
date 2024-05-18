#Final Project

import datetime

instance = datetime.datetime.now()
select = ''

print("Welcome to the Clock. Please select an option:")
print("1.Display the time")
print("2.Display the day of the week")
print("3.Display the date")
print("4.All of the above")

select = input()

while not (select == "1" or select == "2" or select == "3" or select == "4"):
        print("You did not select a valid option. Please select a valid option.")
        print("1.Display the time")
        print("2.Display the day of the week")
        print("3.Display the date")
        print("4.All of the above")

        select = input()

if (select == '1'):
        print("It is currently " + instance.strftime("%I") + ":" + instance.strftime("%M") + " " + instance.strftime("%p"))

if (select == '2'):
        print("Today is currently " + instance.strftime("%A"))

if (select == '3'):
        print("The date is currently " + instance.strftime("%B") + " " + instance.strftime("%d") + "," + instance.strftime("%Y"))

if (select == '4'):
        print("It is currently " + instance.strftime("%I") + ":" + instance.strftime("%M") + " " + instance.strftime("%p"))
        print("Today is currently " + instance.strftime("%A"))
        print("The date is currently " + instance.strftime("%B") + " " + instance.strftime("%d") + "," + instance.strftime("%Y"))
