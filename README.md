# Scrabble Word Game
## Introduction
This is an interactive word creation game that is a lot like Scrabble or Words With Friends. Letters are dealt to players, who then construct one or
more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.
Users can play the game by themselves or let the computer play the game.
* Code is written in Python.
* Four files are included: 1) helper_functions.py; 2) user_play.py; 3) computer_play.py; 4) word.txt.

## Rules of the game
 
#### Dealing
* A player is dealt a hand of n letters chosen at random (assume n = 7 in this library).
* The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
* Some letters may remain unused (these won't be scored).

#### Scoring
* The score for the hand is the sum of the scores for each word formed.
* The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points
  if all n letters are used on the first word created.
* Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. The
  dictionary SCRABBLE_LETTER_VALUES is defined to map each lowercase letter to its Scrabble letter value.
* For example, if n = 7, 'waybill' would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7 = 105, plus
  an additional 50 points bonus for using all n letters).
  
#### Playing
 Users can choose to play the game by themselves or let the computer play the game.

## Installation and Usages
* Downlaod all files in this repository and save them in the same folder.
* Run computer_play.py to play the game.
  
