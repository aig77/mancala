# Mancala
Play against a Mancala AI solved using minimax.

## Rules
1. The game begins with a player picking up all the stones in any of the pits on their side.
2. Moving counterclockwise, the player places a stone in each pit until they run out.
3. A player places a stone in the store when passing their own Mancala. However they do not place one when passing their opponent's Mancala. The Mancala keeps track of the player's score.
4. If the last stone is placed in their Mancala, the player repeats their turn.
5. If the last stone is dropped in an empty pit on the player's side, the piece is captured (placed in the player's Mancala) along with the stones in the opponent's adjacent pit.
6. The game ends when all the pits on one side are empty.
7. The player with remaining stones captures all those pieces.
8. The winner of the game goes to the player with more stones in their Mancala. 

## Instructions
Select the amount of pits and stones to begin the game with. The depth is defaulted to 30 but can be changed in the code. Keep in mind that increasing the number of pits and stones in the beginning of the game increases the state space. If the state space is too large, the program will crash due to infinite recursion. The depth value is there to keep that in check but is still a possibility. 
