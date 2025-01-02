# Mancala Game Simulator

## Description
This project is the Mancala game implemented in Python. It allows two players to compete in the classic Mancala board game, featuring visual board representation and a turn-based gameplay system.

## Features
- **Interactive Gameplay**  
  - Two players can input their names and take turns moving stones between cups.  
  - Special rules, such as extra turns for landing in the Mancala, are implemented.  

- **Dynamic Board Rendering**  
  - Displays the game board in a visually formatted ASCII art style.  
  - Real-time updates of the board after each move.  

- **Victory Determination**  
  - Automatically detects when the game ends.  
  - Announces the winner based on stone counts in the Mancalas.  

- **Customizable Parameters**  
  - Adjustable board dimensions and block sizes for flexibility.  

## Gameplay Instructions
1. Players are prompted to enter their names at the start.  
2. Players take turns selecting cups to move stones.  
3. The game board updates after each move to reflect the new state.  
4. The game ends when one player's side is empty, and the winner is determined by comparing Mancala stone counts.  

## Code Highlights
- **Game Logic**  
  - Implements Mancala rules, including redistributing stones and handling special conditions (e.g., extra turns, no stones in a cup).  

- **Board Rendering**  
  - Custom ASCII-based representation for cups, Mancalas, and stones.  

- **Victory Conditions**  
  - Automatically checks if all cups on one side are empty to determine the winner.  

## How to Run
1. Clone the repository:  
   ```bash
   python Mancala.pyc
