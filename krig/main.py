import random


def main():
    cards = [(val, color) for color in ["diamond", "club", "heart", "spades"] for val in range(2, 15)]

    p1 = []
    p2 = []

    # Distribute cards
    random.shuffle(cards)
    while cards:
        p1.append(cards.pop())
        p2.append(cards.pop())

    # Play the game
    try:
        while p1 and p2:
            round(p1, p2)
    except IndexError:
        pass

    if p1:
        print("Player 1 won the game!!!")
    elif p2:
        print("Player 2 won the game!!!")
    else:
        print("Wha")


def round(p1, p2):
    card1 = p1.pop()
    card2 = p2.pop()

    if card1[0] == card2[0]:
        if krig(p1, p2):
            p1.append(card1)
            p1.append(card2)
        else:
            p2.append(card1)
            p2.append(card2)

    elif card1[0] > card2[0]:
        p1.append(card1)
        p1.append(card2)
    else:
        p2.append(card1)
        p2.append(card2)


def krig(p1, p2) -> bool:
    pool1 = [p1.pop() for _ in range(3)]
    pool2 = [p2.pop() for _ in range(3)]

    if pool1[-1][0] == pool2[-1][0]:
        return krig(p1, p2)
    elif pool1[-1][0] > pool2[-1][0]:
        p1.extend(pool1)
        p1.extend(pool2)
        return True
    else:
        p2.extend(pool1)
        p2.extend(pool2)
        return False


if __name__ == "__main__":
    main()
