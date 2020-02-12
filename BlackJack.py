from random import choice as rand
from os import system as system

stage = [1]
score = [0]

def script():
    rngroll = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    deck = [
        [1, "Ace of Clubs", "Black", 11, 1],
        [2, "Ace of Spades", "Black", 11, 1],
        [3, "Ace of Diamonds", "Red", 11, 1],
        [4, "Ace of Hearts", "Red", 11, 1],
        [5, "2 of Clubs", "Black", 2],
        [6, "2 of Spades", "Black", 2],
        [7, "2 of Diamonds", "Red", 2],
        [8, "2 of Hearts", "Red", 2],
        [9, "3 of Clubs", "Black", 3],
        [10, "3 of Spades", "Black", 3],
        [11, "3 of Diamonds", "Red", 3],
        [12, "3 of Hearts", "Red", 3],
        [13, "4 of Clubs", "Black", 4],
        [14, "4 of Spades", "Black", 4],
        [15, "4 of Diamonds", "Red", 4],
        [16, "4 of Hearts", "Red", 4],
        [17, "5 of Clubs", "Black", 5],
        [18, "5 of Spades", "Black", 5],
        [19, "5 of Diamonds", "Red", 5],
        [20, "5 of Hearts", "Red", 5],
        [21, "6 of Clubs", "Black", 6],
        [22, "6 of Spades", "Black", 6],
        [23, "6 of Diamonds", "Red", 6],
        [24, "6 of Hearts", "Red", 6],
        [25, "7 of Clubs", "Black", 7],
        [26, "7 of Spades", "Black", 7],
        [27, "7 of Diamonds", "Red", 7],
        [28, "7 of Hearts", "Red", 7],
        [29, "8 of Clubs", "Black", 8],
        [30, "8 of Spades", "Black", 8],
        [31, "8 of Diamonds", "Red", 8],
        [32, "8 of Hearts", "Red", 8],
        [33, "9 of Clubs", "Black", 9],
        [34, "9 of Spades", "Black", 9],
        [35, "9 of Diamonds", "Red", 9],
        [36, "9 of Hearts", "Red", 9],
        [37, "10 of Clubs", "Black", 10],
        [38, "10 of Spades", "Black", 10],
        [39, "10 of Diamonds", "Red", 10],
        [40, "10 of Hearts", "Red", 10],
        [41, "Jack of Clubs", "Black", 10],
        [42, "Jack of Spades", "Black", 10],
        [43, "Jack of Diamonds", "Red", 10],
        [44, "Jack of Hearts", "Red", 10],
        [45, "Queen of Clubs", "Black", 10],
        [46, "Queen of Spades", "Black", 10],
        [47, "Queen of Diamonds", "Red", 10],
        [48, "Queen of Hearts", "Red", 10],
        [49, "King of Clubs", "Black", 10],
        [50, "King of Spades", "Black", 10],
        [51, "King of Diamonds", "Red", 10],
        [52, "King of Hearts", "Red", 10]
        ]
    hand = [int(0)]
    aceCount = [0]
    
    def drawcard():
        #chooses a random number 1-52
        x = rand(rngroll)        
        #removes card after drawn
        rngroll.remove(x)

        #adds the name of the card to the player's hand[1:]
        hand.append(deck[x-1][1])
        
        #Adds Value to the player's hand[0]
        hand[0] += int(deck[x-1][3])

        #Sets up a check to see if you hold an ace after you go over 21
        if 'Ace' in deck[x-1][1]:
            aceCount[0] += 1
        
        menu()

    def startGameCheck():
        #if hand[0], your value, is 0 then there is no game in progress.
        if stage[0] == 6:
            system('cls')
            print("You finished all 5 rounds. Your score was " + str(score[0]))
            print("If you want to play again, type 'blackjack' at the prompt. Goodbye!")
            exit()

        else:
            if int(hand[0]) == 0:
                system('cls')
                print("\nRound " + str(stage[0]) + " of 5\n")
                print("Your Hand: Empty!")
                print("Your Score: " + str(score[0]))
            else: 
                print("\nYour Hand: " + str(hand[1:]))
            print("Deck Value: " + str(hand[0]) + "\n")

    def scoring():
        if hand[0] < 21:
            score[0] += 3*(21-hand[0])
        elif hand[0] == 21:
            score[0] += 0
        elif hand[0] > 21:
            score[0] += 7 * (hand[0]-21)
        stage[0] += 1
        script()

    def menu():
        #prints appropriate text based on if a game is ongoing
        startGameCheck()
        
        if int(hand[0]) == 21: 
            print("You Win!")
            input("Press Enter to go to the next round... ")
            scoring()
        
        #If you're over 21...
        elif hand[0] not in range(0,21):
            #Ace check; if you don't have one the game is over
            if aceCount[0] == 0:
                print("You got over 21!")
                input("Press Enter to go to the next round...")
                scoring()

            #Ace check; if you have an ace your hand value drops by 10 and the game resumes
            elif aceCount[0] > 0:
                print("You got over 21, but you drew 1 or more Aces! One of them has been devalued to 1 to let you keep drawing")
                hand[0] += -10
                aceCount[0] += -1
                menu()
        
        else:
            while True:
                try:
                    card = int(input("Draw Card? 1 for yes or 2 to end the round "))
                    #add a check if you want to leave
                except ValueError:
                    drawcard()
                if card == int(1):
                    drawcard()
                elif card == int(2):
                    scoring()
    
    #executes Menu when script() is ran
    menu()
script()
