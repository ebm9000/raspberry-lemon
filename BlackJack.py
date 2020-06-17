from random import choice as rand
from os import system as system

#round number
stage = [1]

#total score
score = [0]

def script():
    #possible values you can roll; resets each round to ensure proper RNG
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
    hand = [0]
    aceCount = [0]
    
    def drawcard():
        #chooses a random number 1-52; based off of the rngroll table
        x = rand(rngroll)        
        #removes card after drawn; based off of value drawn, not the position in table
        rngroll.remove(x)

        #adds the name of the card to the player's hand[1:]; 'x' was a value, but now it is used to get a value based on >position< in the >deck< table; offset by 1
        hand.append(deck[x-1][1])
        
        #Adds Value to the player's hand[0]; aces are assumed as 11 for now
        hand[0] += int(deck[x-1][3])

        #If you go over 21, checks to see if you have an ace
        if 'Ace' in deck[x-1][1]:
            aceCount[0] += 1
        
        scorecheck()

    #basic UI
    def menu():
        #Ends the game if 5 rounds are completed
        if stage[0] == 6:
            system('cls')
            print("You finished all 5 rounds. Your score was " + str(score[0]))
            print("If you want to play again, type 'blackjack' at the prompt. Goodbye!")
            exit()

        else:
            #if stage[0] is 1, start a game (default when launched)
            system('cls')
            print("\nRound " + str(stage[0]) + " of 5\n")
            print("Your Score: " + str(score[0]))

            #stage[0] is never 0; but if it is set to == 1 here, then the script does not print your hand!
            if int(stage[0]) == 0:
                print("Your Hand: Empty!")
            else: 
                print("\nYour Hand: " + str(hand[1:]))
           
            #makes more logical sense to print Hand Value after printing the contents of your Hand
            print("Hand Value: " + str(hand[0]) + "\n")

    #Tallys game score, reruns script() to reset rngroll, deck and hand. var 'score' is exclusive
    def eor_scoring():
        if hand[0] < 21:
            score[0] += 3*(21-hand[0])
        elif hand[0] == 21:
            score[0] += 0
        elif hand[0] > 21:
            score[0] += 7 * (hand[0]-21)
        stage[0] += 1
        script()

    #runs menu() followed by itself; checks current hand value and catches if over 20
    def scorecheck():

        menu()
        
        if int(hand[0]) == 21: 
            print("You Win!")
            input("Press Enter to go to the next round... ")
            eor_scoring()
        
        #If your scoe is over 21... can't become negative at any time
        elif hand[0] > 21:
            #Ace check; if you don't have one the game is over
            if aceCount[0] == 0:
                print("You got over 21!")
                input("Press Enter to go to the next round...")
                eor_scoring()

            #Ace check; if you have an ace your hand value drops by 10 and the game resumes
            elif aceCount[0] > 0:
                print("You got over 21, but you drew 1 or more Aces! One of them has been devalued to 1 to let you keep drawing")
                
                #devalues a single ace by 10, removes it from the deck, then continues
                hand[0] += -10
                aceCount[0] += -1
                scorecheck()
    
        
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
                    eor_scoring()
    
    #executes Menu when script() is ran
    scorecheck()
script()