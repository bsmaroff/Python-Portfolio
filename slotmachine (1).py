#Benjamin Smaroff
#Slot Machine
#Initialize
symbols = ["7", "♣", "♥", "♠", "♦", "☆", "☂", "✸", "✽"]
credits = 100
import random
import time
#Functions
def slotmachine():
    print("Welcome to Ben's Casino Slot Machines!")
    while True:
        global symbols
        global credits
        if credits>0:
            play = input("Would you like to spin or quit (S/Q)")
            if play == "S":
                bet = int(input("How many credits would you like to bet?"))
                credits = credits - bet
                print("Spinning...")
                time.sleep(1)
                slot1 = (random.choice(symbols))
                print(slot1)
                time.sleep(1)
                slot2 = (random.choice(symbols))
                print(slot1+slot2)
                time.sleep(1)
                slot3 = (random.choice(symbols))
                print(slot1+slot2+slot3)
                if slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("You won the jackpot!")
                    credits = credits + (bet*100)
                    print("Credits: " + str(credits))
                elif slot1 == slot2 == slot3:
                    print("You win!")
                    credits = credits + (bet*10)
                    print("Credits: " + str(credits))
                elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                    print("Two of a kind!")
                    credits = credits + (bet*2)
                    print("credits: " + str(credits))
                else:
                    print("You lost")
                    print("Credits: " + str(credits))
            if play =="Q":
                print("Come back soon!")
                break
        else:
            print("Sorry you ran out of credits")
            break
#Main
slotmachine()
#Couldn't find probability weights, so I skipped to 3rd expansion

