from .card import Deck
from .state import GameState, Player, Team


def start_game(player_count: int, team_count: int) -> GameState:
    if player_count < 2:
        raise ValueError("Cannot start a game with less than 2 players")
    if team_count < 2:
        raise ValueError("Cannot start a game with less than 2 teams")

    teams = [Team(f"team-{n}") for n in range(team_count)]
    players = [Player(f"player-{n}") for n in range(player_count)]

    for i, p in enumerate(players):
        teams[i % team_count].players.append(p)

    decks = 2 if player_count < 6 else player_count // 2
    deck = Deck(decks)

    # deck.draw could take 11 as an argument, however that would make it lean towards some players, in my humble opinon
    for _ in range(11):
        for player in players:
            player.hand.append(*deck.draw())

    game_state = GameState(teams, deck)

    return game_state
