import tkinter as tk
from tkinter import messagebox

class BlackjackGame:
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.has_doubled = False
        
        self.window = tk.Tk()
        self.window.title("Blackjack Game")
        
        # Dealer's hand
        self.dealer_frame = tk.Frame(self.window)
        self.dealer_frame.pack(pady=10)
        
        self.dealer_label = tk.Label(self.dealer_frame, text="Dealer's Hand: ")
        self.dealer_label.pack()

        self.dealer_value_label = tk.Label(self.dealer_frame, text="Total: ")
        self.dealer_value_label.pack(pady=(0, 10))

        
        # Player's hand
        self.player_frame = tk.Frame(self.window)
        self.player_frame.pack(pady=10)
        
        self.player_label = tk.Label(self.player_frame, text="Your Hand: ")
        self.player_label.pack()

        self.player_value_label = tk.Label(self.player_frame, text="Total: ")
        self.player_value_label.pack(pady=(0, 10))

        
        # Game controls
        self.control_frame = tk.Frame(self.window)
        self.control_frame.pack(pady=10)
        
        self.hit_button = tk.Button(self.control_frame, text="Hit", command=self.hit)
        self.stand_button = tk.Button(self.control_frame, text="Stand", command=self.stand)
        self.double_button = tk.Button(self.control_frame, text="Double", command=self.double)
        
        self.hit_button.pack(side=tk.LEFT, padx=5)
        self.stand_button.pack(side=tk.LEFT, padx=5)
        self.double_button.pack(side=tk.LEFT, padx=5)
        
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [(rank, suit) for suit in suits for rank in ranks]
        
    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)
        
    def deal_initial_cards(self):
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        
    def start_game(self):
        self.create_deck()
        self.shuffle_deck()
        self.deal_initial_cards()
        self.update_ui()
        
    def hit(self):
        self.player_hand.append(self.deck.pop())
        self.update_ui()
        
        if self.calculate_hand_value(self.player_hand) > 21:
            messagebox.showinfo("Result", "Bust! You lose.")
            self.reset_game()
        
        
        
    def stand(self):
        self.dealer_turn()
        self.determine_winner()
        self.reset_game()
        
        
        
    def double(self):
        if self.has_doubled:
            messagebox.showinfo("Result", "Already doubled down this hand.")
            return
            
        self.hit()
        self.update_ui()
        self.has_doubled = True
        
        if self.calculate_hand_value(self.player_hand) > 21:
            messagebox.showinfo("Result", "Bust! You lose.")
            self.reset_game()
        
    def update_ui(self):
        dealer_text = "Dealer's Hand: " + " ".join([card[0] for card in self.dealer_hand])
        player_text = "Your Hand: " + " ".join([card[0] for card in self.player_hand])
        
        self.dealer_label.config(text=dealer_text)
        self.player_label.config(text=player_text)
        
    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        
        for rank, _ in hand:
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
            else:
                value += int(rank)
        
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value
                
    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
            
    def determine_winner(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        
        if player_value > 21:
            messagebox.showinfo("Result", "Bust! You lose.")
        elif dealer_value > 21:
            messagebox.showinfo("Result", "Dealer bust! You win!")
        elif player_value > dealer_value:
            messagebox.showinfo("Result", "You win!")
        elif dealer_value > player_value:
            messagebox.showinfo("Result", "Dealer wins!")
        else:
            messagebox.showinfo("Result", "It's a tie!")
            
    def reset_game(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.start_game()
        
if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()
    game.window.mainloop()
