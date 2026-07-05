from dataclasses import dataclass, field

from .card import Card, Deck, Rank, Suit


@dataclass
class Player:
    name: str
    hand: list[Card] = field(default_factory=list)


@dataclass
class Team:
    name: str
    players: list[Player] = field(default_factory=list)
    melds: dict[Rank, list[Card]] = field(default_factory=dict)
    score: int = 0
    red_threes: list[Card] = field(default_factory=list)


@dataclass
class GameState:
    teams: list[Team]
    stock: Deck
    discard_pile: list[Card] = field(default_factory=list)
    turn_idx: int = 0

    @property
    def current_player(self) -> Player:
        all_players = [p for t in self.teams for p in t.players]
        return all_players[self.turn_idx % len(all_players)]
