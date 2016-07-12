This is a word game that is a lot like Scrabble or Words With Friends. Letters are dealt to players, who then construct one or more words out of their letters. 
Each valid word receives a score, based on the length of the word and the letters in that word. 
Users can play the game by themselves or let the computer to play it!

The rules of the game are as follows:

-Dealing
* A player is dealt a hand of n letters chosen at random (assume n = 7 for now).

* The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

* Some letters may remain unused (these won't be scored).

-Scoring
* The score for the hand is the sum of the scores for each word formed.

* The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

* Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. I have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

* For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiplied by lengthe of 'weed' to get (4+1+1+2)*4 = 32). 

* As another example, if n = 7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7 = 105, plus an additional 50 points bonus for using all n letters).
 
