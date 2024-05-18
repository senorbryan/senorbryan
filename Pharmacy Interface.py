import json #Needed for formatting to print the registrar, i'm not sure why printing it was such an issue

#Entry keys cause it's a pharmacy program and I am too used to security at my job already
passcode = ''
id = ""
key = ''
license = '02 082702'

#Tuple, Dictionary and List :3
registrar = ("Bryan", "Josh", "Sandy", "Katherine")
eScripts = {
    "Amanda Bayer": "Omeprazole - 40 MG",
    "Brandi Jones": "Loratadine - 5 MG",
    "Jennifer Dune": "Alprazolam - 1.5 MG",
    "Martin Cole": "Cyanocobalamin - 1 ct.",
    "Randy Roger": "Tamsulosin - 0.4 MG",
    "Wendy Williams": "Vitamin D3 - 50,000 IU"
}
CONTROLLED = ["Amphetamine Salt", ]


#Entry prompt
print("'Welcome to Winpharm. Please enter the passcode:")
passcode = input()
passcode.lower()

while not (passcode == 'pharmaceutical'):
    print('This is not the correct passcode. Please input the correct passcode:')
    passcode = input()
    passcode.lower()

#Registrar entry prompt
print("Access Granted. Please state your name for recorded entry with the first initial capitalized.")
print("Example: 'Samantha'")
id = input()

#More security measures because I love while loops for some reason
while (id not in registrar):
    print("We're sorry. The selected name is not a current member of our pharmacy. Please try again.")
    print("Example: 'Samantha'")
    id = input()

#Mainframe
print("Access granted. Welcome " + id + ".")
print()
print("Please select an option:")
print("1. View Electronic Scripts")
print("2. Add an eScript")
print("3. Add a pharmacy technician [Pharmacist Only]")
print("4. Document a Controlled Substance [Pharmacist Only]")
print("5. Logout")

key = input()

#Will print the dictionary
if (key == '1'):
        print("--eScripts--")
        print()
        print(json.dumps(eScripts, indent = 4))

#Will add an item and print the dictionary (Almost drove me crazy trying to implement this)
if (key == '2'):
        patient = ''
        prescription = ''

        print("Enter the patient name:")
        patient = input()

        print("Enter the patient's prescription in the following format: Medication - Dosage")
        print("Example: Calcium Tablets - 667 MG")
        prescription = input()

        eScripts[patient] = prescription

        print("--eScripts--")
        print()
        print(json.dumps(eScripts, indent = 4))

#Adding an option to the tuple featuring a security measure with grave consequences for intruders
if (key == '3'):
        print("You are attempting to add a technician to the database. This is a pharmacist only option.")
        print('Please enter your licensing number using this format (00 123456):')
        license = input()

        i = 3

        while not (license == "02 082702"):

            i = i-1

            #Anti social engineering measure
            if (i == 0):
                print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF ATTEMPTS! NATIONAL AUTHORITIES WILL BE TRACKING THE IP ADDRESS!")
                print("&$#&*(@&(#$(@&#@!&($*&)(!@&$(*&(#&(@&($&@#&$(@&#$(&@)($#@(*^*&&#*^*^*^*&^$&*#*#$)")
                break
            
            attempts = str(i)
            print("You have not input a license number. You have " + attempts + " more attempts:")
            license = input()
            int(i)

        confirm = ''

        #Prompt for non-intruders that will add to the tuple
        while not (confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'YES'):
            print('Welcome Bryan. Please enter the name of the registering pharmacy technician. Enter "0" to go back.')
            technician = input()

            if (technician == '0'):
                break

            print('You are submitting the name -' + technician + '-. Is this correct? Enter "Y" or "yes" to confirm.')
            confirm = input()
            confirm.lower()

            eScript_refreshed = registrar + (technician,)

            print()
            print('Successfully added ' + technician + ' to the registrar.')

            print('Pharmacy registrar:')
            print(eScript_refreshed)

#Will add to the list with security system 
if (key == '4'):
    print("You are attempting to document a controlled substance. This is a pharmacist only option.")
    print('Please enter your licensing number using this format (00 123456):')
    license = input()

    i = 3

    while not (license == "02 082702"):

        i = i-1

        if (i == 0):
            print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF ATTEMPTS! NATIONAL AUTHORITIES WILL BE TRACKING THE IP ADDRESS!")
            print("&$#&*(@&(#$(@&#@!&($*&)(!@&$(*&(#&(@&($&@#&$(@&#$(&@)($#@(*^*&&#*^*^*^*&^$&*#*#$)")
            break
            
        attempts = str(i)
        print("You have not input a license number. You have " + attempts + " more attempts:")
        license = input()
        int(i)

    confirm = ''

    #Prompt that will add item to list 
    while not (confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'YES'):
        print('Welcome Bryan. Please enter the name of the controlled medication. Enter "0" to go back.')
        C2 = input()

        if (C2 == '0'):
            break

        print('You are submitting the controlled substance -' + C2 + '-. Is this correct? Enter "Y" or "yes" to confirm.')
        confirm = input()
        confirm.lower()

        CONTROLLED.append(C2)

        print()
        print('Successfully added ' + C2 + ' to the controlled substance records.')
        print()

        print('Controlled Medicine Records:')
        
        for x in range(len(CONTROLLED)):
            print (CONTROLLED[x])

#Logout optionnnnnnn
if (key == '5'):
    print("Thank you " + id + ". You are now logged out.")

#Prompt for out of bounds input
while not(key == '1' or key == '2' or key == '3' or key == '4' or key == '5'):
    print("You have not selected an option. Please select an option:")
    print()
    print("Please select an option:")
    print("1. View Electronic Scripts")
    print("2. Add an eScript")
    print("3. Add a pharmacy technician [Pharmacist Only]")
    print("4. Document a Controlled Substance [Pharmacist Only]")
    print("5. Logout")
    if (key == '1'):
        print("--eScripts--")
        print()
        print(eScripts)

    if (key == '2'):
        patient = ''
        prescription = ''

        print("Enter the patient name:")
        patient = input()

        print("Enter the patient's prescription in the following format: Medication - Dosage")
        print("Example: Calcium Tablets - 667 MG")
        prescription = input()

        escripts = {patient : prescription}

    if (key == '3'):
        print("You are attempting to add a technician to the database. This is a pharmacist only option.")
        print('Please enter your licensing number using this format (00 123456):')
        license = input()

        i = 3

        while not (license == "02 082702"):

            i = i-1

            if (i == 0):
                print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF ATTEMPTS! NATIONAL AUTHORITIES WILL BE TRACKING THE IP ADDRESS!")
                print("&$#&*(@&(#$(@&#@!&($*&)(!@&$(*&(#&(@&($&@#&$(@&#$(&@)($#@(*^*&&#*^*^*^*&^$&*#*#$)")
                break
            
            attempts = str(i)
            print("You have not input a license number. You have " + attempts + " more attempts:")
            license = input()
            int(i)

        confirm = ''

        while not (confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'YES'):
            print('Welcome Bryan. Please enter the name of the registering pharmacy technician. Enter "0" to go back.')
            technician = input()

            if (technician == '0'):
                break

            print('You are submitting the name -' + technician + '-. Is this correct? Enter "Y" or "yes" to confirm.')
            confirm = input()
            confirm.lower()

            eScript_refreshed = registrar + (technician,)

            print()
            print('Successfully added ' + technician + ' to the registrar.')

            print('Pharmacy registrar:')
            print(eScript_refreshed)

    if (key == '4'):
        print("You are attempting to document a controlled substance. This is a pharmacist only option.")
        print('Please enter your licensing number using this format (00 123456):')
        license = input()

        i = 3

        while not (license == "02 082702"):

            i = i-1

            if (i == 0):
                print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF ATTEMPTS! NATIONAL AUTHORITIES WILL BE TRACKING THE IP ADDRESS!")
                print("&$#&*(@&(#$(@&#@!&($*&)(!@&$(*&(#&(@&($&@#&$(@&#$(&@)($#@(*^*&&#*^*^*^*&^$&*#*#$)")
                break
                    
            attempts = str(i)
            print("You have not input a license number. You have " + attempts + " more attempts:")
            license = input()
            int(i)

            confirm = ''

        while not (confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'YES'):
            print('Welcome Bryan. Please enter the name of the controlled medication. Enter "0" to go back.')
            C2 = input()

            if (C2 == '0'):
                break

            print('You are submitting the controlled substance -' + C2 + '-. Is this correct? Enter "Y" or "yes" to confirm.')
            confirm = input()
            confirm.lower()

            CONTROLLED.append(C2)

            print()
            print('Successfully added ' + C2 + ' to the controlled substance records.')
            print()

            print('Controlled Medicine Records:')
            
            for x in range(len(CONTROLLED)):
                print (CONTROLLED[x])

    if (key == '5'):
        print("Thank you " + id + ". You are now logged out.")

    else:
        print()


