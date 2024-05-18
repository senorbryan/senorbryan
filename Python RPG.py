
#Assignment 6
import json 
import random

#Classes

class General:
    def __init__(self, name, HP, exp, wins):
        self.name = name
        self.HP = HP
        self.exp = exp
        self.wins = wins
    
    def stats(self):
        if self.HP < 0:
            self.HP = 0

        health = str(self.HP)
        experience = str(self.exp)
        wins = str(self.wins)

        print()
        print("--Stats--")
        print(self.name + ":    ") 
        print("HP:   " + health)
        print("Exp.    " + experience)
        print("Wins:    " + wins)
        
        
    def rules(self):
        print("I see you want to hear the rules " + self.name + ".")
        print()
        print("You are required to win 5 battles in any biome of your choice. You will verse a variety of enemies with elements unique to their biome.")
        print("This is a role-playing based game. You will select a battle option first, your opponent will select a battle option after you.")
        print("You will gain experience with every win. Gain 827 or more experience and you will level up, raising your HP. If your HP reaches 0, you must start over.")
        
    def win(self):
        print(self.name + " wins!")
    
    def victory(self):
        print('Congratulations ' + name + '. You have won the game.')
        print()
        player.stats()
        print()
        print(json.dumps(General.stats, indent = 4))

    
    def game_over(self):
        print("HP has reached 0...")
        print(name + " has lost consciousness...")
        confirm = ''
        print("-Game Over-")


    
   



#Variables
name = ''
confirm = ''
space = ''
option = ''
HP = 50
MAX_HP = 50
increment = 0 + random.randint(2,7)
level = 1
victory = False
win = 0
matches = 0
chance = 0
experience = 0
game_over = False
run = False

stats = {
}
maps = ["The Junkyard", "The Woods", "The Underpass", "Rules", "Stats"]
junkyard_enemies = ["Mad Taxi", "Plague Rat of Doom", "Dirty Soap Bubble"]
woods_enemies = ["Territorial Oak", "Sssssssneaky Snake", "Arachnid!"]
underpass_enemies = ["Shallow Shallow Shadow", "Well-Nutritioned Deer", "Pineapple-Hating Squirrel"]
credits = tuple("Thank You!")
size = len(maps)

#Entry prompt
print("***********Welcome***********")
print("This is a role-playing video game. The format will require you to enter any key to continue.")
print("You may test this now.")
print()
print("Press any key to continue...")
name = input()

print()
print("'Welcome Traveler. Please tell me your name:")
name = input()

if (name == "Don't Care"):
    name = 'Bryan'

print(name + ", is this correct? Enter 'Y' or 'yes' to confirm.")
confirm = input()

while not (confirm == 'Y' or confirm == 'yes'):
    print("Traveler. Please tell me your name.")
    name = input()

    print(name + ", is this correct? Enter 'Y' or 'yes' to confirm.")
    confirm = input()

player = General(name, 50, 0, 0)

#Rules
print("Ok " + name + ". Let's get going. You will be allowed to enter 3 biomes of your choice.")
print("Press any key to continue")
space = input()

print("In order to prove yourself, you must cross any of the following biomes of your choice 5 times.")
space = input()

print("Should your HP points fall to 0, you must start from the beginning. If you level up, you will replenish some health.")
space = input()

while not (HP <= 0 or win >= 5):

    #Level Up Condition
    if (experience >= 827):
        print()
        print("Congratulations, you have leveled up!")

        level = level + 1
        experience = experience - 827

        MAX_HP = MAX_HP + increment
        HP = MAX_HP + 0

        level_stat = ("Level " + str(level))
        exp_stat = str(experience)
        stats[name] = level_stat
        stats["HP"] = health
        stats["Exp."] = exp_stat



    #Game Over condition
    if (HP == 0):
        break

    print(General.stats)
    print(json.dumps(stats, indent = 4))
    print()


    #Biome Selection
    print("Where do you want to go?")
    for i,item in enumerate(maps, 1):
        print(i, item)

    #Fixes the index of choice for the user 
    option = int(input())

    #Out-Of-Bounds Loop
    while (option <= 0 or option >= 6):
        print("I don't see that option on the map. Would you mind trying again?")
        print("Press any key to continue")
        space = input()

        print()
        print("Where do you want to go?")
        for i,item in enumerate(maps, 1):
            print(i, item)

        #Fixes the index of choice for the user 
        option = int(input())

    #Junkyard Biome
    if (option == 1):
        print("Let's head inside the Junkyard.")
        print("Press any key to continue")

        space = input()
        enemy = random.choice(junkyard_enemies)
        enemy_hp = random.randint(20, 25)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
            
            #Attack Condition
            if (choice == '1'):
                damage = random.randint(10,20)
                critical = random.randint(1,100)
                
                #Critical Hit aspect
                if (critical == 100):
                    damage * 10
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()
                       
                else:
                    enemy_hp = enemy_hp - damage
                    dmg = str(damage)

                    print(name + " attacked.")
                    space = input()
                    print()
                    print(name + " dealt " + dmg + " damage.")
                    print()

                #Enemy Attack Path
                attack = random.randint(10,15)
                HP  = HP - attack
                atk = str(attack)
                health = str(HP)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                print("The " + enemy + " dealt " + atk + " damage.")
                print()

                space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)
                    
                if (chance == 1 or chance == 2 or chance == 3):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 4):
                    print("There was no way out.")
                    print()

                    HP  = HP - attack
                    atk = str(attack)
                    health = str(HP)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

            #Enemy Defeat Condition
            if (enemy_hp <= 0):
                experience += experience + random.randint(217,728)
                exp_stat = str(experience)
                win = win + 1

                player.win()

                player.exp = experience
                player.HP = HP
                player.wins = win

                player.stats()

                break

                
            #Game Over Condition
            if (HP <= 0):
                break
    
    #The Woods Biome
    if (option == 2):
        print("Alright, we're outside the woods. I heard the attacks from the inhabitants are hit or miss. Be careful as they are hard to run away from.")
        print("Press any key to continue")

        space = input()
        enemy = random.choice(woods_enemies)
        enemy_hp = 0 + random.randint(25,50)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle Condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
                
            #Fight Condition    
            if (choice == '1'):
                damage = random.randint(5,30)
                critical = random.randint(1,100)

                #Critical Hit Condition
                if (critical == 100):
                    damage * 10
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()
                    
                else:
                    enemy_hp = enemy_hp - damage
                    dmg = str(damage)

                    print(name + " attacked.")
                    space = input()
                    print()
                    print(name + " dealt " + dmg + " damage.")
                    print()

                #Enemy Attack Path
                attack = 5
                rage = random.randint(1,5)

                #Rage Condition
                if (rage == 5):
                    attack = attack * 8
                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

                    HP  = HP - attack
                    atk = str(attack)
                    health = str(HP)

                    print("Ouch! The " + enemy + " dealt " + atk + " damage.")
                    print()

                else :
                    HP  = HP - attack
                    atk = str(attack)
                    health = str(HP)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

                print("The " + enemy + " dealt " + atk + " damage.")
                print()

                space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)

                if (chance == 1):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 2 or chance == 3 or chance == 4):
                    print("There was no way out.")

                    HP  = HP - attack
                    atk = str(attack)
                    health = str(HP)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()
                    
            #Enemy Defeat Condition

            if (enemy_hp <= 0):
                experience += experience + random.randint(170,1307)
                exp_stat = str(experience)
                win = win + 1

                player.win()

                player.exp = experience
                player.HP = HP
                player.wins = win

                player.stats()

                break

            #Game Over Condition
            if (HP <= 0):
                break
    
    #The Underpass Condition
    if (option == 3):
        print("We have arrived to the Underpass. We can't stay here too long however. The radiation is bound to hurt us.")
        print("Press any key to continue")

        space = input()
        enemy = random.choice(underpass_enemies)
        enemy_hp = 0 + random.randint(47, 63)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle Condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
            
            #Fight Condition
            if (choice == '1'):
                damage = random.randint(29,74)
                critical = random.randint(1,17)

                if (critical == 17):
                    damage * 3
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()
                    
                else:
                    enemy_hp = enemy_hp - damage
                    dmg = str(damage)

                    print(name + " attacked.")
                    space = input()
                    print()
                    print(name + " dealt " + dmg + " damage.")
                    print()

                #Enemy Attack Path
                attack = random.randint(0,7)
                HP  = HP - attack
                atk = str(attack)
                health = str(HP)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                #Enemy Miss Condition
                if (attack == 0):
                    print('The ' + enemy + " missed!")
                    space = input()

                else:
                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()

                    space = input()

                attack = random.randint(0,7)
                HP  = HP - attack
                atk = str(attack)
                health = str(HP)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                #Enemy Miss Condition
                if (attack == 0):
                    print('The ' + enemy + " missed!")
                    space = input()

                else:
                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()

                    space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)
                    
                if (chance == 1 or chance == 2 or chance == 3):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 4):
                    print("There was no way out.")
                    print()

                    HP  = HP - attack
                    atk = str(attack)
                    health = str(HP)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

            #Enemy Miss Condition
            if (enemy_hp <= 0):
                experience += experience + random.randint(300,420)
                exp_stat = str(experience)
                win = win + 1

                player.win()

                player.exp = experience
                player.HP = HP
                player.wins = win

                player.stats()

                break

            #Game Over Condition
            if (HP <= 0):
                break
            
            #Damage per round Condition(Biome Specific)
            HP = HP - 5

            print(name + " took 5 damage from the radiation!")

    if (option == 4):
        player.rules()
        confirm = input()

    if (option == 5):
        player.stats()
        confirm = input()

    else:
        while not (option == 1 or option == 2 or option == 3 or option == 4 or option == 5):
            while (option <= 0 or option >= 6):
                print("I don't see that option on the map. Would you mind trying again?")
                print("Press any key to continue")
                space = input()

                print()
                print("Where do you want to go?")
                for i,item in enumerate(maps, 1):
                    print(i, item)

                #Fixes the index of choice for the user 
                option = int(input())

            #Junkyard Biome
            if (option == 1):
                print("Let's head inside the Junkyard.")
                print("Press any key to continue")

                space = input()
                enemy = random.choice(junkyard_enemies)
                enemy_hp = random.randint(20, 25)

                print("--You encounter a " + enemy + "!--")
                print()

                #Battle condition
                while (victory == False):
                    print("What do you want to do?")
                    print("1. Fight")
                    print("2. Run")
                    print()

                    choice = input()
                    damage = 0
                    
                    #Attack Condition
                    if (choice == '1'):
                        damage = random.randint(10,20)
                        critical = random.randint(1,100)
                        
                        #Critical Hit aspect
                        if (critical == 100):
                            damage * 10
                            enemy_hp  = enemy_hp - damage
                            dmg = str(damage)

                            print(name + " attacked.")
                            space = input()
                            print()
                            print("Critical hit! " + name + " dealt " + dmg + " damage.")
                            print()
                            
                        else:
                            enemy_hp = enemy_hp - damage
                            dmg = str(damage)

                            print(name + " attacked.")
                            space = input()
                            print()
                            print(name + " dealt " + dmg + " damage.")
                            print()

                        #Enemy Attack Path
                        attack = random.randint(10,15)
                        HP  = HP - attack
                        atk = str(attack)
                        health = str(HP)

                        print('The ' + enemy + ' attacks.')
                        print()
                        space = input()

                        print("The " + enemy + " dealt " + atk + " damage.")
                        print()

                        space = input()

                    #Run Condition
                    if (choice == '2'):
                        chance = random.randint(1,4)
                            
                        if (chance == 1 or chance == 2 or chance == 3):
                            print("You have escaped successfully!")
                            print()
                            break

                        if (chance == 4):
                            print("There was no way out.")
                            print()

                            HP  = HP - attack
                            atk = str(attack)
                            health = str(HP)

                            print('The ' + enemy + ' attacks.')
                            print()
                            space = input()

                    #Enemy Defeat Condition
                    if (enemy_hp <= 0):
                        experience += experience + random.randint(217,728)
                        exp_stat = str(experience)
                        win = win + 1

                        player.win()

                        player.exp = experience
                        player.HP = HP
                        player.wins = win

                        player.stats()

                        break

                        
                    #Game Over Condition
                    if (HP <= 0):
                        break
            
            #The Woods Biome
            if (option == 2):
                print("Alright, we're outside the woods. I heard the attacks from the inhabitants are hit or miss. Be careful as they are hard to run away from.")
                print("Press any key to continue")

                space = input()
                enemy = random.choice(woods_enemies)
                enemy_hp = 0 + random.randint(25,50)

                print("--You encounter a " + enemy + "!--")
                print()

                #Battle Condition
                while (victory == False):
                    print("What do you want to do?")
                    print("1. Fight")
                    print("2. Run")
                    print()

                    choice = input()
                    damage = 0
                        
                    #Fight Condition    
                    if (choice == '1'):
                        damage = random.randint(5,30)
                        critical = random.randint(1,100)

                        #Critical Hit Condition
                        if (critical == 100):
                            damage * 10
                            enemy_hp  = enemy_hp - damage
                            dmg = str(damage)

                            print(name + " attacked.")
                            space = input()
                            print()
                            print("Critical hit! " + name + " dealt " + dmg + " damage.")
                            print()
                            
                        else:
                            enemy_hp = enemy_hp - damage
                            dmg = str(damage)

                            print(name + " attacked.")
                            space = input()
                            print()
                            print(name + " dealt " + dmg + " damage.")
                            print()

                        #Enemy Attack Path
                        attack = 5
                        rage = random.randint(1,5)

                        #Rage Condition
                        if (rage == 5):
                            attack = attack * 8
                            print('The ' + enemy + ' attacks.')
                            print()
                            space = input()

                            HP  = HP - attack
                            atk = str(attack)
                            health = str(HP)

                            print("Ouch! The " + enemy + " dealt " + atk + " damage.")
                            print()

                        else :
                            HP  = HP - attack
                            atk = str(attack)
                            health = str(HP)

                            print('The ' + enemy + ' attacks.')
                            print()
                            space = input()

                        print("The " + enemy + " dealt " + atk + " damage.")
                        print()

                        space = input()

                    #Run Condition
                    if (choice == '2'):
                        chance = random.randint(1,4)

                        if (chance == 1):
                            print("You have escaped successfully!")
                            print()
                            break

                        if (chance == 2 or chance == 3 or chance == 4):
                            print("There was no way out.")

                            HP  = HP - attack
                            atk = str(attack)
                            health = str(HP)

                            print('The ' + enemy + ' attacks.')
                            print()
                            space = input()
                            
                    #Enemy Defeat Condition

                    if (enemy_hp <= 0):
                        experience += experience + random.randint(170,1307)
                        exp_stat = str(experience)
                        win = win + 1

                        player.win()

                        player.exp = experience
                        player.HP = HP
                        player.wins = win

                        player.stats()

                        break

                    #Game Over Condition
                    if (HP <= 0):
                        break
            
            #The Underpass Condition
            if (option == 3):
                print("We have arrived to the Underpass. We can't stay here too long however. The radiation is bound to hurt us.")
                print("Press any key to continue")

                space = input()
                enemy = random.choice(underpass_enemies)
                enemy_hp = 0 + random.randint(47, 63)

                print("--You encounter a " + enemy + "!--")
                print()

                #Battle Condition
                while (victory == False):
                    print("What do you want to do?")
                    print("1. Fight")
                    print("2. Run")
                    print()

                    choice = input()
                    damage = 0
                    
                    #Fight Condition
                    if (choice == '1'):
                        damage = random.randint(29,74)
                        critical = random.randint(1,17)

                        if (critical == 17):
                            damage * 3
                            enemy_hp  = enemy_hp - damage
                            dmg = str(damage)

                            print(name + " attacked.")
                            space = input()
                            print()
                            print("Critical hit! " + name + " dealt " + dmg + " damage.")
                            print()
                            
                        else:
                            enemy_hp = enemy_hp - damage
                            dmg = str(damage)

                            print(name + " attacked.")
                            space = input()
                            print()
                            print(name + " dealt " + dmg + " damage.")
                            print()

                        #Enemy Attack Path
                        attack = random.randint(0,7)
                        HP  = HP - attack
                        atk = str(attack)
                        health = str(HP)

                        print('The ' + enemy + ' attacks.')
                        print()
                        space = input()

                        #Enemy Miss Condition
                        if (attack == 0):
                            print('The ' + enemy + " missed!")
                            space = input()

                        else:
                            print("The " + enemy + " dealt " + atk + " damage.")
                            print()

                            space = input()

                        attack = random.randint(0,7)
                        HP  = HP - attack
                        atk = str(attack)
                        health = str(HP)

                        print('The ' + enemy + ' attacks.')
                        print()
                        space = input()

                        #Enemy Miss Condition
                        if (attack == 0):
                            print('The ' + enemy + " missed!")
                            space = input()

                        else:
                            print("The " + enemy + " dealt " + atk + " damage.")
                            print()

                            space = input()

                    #Run Condition
                    if (choice == '2'):
                        chance = random.randint(1,4)
                            
                        if (chance == 1 or chance == 2 or chance == 3):
                            print("You have escaped successfully!")
                            print()
                            break

                        if (chance == 4):
                            print("There was no way out.")
                            print()

                            HP  = HP - attack
                            atk = str(attack)
                            health = str(HP)

                            print('The ' + enemy + ' attacks.')
                            print()
                            space = input()

                    #Enemy Miss Condition
                    if (enemy_hp <= 0):
                        experience += experience + random.randint(300,420)
                        exp_stat = str(experience)
                        win = win + 1

                        player.win()

                        player.exp = experience
                        player.HP = HP
                        player.wins = win

                        player.stats()

                        break

                    #Game Over Condition
                    if (HP <= 0):
                        break
                    
                    #Damage per round Condition(Biome Specific)
                    HP = HP - 5

                    print(name + " took 5 damage from the radiation!")

            if (option == 4):
                player.rules()
                confirm = input()

            if (option == 5):
                player.stats()
                confirm = input()



if (win >= 5):
    player.victory()

if (HP <= 0):
    player.game_over()

