import random
from enum import Enum, IntEnum
from typing import Optional


class Suit(Enum):
    Heart = "heart"
    Spade = "spade"
    Diamond = "diamond"
    Club = "club"


class Rank(IntEnum):
    Joker = 15
    Ace = 14
    King = 13
    Queen = 12
    Jack = 11
    Ten = 10
    Nine = 9
    Eight = 8
    Seven = 7
    Six = 6
    Five = 5
    Four = 4
    Three = 3
    Two = 2


class Card:
    rank: Rank
    suit: Optional[Suit]
    is_wild: bool
    is_red: bool  # Only relevant for 3's
    point_value: int

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = None if rank == Rank.Joker else suit

        # Is wild status
        self.is_wild = rank in (Rank.Two, Rank.Joker)

        # Is red status
        if rank == rank.Three:
            self.is_red = suit in (Suit.Heart, Suit.Diamond)

        # Point value determination
        if 4 <= rank <= 7:
            self.point_value = 5
        elif 8 <= rank <= Rank.King:
            self.point_value = 10
        elif rank in (2, Rank.Ace):
            self.point_value = 20
        elif rank == Rank.Joker:
            self.point_value = 50
        elif rank == Rank.Three:
            self.point_value = 100 if self.is_red else 0
        else:
            raise ValueError(f"'{rank}' of '{suit}' is unrecognized")

    def __str__(self):
        if self.rank == Rank.Joker:
            return f"{Rank.Joker}"
        return f"{self.rank.name} of {self.suit.name}"

    def __repr__(self):
        if self.rank == Rank.Joker:
            return f"<{Rank.Joker}>"
        return f"<{self.rank.value}-{self.suit.value}>"

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    # def __lt__(self, other):
    #     pass


class Deck:
    cards: list[Card]

    def __init__(self, deck_count: int = 1, seed: Optional[int] = None):
        if deck_count < 1:
            raise ValueError("deck_count cannot be less than 1")

        if seed:
            random.seed(seed)

        self.cards = [Card(rank, suit) for suit in Suit for rank in Rank] * deck_count
        random.shuffle(self.cards)

    def draw(self, n: int = 1):
        if n < 1:
            # i know its wierd to raise key error but i dont want the same error type
            raise KeyError("Cannot draw less than 1 card")
        if len(self.cards) < n:
            raise ValueError("Not enough cards to draw")
        drawn, self.cards = self.cards[:n], self.cards[n:]
        return drawn

    def __len__(self):
        return len(self.cards)
