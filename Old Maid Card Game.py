
# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     for i in range(0,len(deck),2):
         other=other+[deck[i]]
         if (i+1)<len(deck):
             dealer=dealer+[deck[i+1]]
             
     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    l.sort()
    previous=""
    for i in range(len(l)):
        if l[i][0]!=previous:
            y=1
            for x in range(i+1,len(l)):
                if l[i][0]==l[x][0]:
                    y=y+1
            if y%2==1:
                no_pairs=no_pairs+[l[i]]
            
        previous=l[i][0]
        
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    print("\n", end="")
    for i in deck:
        print(i, end=" ")
    print("\n")
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     integer=0
     while int(integer)>n or int(integer)<1:
         integer=input("Give me an integer between 1 and "+str(n)+": ")

     return integer

def addCard(deck, s):
    '''
    (list of str, str)->list of str
    Returns the deck of cards with the added card s.
    '''
    deck.append(s)
    return deck

def removeCard(deck, s):
    '''
    (list of str, str)->list of str
    Returns the deck of cards with the removed card s.
    '''
    deck.remove(s)
    return deck

def determineSuffix(num):
    '''
    (str)->str
    Adds the proper suffix to a number so it can be used in writing.
    '''
    if int(num)>9:
        tempNum=num[1]
    else:
        tempNum=num
        
    if tempNum=="1":
        suffix="st"
    elif tempNum=="2":
        suffix="nd"
    elif tempNum=="3":
        suffix="rd"
    else:
        suffix="th"
    return num+suffix

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     print("*"*60)
     while len(dealer)!=0 and len(human)!=0:
         print("Your turn.\n")
         print("Your current deck of cards is:")
         print_deck(human)

         #Human card choice
         dealerNum=len(dealer)
         print("I have "+str(dealerNum)+" cards. If 1 stands for my first card and "+str(dealerNum)+" for my last card, which of my cards would you like?")   
         cardChoice=get_valid_input(dealerNum)
         print("You asked for my "+determineSuffix(cardChoice)+" card.")
         cardChoice=int(cardChoice)

         chosen=dealer[cardChoice-1]
         print("Here it is. It is "+chosen+"\n")

         print("With "+chosen+" added, you current deck of cards is: ")
         human=addCard(human, chosen)
         dealer=removeCard(dealer,chosen)
         print_deck(human)
         print("And after discarding pairs and shuffling, your deck is: ")
         human=remove_pairs(human)
         print_deck(human)
         
         wait_for_player()
         print("*"*60)
         #Robot card choice
         if len(human)!=0 and len(dealer)!=0:
             print("My turn.\n")
             cardChoice=random.randint(1, len(human))
             chosen=human[cardChoice-1]
             dealer=addCard(dealer,chosen)
             human=removeCard(human,chosen)

             print("I took your "+determineSuffix(str(cardChoice))+" card")
             dealer=remove_pairs(dealer)
             wait_for_player()
             print("*"*60)


     if len(dealer)==0:
         print("Ups. I do not have any more cards")
         print("You lost! I, Robot, win")
     else:
         print("Ups. You do not have any more cards")
         print("Congratulations! You, Human, win")
        
         
     

# main
play_game()
