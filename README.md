# Python Blackjack Game

## Description
A simple implementation of the Blackjack card game in Python using Tkinter for the user interface.

## Features
- Play Blackjack against a dealer
- Dealer follows standard rules (hits until 17, stands on soft 17)
- Player can Hit, Stand, or Double (once per hand)
- Clear display of cards and hand totals
- Automatic game reset after each round

## How to Run
1. Ensure you have Python installed
2. Install Tkinter (usually comes with Python installation)
3. Save this code in a file called `main.py`
4. Run the game using the command: 
   ```
   python main.py
   ```

## Game Rules
- The goal is to get a hand value closer to 21 than the dealer without going over
- Aces count as 1 or 11
- Face cards (J, Q, K) count as 10
- The dealer must hit until reaching 17 or higher

## Controls
- **Hit**: Take another card
- **Stand**: End your turn, let the dealer play
- **Double**: Double your stake and take one extra card (only once per hand)
