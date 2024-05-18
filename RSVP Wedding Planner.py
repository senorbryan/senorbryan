print('Welcome to the Wedding RSVP list program. This program will add confirmed attendees to your wedding.')

#This block of code will take in input
print('Enter a name to add to the RSVP attendees:')
name = input()
key = ""

#This object will open, read, and write in the file
file_opener = open('Invites.txt',"a+")

#Sets the position of the cursor in the file
file_opener.seek(0)

#This block of code writes a name in the file while adding a line break between each name
file_opener.write("\n")
file_opener.write(name)

print('Would you like to add another name to the list? Enter "Y" or "y". Input anything else to close the list.')
key = input()
key.lower()

while (key == 'yes' or key == 'y'):
    print('Enter a name to add to the RSVP attendees:')
    name = input()

    #This object will open, read, and write in the file
    file_opener = open('Invites.txt',"a+")

    file_opener.seek(0)

    #This block of code writes a name in the file while adding a line break between each name
    file_opener.write("\n")
    file_opener.write(name)

    print('Would you like to add another name to the list? Enter "Y" or "y". Input anything else to close the list.')
    key = input()
    key.lower()


#This block of code closes the file so that it can be read with the updated names
file_opener.close()

#Re-opens the file with new names added
file_opener = open('Invites.txt', 'r')

#Prints the contents of the RSVP Wedding List
with open('Invites.txt', 'r') as f:
    print(f.read())




