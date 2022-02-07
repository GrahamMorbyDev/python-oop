from cards import Card
import random


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Egg', 'Ork', 'Ham', 'Bus', 'Far', 'Gum', 'Hut', 'Gun']
        self.column_names = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for columns in self.column_names:
            for num in range(1, self.size + 1):
                self.locations.append(f'{columns}{num}')

    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)

    def create_row(self, num):
        row = []
        for column in self.column_names:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')
        return row

    def create_grid(self):
        header = ' |  ' + '  |  '.join(self.column_names) + '  |'
        print(header)
        for row in range(1, self.size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)

    def check_matched(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f'{card.location}: {card}')
            return False

    def check_win(self):
        for card in self.cards:
            if not card.matched:
                return False
        return True

    def check_location(self, time):
        while True:
            guess = input(f"What's the location of your {time} card? ")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print("That's not a valid location, it should look like this: A1")

    def start_game(self):
        game_running = True
        print('Welcome to a memory game')
        self.set_cards()
        while game_running:
            self.create_grid()
            guess1 = self.check_location('first')
            guess2 = self.check_location('second')
            if self.check_matched(guess1, guess2):
                if self.check_win():
                    print('Congratz!!! you have guess them all')
                    self.create_grid()
                    game_running = False
            else:
                input('Those cards are not a match. press enter to continue')
        print('GAME OVER')


if __name__ == '__main__':
    game = Game()
    game.start_game()
