# Rock Paper Scissors

This is my version of the classic Rock, Paper, Scissors game.
Player makes a choice and then the computer randomly makes its choice. The winner is determined by the outcome of the two choices. Or maybe both make the same choice and then it's a tie!
The rules of the game are: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.

Link to [live version of my project](https://rps-project-2e54f529f3b1.herokuapp.com/)

<img width="75%" alt="Am I Responsive" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/72f20da3-b363-4f9f-91f2-cabf731b03a0">


## Features 

### The start of the game

This is where the player is asked to make their move by typing one of the three options provided.

<img width="50%" alt="Start of game" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/06c66f96-71bd-4045-bc16-b28d54f88f3b">


### Player choice and result

The player makes a move and then the computer makes a random choice. The result is presented, in this case player wins.

<img width="50%" alt="Your choice and result" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/52af4d6b-f409-4b01-970a-a608120ff997">


A different outcome. Player lost the game.

<img width="50%" alt="You lose" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/f7d51734-0ccb-40e3-aec4-d82a2df060cc">


Or, both make the same choice, it's a tie.

<img width="50%" alt="Its at tie!" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/08057dd1-b75d-408d-bc08-e469fd9c82fd">


### To continue game

When the result has been presented the player has the option to choose if they want to continue playing by typing the answer yes or no. If the choice is yes the games starts over.

<img width="50%" alt="Answer yes - continue game" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/f8d76fd0-c43c-4e55-89f2-55c01521c88f">


If the choice is no the game will break.

<img width="50%" alt="Answer no - break" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/ae049678-89f7-46f6-ba0a-571f0000ca28">


### Invalid inputs

If player types anything else than the three options provided the game will announce that a valid choice is required and give the player another chance to make a correct move.

<img width="50%" alt="Your choice invalid" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/fb314801-efa2-44df-ad44-05bdd9532929">


The same goes for the answer to continue or quit game. The game will announce that a valid choice is required if player types anything else than yes or no.

<img width="50%" alt="Answer invalid" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/b657f898-b3fa-4022-9f6f-143f96d8c8b8">


## Testing

The game has been run through the CI Python Linter without any errors.

<img width="75%" alt="CI Python Linter" src="https://github.com/InglisSofia/rock-paper-scissors/assets/143741255/2b179218-e34e-4a8f-a6d8-faf0a792c3c7">


## Bugs

### Unsolved bugs

- When player makes an invalid choice more than once when asked to continue game (yes/no) the game automatically continues after the second invalid input.
- In the live version, if player answers "no" when asked to continue game the game breaks. However if an invalid input is made first, the player types "no" the game continues. This doesn't happen when testing in Codeanywhere.

## Deployment

Step by step how the deployment wnt on
