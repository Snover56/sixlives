# Written by Matthew Quinn
# Last updated: 2/20/20


import time
import random as r
#name = input('#   ')
#all random dice values were commented out, with predetermined values used instead. This is for testing purposes.

stage = 1
prename = input('Welcome to the Game of Life. What is your name?   ').strip()
name = prename[0].upper() + prename[1:].lower()

while(stage == 1):
    if name == '':
        name = input("That's not a name. What's your real name?   ").upper().strip()
    else:
        stage = 2

rolldice = input('Hello ' + name + ', will you roll the dice of life?   ').upper()

while(stage == 2):

    if rolldice == 'YES':
        stage = 3
    else:
        input('You must roll the dice of life. as it makes you alive.')
        rolldice = input('Will you roll the dice of life?   ').upper()

print('Rolling...   ')
time.sleep(2.25)
#dice = r.randint(1, 6)
dice = 1
input('You rolled a ' + str(dice) + '.')
print('Loading your life...   ')
time.sleep(2.25)
print('...   ')
time.sleep(2.25)

rice = 0
hoe = 0
widerhoe = 0
autohoeinator = 0

while(dice == 1):

    print('It is 1000 BC, and you are a 40 year old rice farmer in China. You are living in your cabin, where you settled next to a fertile land, ideal for growing rice. What will you do?')
    riceinput = input('Gather Rice, See Rice, Shop   ').upper()
    dice = 10

    while(dice == 10):

        #rice collection ways
        if riceinput == 'Gather rice'.upper() and hoe == 0 and widerhoe == 0 and autohoeinator == 0:
            rice = rice + 1
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()
        elif riceinput == 'Gather rice'.upper() and hoe == 1 and widerhoe == 0 and autohoeinator == 0:
            rice = rice + 2
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()
        elif riceinput == 'Gather rice'.upper() and widerhoe == 1 and autohoeinator == 0:
            rice = rice + 5
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()
        elif riceinput == 'Gather rice'.upper() and hoe == 0 and widerhoe == 0 and autohoeinator == 1:
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 1
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()
        elif riceinput == 'Gather rice'.upper() and hoe == 1 and widerhoe == 0 and autohoeinator == 1:
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 2
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()
        elif riceinput == 'Gather rice'.upper() and widerhoe == 1 and autohoeinator == 1:
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            print('You have ' + str(rice) + ' rice.')
            time.sleep(0.05)
            rice = rice + 5
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()

        #everything else
        elif riceinput == 'See Rice'.upper():
            riceinput = input('You have ' + str(rice) + ' rice.   ').upper()

        elif riceinput == 'Shop'.upper():
            shoploop = 1
            print('Welcome to the Shop. Options:   ')
            print('[1] Hoe (10 rice)   ')
            print('[2] Wider Hoe (30 rice)   ')
            print('[3] Autohoeinator (75 rice)   ')
            print('[4] Mysterious Rock (1000 rice)   ')
            print('[5] Exit   ')
            shopinput = input('What will you buy?   ').upper()
            while(shoploop == 1):

                if shopinput == 'HOE' and rice >= 10:
                    rice = rice - 10
                    hoe = 1
                    input('You have bought the Hoe.')
                    shopinput = input('You have bought the Hoe.   ').upper()
                elif shopinput == '1' and rice >= 10:
                    rice = rice - 10
                    hoe = 1
                    shopinput = input('You have bought the Hoe.   ').upper()

                elif shopinput == 'WIDER HOE' and rice >= 30:
                    rice = rice - 30
                    widerhoe = 1
                    shopinput = input('You have bought the Wider Hoe.   ').upper()
                elif shopinput == '2' and rice >= 30:
                    rice = rice - 30
                    widerhoe = 1
                    shopinput = input('You have bought the Wider Hoe.   ').upper()

                elif shopinput == 'AUTOHOEINATOR' and rice >= 75:
                    rice = rice - 75
                    autohoeinator = 1
                    shopinput = input('You have bought the Autohoeinator.   ').upper()
                elif shopinput == '3' and rice >= 75:
                    rice = rice - 75
                    autohoeinator = 1
                    shopinput = input('You have bought the Autohoeinator.   ').upper()
                    #endphase
                elif shopinput == 'MYSTERIOUS ROCK' and rice >= 1000:
                    rice = rice - 1000
                    mysteriousrock = 1
                    shoploop = 0
                    dice = 2
                    #dice = r.randint(2, 6)
                    input('You have bought the Mysterious Rock.')
                    input('As you carry the mysterious rock outside of the shop, you hear a slight humming sound emanating from it.')
                    input('The humming grows louder as the rock produces a blinding white light. It trembles between your hands as the sound and light becomes too intense to bear.')
                    input('You drop the rock, and it falls to the ground, shattering.')
                    input('Within it, a die. The number ' + str(dice) + ' faces upwards.')
                    input('Your perception of the world begins to deteriorate.')
                    print('Loading your life...   ')
                    time.sleep(2.25)
                    print('...   ')
                    time.sleep(2.25)
                elif shopinput == '4' and rice >= 1000:
                    rice = rice - 1000
                    mysteriousrock = 1
                    shoploop = 0
                    dice = 2
                    #dice = r.randint(2, 6)
                    input('You have bought the Mysterious Rock.')
                    input('As you carry the mysterious rock outside of the shop, you hear a slight humming sound emanating from it.')
                    input('The humming grows louder as the rock produces a blinding white light. It trembles between your hands as the sound and light becomes too intense to bear.')
                    input('You drop the rock, and it falls to the ground, shattering.')
                    input('Within it, a die. The number ' + str(dice) + ' faces upwards.')
                    input('Your perception of the world begins to deteriorate.')
                    print('Loading your life...   ')
                    time.sleep(2.25)
                    print('...   ')
                    time.sleep(2.25)

                elif shopinput == 'EXIT':
                    shoploop = 0
                    riceinput = '0'
                elif shopinput == '5':
                    shoploop = 0
                    riceinput = 'whereami'

                else:
                    shopinput = input('Invalid selection/you are short on rice.   ').upper()

        elif riceinput == 'whereami':
            riceinput = input('You have left the shop and are back on the rice field.   ').upper()

        else:
            riceinput = input('You may either Gather Rice, See Rice, or Shop.   ').upper()


while(dice == 2):
    k

while(dice == 3):
    k

while(dice == 4):
    k

while(dice == 5):
    k

while(dice == 6):
    k
