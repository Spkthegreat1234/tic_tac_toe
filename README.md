# tic_tac_toe
To make a tic tac toe game using python 
This game is written on a simple python code simulate a python game with the user and the computer

_**Note**: The computer will not mark its moves randomly and makes logical moves in order to win. Winning positions are known to the computer and it will
play accordingly._

The modules used are:
  1. **Random module:** It has been used to generate random numbers from 1-9 to allocate positions for the             computer to mark.

The Global variables are:
  1. **Board:** Generates a list of 9 whitespace characters to represent the board.
  2. **Player & Computer:** Initializes the character played by the player and the computer which are _"X"_ and _      _"O"_ respectively.
  3. **Winning Combinations:** Stores a tuple of tuples , each element tuple consists of 3 numbers which represent     the positions to be
    occupied by the player or the computer in order to secure a victory (for eg: 1,2 and 3).
      
The functions used in the code are as follows:
  1. **"draw_board:"** Generates the characters stored in the _Board_ variable into a neat matrix form that is         readable by the user.
  2. **is_board_full:** Checks the board if all the whitespaces have been replaced by _'X'_ or _'O'_ and returns       _True_ or _False_ .
  3. **is_winner:** Checks to see if the player has filled their respective characters in the winning positions,       returns _True_ or _False_ accordingly.
  4. **is_computer_winner:** Checks to see if the computer has filled their respective characters in the winning       positions, returns _True_ or _False_ accordingly.
  5. **is_space_free:** Checks if there are any remaining free spaces in the board and returns _True_ or _False_.
  6. **insert_letter:** Takes input of _'X'_ or _'O'_ into the board.
  7. **player_move:** Used to take input from the player into the board and allows only valid positions(empty and       between 1 to 9).
  8. **computer_move:** This is the main algorithm working behind the moves made by the computer.
     a. It creates a list _possible_moves_ that has the remaining positions.
     b. It checks the board if the computer can fill any position and secure a victory, if not it proceeds next.
     c. It next checks the corners(1,3,7,9) and if they are open it fills any corner from the board and assigns it         to the move variable. If no corners are free it proceeds further.
     d. It checks if the centre of the board(5) is free and if found empty sets 5 as the move variable's value. If         centre is found to be filled it proceeds further. 
     e. Next it checks the edge positions(2,4,6,8) and randomly fills any empty edge position by assigning it to           the move variable 

      
