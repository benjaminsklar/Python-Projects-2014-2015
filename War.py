# Ben Sklar# WAR card game.# From 1 to 15 players compete against a dealer.# Keeps track of wins, losses, and ties (Extra Extension).# Includes all extensions.# Imports 2 needed modules.import cards, games_upgraded # Defines what exactly a card is in the game of WAR.class WAR_Card(cards.Card):    """ A WAR Card. """    @property    def value(self):        # If card is an Ace, 14 points (highest).        if self.rank == "A":            v = 14        else:            v = WAR_Card.RANKS.index(self.rank) + 1        return vclass WAR_Deck(cards.Deck):    """ A WAR Deck. """    def populate(self):        for suit in WAR_Card.SUITS:             for rank in WAR_Card.RANKS:                 self.cards.append(WAR_Card(rank, suit))    class WAR_Hand(cards.Hand):    """ A WAR Hand. """    def __init__(self, name):        super(WAR_Hand, self).__init__()        self.name = name        self.score = [0, 0, 0]    def __str__(self):        rep = self.name + ":\t" + super(WAR_Hand, self).__str__()          if self.total:            rep += "(" + str(self.total) + ")"                return rep    @property         def total(self):        # If a card in the hand has value of None, then the total is None.        for card in self.cards:            if not card.value:                return None                # Add up the card values.        t = 0        for card in self.cards:              t += card.value           return t    # Keeps the game running.    # Total will never exceed 14 points, chose > 15 to be safer.    def is_over(self):        return self.total > 15class WAR_Player(WAR_Hand):    """ A WAR Player. """    # Add 1 loss to player's score.    def lose(self):        print(self.name, "loses.")        self.score[1] += 1    # Add 1 win to player's score.    def win(self):        print(self.name, "wins.")        self.score[0] += 1    # Add 1 tie to player's score.    def tie(self):        print(self.name, "ties.")        self.score[2] += 1        class WAR_Dealer(WAR_Hand):    """ A WAR Dealer. """    def flip_first_card(self):        first_card = self.cards[0]        first_card.flip()class WAR_Game(object):    """ A WAR Game. """    def __init__(self, names):              self.players = []        for name in names:            player = WAR_Player(name)            self.players.append(player)                self.dealer = WAR_Dealer("Dealer")        # Create's deck, populates it, then shuffles it at beginning.        self.deck = WAR_Deck()        self.deck.populate()        self.deck.shuffle()    # While game is still being played, game is not over.    @property    def still_playing(self):        sp = []        for player in self.players:            if not player.is_over():                sp.append(player)        return sp    def play(self):        # Deal initial 1 card to everyone.        self.deck.deal(self.players + [self.dealer], per_hand = 1)        for player in self.players:            print(player)        print(self.dealer)        # Compare each player still playing to the dealer.        # Check if player won, lost, or tied the dealer.        for player in self.still_playing:            if player.total > self.dealer.total:                    player.win()            elif player.total < self.dealer.total:                    player.lose()            else:                player.tie()        # Remove everyone's cards after a round.        for player in self.players:            player.clear()        self.dealer.clear()# Main function.def main():    # Welcomes player to the game of WAR.    print("\t\tWelcome to WAR!\n")    names = []    # Made my own function for this, since original had errors.    # Won't break if you press enter without a value anymore.    # Asks for number of players. Only accepts digits between 1-15.    number = games_upgraded.ask_number("How many players? (1 - 15): ", low = 1, high = 16)    for i in range(number):        name = input("Enter player name: ")        names.append(name)    # Begin the game.    game = WAR_Game(names)    # Checks to make sure there are enough cards to deal and play before each hand.    # If not enough, ends game.    again = None    while again != "n" and len(game.deck.cards) >= number + 1:        game.play()        again = games_upgraded.ask_yes_no("\nDo you want to play again? (y/n): ")        if len(game.deck.cards) < number + 1 and again == "y":            # If player says yes, but not enough cards in the deck, ends the game.            print("Not enough cards to deal. Ending game.")    # Prints the final scores neatly, by player's wins, losses, and ties.    print("\nFINAL SCORES:")    for i in range(number):        print("\n", names[i])        print("Wins:", "Losses:", "Ties:")        print(game.players[i].score[0], "\t", game.players[i].score[1], "\t", game.players[i].score[2])    main()input("\n\nPress the enter key to exit.")