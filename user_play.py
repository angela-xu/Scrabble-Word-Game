from helper_functions import *


#
# #1: Users play a hand
#
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total = 0
    while calculateHandlen(hand) > 0:
        print('Current Hand: '),
        displayHand(hand)
        w = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if w == '.':
            break
        else:
            if isValidWord(w, hand, wordList) == False:
                print('Invalid word, please try again.')
                print('\n')
            else:
                s = getWordScore(w, n)
                total += s
                print('"' + w + '"' + ' earned ' + str(s) + ' points. Total: ' + str(total))
                print('\n')
                hand = updateHand(hand, w)
                
    if w == '.':
        print('Goodbye! Total score: ' + str(total))
    else:
        print('Run out of letters. Total score: ' + str(total) + ' points')


#
# #2: Users play the game
# 
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    hand = {}
    while True:
        x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if x == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            print('')
        elif x == 'r':
            if hand == {}:
                print('You have not played a hand yet. Please play a new hand first!')
                print('')
            else:
                playHand(hand, wordList, HAND_SIZE)
                print('')
        elif x == 'e':
            break
        else:
            print('Invalid command.')
            print('')
    print('\n')


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
